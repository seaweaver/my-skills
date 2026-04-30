#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smartbi Report CLI — 查询与导出一体化
查询当前登录用户可访问的 Smartbi 报表，并支持导出。

子命令:
  login      AD域登录，获取Token
  logout     登出，删除本地Token
  list       查询/搜索报表列表
  params     查询报表参数及备选值（JSON输出）
  info       查询报表参数（表格输出，供用户查看）
  export     导出报表

Usage:
  python smartbi_report.py login -u <用户名>                     # AD域登录
  python smartbi_report.py logout                                # 登出
  python smartbi_report.py list --json                           # 查询所有报表(JSON)
  python smartbi_report.py list -s "关键词" --json               # 搜索报表
  python smartbi_report.py params -r <report_id>                 # 查询参数(JSON)
  python smartbi_report.py info -r <report_id>                   # 查看参数(表格)
  python smartbi_report.py export -r <report_id> -t EXCEL2007    # 导出报表
"""

import requests
import json
import os
import sys
import getpass
from datetime import datetime


# ── 配置 ────────────────────────────────────────────────────────

TOKEN_DIR = os.path.join(os.path.expanduser("~"), ".smartbi")
TOKEN_FILE = os.path.join(TOKEN_DIR, "token.json")


def _resolve_token_path(config):
    """从配置中获取 token 路径并展开 ~ 为用户目录"""
    return os.path.expanduser(config.get('token_path', TOKEN_FILE))


def _extract_host_port(url):
    """从 URL 中提取 host:port 部分，忽略路径前缀"""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"
    except Exception:
        return url


def load_config():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


# ── Token 管理 ─────────────────────────────────────────────────

def load_token(config):
    """从本地文件读取 Token，返回 Token 字符串或 None"""
    token_path = _resolve_token_path(config)
    if not os.path.exists(token_path):
        return None
    try:
        with open(token_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Token 共享：只比对 host+port，不比对路径前缀
        saved_server = data.get('server_url', '')
        current_server = config.get('api_base_url', '')
        if _extract_host_port(saved_server) != _extract_host_port(current_server):
            return None
        return data.get('token')
    except (json.JSONDecodeError, KeyError):
        return None


def save_token(token, username, config):
    """保存 Token 到本地文件"""
    token_path = _resolve_token_path(config)
    token_dir = os.path.dirname(token_path)
    os.makedirs(token_dir, exist_ok=True)

    data = {
        "token": token,
        "username": username,
        "server_url": config.get('api_base_url', ''),
        "saved_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    }
    with open(token_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def delete_token(config):
    """删除本地 Token 文件"""
    token_path = _resolve_token_path(config)
    if os.path.exists(token_path):
        os.remove(token_path)
        return True
    return False


# ── 登录弹窗 ──────────────────────────────────────────────────

def _login_gui(config, message="Smartbi 登录"):
    """弹出登录窗口，用户输入用户名和密码后登录。返回是否登录成功。

    无 Tkinter 环境时自动回退返回 False。
    """
    try:
        import tkinter as tk
        from tkinter import ttk, messagebox
    except ImportError:
        return False

    result = {"success": False}

    def on_login(event=None):
        username = entry_user.get().strip()
        password = entry_pass.get().strip()
        if not username or not password:
            return

        btn_login.config(state="disabled", text="登录中...")
        root.update()

        url = _build_url(config, "/api/auth/login", 'query_prefix')
        timeout = config.get('timeout', 30)
        try:
            resp = requests.post(
                url,
                json={"username": username, "password": password},
                headers={"Content-Type": "application/json; charset=utf-8"},
                timeout=timeout,
            )
            resp.encoding = 'utf-8'
            data = resp.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("错误", f"连接服务器失败:\n{e}")
            btn_login.config(state="normal", text="登 录")
            return

        if data.get('success'):
            save_token(data['token'], data['username'], config)
            result["success"] = True
            root.destroy()
        else:
            messagebox.showerror("登录失败", data.get('message', 'AD域验证失败，请检查用户名和密码'))
            btn_login.config(state="normal", text="登 录")

    root = tk.Tk()
    root.title(message)
    root.geometry("360x220")
    root.resizable(False, False)

    # 居中显示
    root.update_idletasks()
    x = (root.winfo_screenwidth() - 360) // 2
    y = (root.winfo_screenheight() - 220) // 2
    root.geometry(f"+{x}+{y}")

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="AD域用户名:").grid(row=0, column=0, sticky="w", pady=(0, 8))
    entry_user = ttk.Entry(frame, width=25)
    entry_user.grid(row=0, column=1, pady=(0, 8))
    entry_user.focus()

    ttk.Label(frame, text="AD域密码:").grid(row=1, column=0, sticky="w", pady=(0, 8))
    entry_pass = ttk.Entry(frame, width=25, show="●")
    entry_pass.grid(row=1, column=1, pady=(0, 8))

    btn_login = ttk.Button(frame, text="登 录", command=on_login)
    btn_login.grid(row=2, column=0, columnspan=2, pady=(12, 0))

    root.bind('<Return>', on_login)

    # 关闭窗口视为取消
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()

    return result["success"]


# ── API 调用 ──────────────────────────────────────────────────

def get_auth_headers(config, auto_gui=True):
    """获取认证头，若本地无 Token 则弹出登录窗口"""
    token = load_token(config)
    if not token and auto_gui:
        if _login_gui(config, "Smartbi 登录 — 首次使用请登录"):
            token = load_token(config)
    if not token:
        print(json.dumps({
            "error": "未登录，请先执行: python smartbi_report.py login -u <用户名>"
        }, ensure_ascii=False))
        sys.exit(1)
    return {"Authorization": f"Bearer {token}"}


def _build_url(config, path, prefix_key='query_prefix'):
    """拼接完整 URL：api_base_url + prefix + path"""
    base = config.get('api_base_url', '')
    prefix = config.get(prefix_key, '')
    return f"{base}{prefix}{path}"


def api_request(config, method, path, params=None, json_data=None, _retry=True, prefix_key='query_prefix'):
    """发送带认证的 API 请求（GET/POST），401 时弹窗重试"""
    url = _build_url(config, path, prefix_key)
    headers = get_auth_headers(config)
    headers["Content-Type"] = "application/json; charset=utf-8"
    timeout = config.get('timeout', 30)

    try:
        if method.upper() == "GET":
            resp = requests.get(url, params=params, headers=headers, timeout=timeout)
        elif method.upper() == "POST":
            resp = requests.post(url, json=json_data, headers=headers, timeout=timeout)
        else:
            return {"error": f"不支持的请求方法: {method}"}

        # 401 认证失败 → 弹窗重新登录并重试一次
        if resp.status_code == 401:
            if _retry:
                try:
                    detail = resp.json().get('detail', '认证失败')
                except Exception:
                    detail = '认证失败'
                if _login_gui(config, f"Smartbi 重新登录 — {detail}"):
                    return api_request(config, method, path, params, json_data, _retry=False, prefix_key=prefix_key)
            print(json.dumps({
                "error": "认证失败，请重新登录"
            }, ensure_ascii=False))
            sys.exit(1)

        resp.encoding = 'utf-8'
        resp.raise_for_status()
        return resp.json()

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def api_post_raw(config, path, payload, _retry=True, prefix_key='export_prefix'):
    """POST 请求，返回原始 Response 对象（用于导出下载文件）"""
    url = _build_url(config, path, prefix_key)
    headers = get_auth_headers(config)
    headers["Content-Type"] = "application/json; charset=utf-8"
    timeout = config.get('export_timeout', 120)
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=timeout)

        # 401 认证失败 → 弹窗重新登录并重试一次
        if resp.status_code == 401:
            if _retry:
                try:
                    detail = resp.json().get('detail', '认证失败')
                except Exception:
                    detail = '认证失败'
                if _login_gui(config, f"Smartbi 重新登录 — {detail}"):
                    return api_post_raw(config, path, payload, _retry=False, prefix_key=prefix_key)
            print(json.dumps({
                "error": "认证失败，请重新登录"
            }, ensure_ascii=False))
            sys.exit(1)

        resp.raise_for_status()
        return resp
    except requests.exceptions.RequestException as e:
        return None


# ── 报表参数 ──────────────────────────────────────────────────

def get_parameters(config, report_id):
    """获取报表参数列表"""
    return api_request(config, "GET", f"/api/report/parameters/{report_id}", prefix_key='export_prefix')


def get_standby_values(config, report_id, param_id):
    """获取参数备选值"""
    return api_request(config, "GET", f"/api/report/parameters/{report_id}/{param_id}/standby-values", prefix_key='export_prefix')


def get_parameters_with_standby(config, report_id):
    """获取报表参数及备选值（合并）"""
    result = get_parameters(config, report_id)
    if 'error' in result:
        return result

    params = result.get('data', [])
    for param in params:
        sv_result = get_standby_values(config, report_id, param['id'])
        param['standbyValues'] = sv_result.get('data', []) if 'error' not in sv_result else []

    return {"code": 200, "data": params}


# ── 子命令: login ──────────────────────────────────────────────

def cmd_login(args):
    """AD 域登录，获取 Token"""
    config = load_config()
    username = args.username
    password = getpass.getpass("请输入AD域密码: ")

    if not password:
        print(json.dumps({"error": "密码不能为空"}, ensure_ascii=False))
        sys.exit(1)

    url = _build_url(config, "/api/auth/login", 'query_prefix')
    timeout = config.get('timeout', 30)
    try:
        resp = requests.post(
            url,
            json={"username": username, "password": password},
            headers={"Content-Type": "application/json; charset=utf-8"},
            timeout=timeout,
        )
        resp.encoding = 'utf-8'
        data = resp.json()
    except requests.exceptions.RequestException as e:
        print(json.dumps({"error": f"连接服务器失败: {e}"}, ensure_ascii=False))
        sys.exit(1)

    if data.get('success'):
        save_token(data['token'], data['username'], config)
        print(json.dumps({
            "success": True,
            "username": data['username'],
            "message": "登录成功，Token已保存"
        }, ensure_ascii=False, indent=2))
    else:
        print(json.dumps({
            "success": False,
            "message": data.get('message', '登录失败')
        }, ensure_ascii=False))
        sys.exit(1)


# ── 子命令: logout ─────────────────────────────────────────────

def cmd_logout(args):
    """登出，删除本地 Token"""
    config = load_config()
    if delete_token(config):
        print(json.dumps({"success": True, "message": "已登出，Token已删除"}, ensure_ascii=False))
    else:
        print(json.dumps({"success": True, "message": "当前未登录"}, ensure_ascii=False))


# ── 子命令: list (查询报表) ────────────────────────────────────

def cmd_list(args):
    """查询报表列表"""
    config = load_config()

    data = api_request(config, "GET", "/api/permissions")

    if 'error' in data:
        print(json.dumps({"error": data['error']}, ensure_ascii=False))
        sys.exit(1)

    user_alias = data.get('user_alias', 'unknown')
    search = args.search

    if search:
        keyword = search.lower()
        filtered = [
            r for r in data.get('data', [])
            if keyword in r['res_alias'].lower() or keyword in r['res_path'].lower()
        ]
        data['data'] = filtered
        data['total'] = len(filtered)

    # 如果指定了 --id，精确查找
    if args.id:
        matched = [r for r in data.get('data', []) if r['res_id'] == args.id]
        if matched:
            data['data'] = matched
            data['total'] = 1
        else:
            data['data'] = []
            data['total'] = 0

    # JSON输出模式
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    # 仅输出ID模式
    if args.id_only:
        for r in data.get('data', []):
            print(r['res_id'])
        return

    # 表格输出
    reports = data.get('data', [])
    total = data.get('total', 0)

    if args.limit:
        reports = reports[:args.limit]

    if not reports:
        print("未查询到报表")
        return

    print(f"查询到 {total} 个报表（用户: {user_alias}）：\n")
    print("| # | 报表名称 | 报表路径 | 报表ID |")
    print("|---|---------|---------|--------|")
    for i, r in enumerate(reports, 1):
        print(f"| {i} | {r['res_alias']} | {r['res_path']} | {r['res_id']} |")

    if args.limit and total > args.limit:
        print(f"\n... 还有 {total - args.limit} 个报表未显示，使用 --limit 增加显示数量或 --json 输出全部")


# ── 子命令: params ─────────────────────────────────────────────

def cmd_params(args):
    """查询报表参数（JSON输出，供AI解析）"""
    config = load_config()
    data = get_parameters_with_standby(config, args.report_id)

    if 'error' in data:
        print(json.dumps({"error": data['error']}, ensure_ascii=False))
        sys.exit(1)

    params = data.get('data', [])

    if not params:
        print(json.dumps({"has_params": False, "parameters": []}, ensure_ascii=False))
    else:
        output = {
            "has_params": True,
            "parameters": []
        }
        for p in params:
            item = {
                "paramId": p['id'],
                "name": p.get('name', ''),
                "alias": p.get('alias', ''),
                "dataType": p.get('dataType', 'STRING'),
                "defaultValue": p.get('value') or '',
                "standbyValues": [
                    {"displayValue": sv['name'], "realValue": sv['value']}
                    for sv in p.get('standbyValues', [])
                ]
            }
            output["parameters"].append(item)
        print(json.dumps(output, ensure_ascii=False, indent=2))


# ── 子命令: info ───────────────────────────────────────────────

def cmd_info(args):
    """查询报表参数（表格输出，供用户查看）"""
    config = load_config()
    data = get_parameters_with_standby(config, args.report_id)

    if 'error' in data:
        print(f"错误: {data['error']}", file=sys.stderr)
        sys.exit(1)

    params = data.get('data', [])

    if not params:
        print("该报表无需参数，可直接导出。")
        print(f"\n使用以下命令导出:")
        print(f'  python smartbi_report.py export -r "{args.report_id}"')
        return

    print("\n" + "=" * 80)
    print("报表参数列表")
    print("=" * 80 + "\n")

    for idx, p in enumerate(params, 1):
        default = p.get('value') or '-'
        standby = p.get('standbyValues', [])

        print(f"参数 {idx}: {p.get('alias', '')} ({p.get('name', '')})")
        print(f"  参数ID: {p['id']}")
        print(f"  数据类型: {p.get('dataType', 'STRING')}")
        print(f"  默认值: {default}")

        if standby:
            print("  备选值:")
            for i, sv in enumerate(standby, 1):
                print(f"    {i}. {sv['name']} (值: {sv['value']})")
        else:
            print("  备选值: 无")
        print()

    print("=" * 80)

    # 生成导出命令示例
    param_parts = []
    for p in params:
        default = p.get('value') or ''
        param_parts.append(f'{{"paramId":"{p["id"]}","realValue":"{default}","displayValue":"{default}"}}')

    print(f"\n导出命令示例:")
    print(f'  python smartbi_report.py export -r "{args.report_id}" -p \'[{",".join(param_parts)}]\'')


# ── 子命令: export ─────────────────────────────────────────────

def cmd_export(args):
    """导出报表（非交互模式）"""
    config = load_config()

    report_id = args.report_id
    export_type = args.type or config.get('default_export_type', 'EXCEL2007')

    # 验证报表是否在用户可查看范围内，同时获取报表名称（用于文件命名）
    report_name = ""
    try:
        perm_data = api_request(config, "GET", "/api/permissions", prefix_key='query_prefix')
        if 'error' not in perm_data:
            matched = [r for r in perm_data.get('data', []) if r['res_id'] == report_id]
            if matched:
                report_name = matched[0].get('res_alias', '')
            else:
                print(json.dumps({
                    "error": f"报表 {report_id} 不在您可查看的范围内，无法导出"
                }, ensure_ascii=False))
                sys.exit(1)
        else:
            print(json.dumps({"error": f"无法验证报表权限: {perm_data.get('error', '未知错误')}"}, ensure_ascii=False))
            sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"验证报表权限失败: {e}"}, ensure_ascii=False))
        sys.exit(1)

    # 解析参数
    parameters = []
    if args.params:
        try:
            parameters = json.loads(args.params)
        except json.JSONDecodeError as e:
            print(json.dumps({"error": f"参数JSON解析失败: {e}"}, ensure_ascii=False))
            sys.exit(1)

    # 如果没有提供参数且不是跳过，自动查询参数并使用默认值
    if not args.params and not args.skip_params:
        param_data = get_parameters(config, report_id)
        if 'error' not in param_data:
            params_list = param_data.get('data', [])
            if params_list:
                for p in params_list:
                    default = p.get('value') or ''
                    parameters.append({
                        "paramId": p['id'],
                        "realValue": default,
                        "displayValue": default
                    })

    # 调用导出API
    payload = {
        "reportId": report_id,
        "exportType": export_type,
        "parameters": parameters
    }

    response = api_post_raw(config, "/api/report/export", payload)

    if response is None:
        print(json.dumps({"error": "导出API调用失败"}, ensure_ascii=False))
        sys.exit(1)

    # 检查是否返回了错误信息（JSON而非文件）
    content_type = response.headers.get('content-type', '')
    if 'application/json' in content_type:
        try:
            err_data = response.json()
            print(json.dumps({"error": err_data.get('message', err_data.get('detail', '导出失败'))}, ensure_ascii=False))
            sys.exit(1)
        except Exception:
            pass

    # 确定输出文件路径
    extension_map = {
        'PDF': 'pdf', 'PNG': 'png', 'WORD': 'docx',
        'EXCEL2007': 'xlsx', 'EXCEL': 'xlsx', 'LIST_EXCEL': 'xlsx',
        'HTML': 'html', 'CSV': 'csv'
    }
    ext = extension_map.get(export_type.upper(), 'xlsx')

    output_file = args.output
    if not output_file:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        # 清理报表名称中不适合做文件名的字符
        import re
        safe_name = re.sub(r'[\\/:*?"<>|]', '_', report_name) if report_name else "report"
        # 去除首尾空白和点号
        safe_name = safe_name.strip(' .')
        if not safe_name:
            safe_name = "report"
        filename = f"{safe_name}_{timestamp}.{ext}"
        # 默认导出到用户桌面
        desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
        if not os.path.isdir(desktop_dir):
            os.makedirs(desktop_dir, exist_ok=True)
        output_file = os.path.join(desktop_dir, filename)

    with open(output_file, 'wb') as f:
        f.write(response.content)

    # JSON输出结果（供AI解析）
    abs_path = os.path.abspath(output_file)
    result = {
        "success": True,
        "report_id": report_id,
        "report_name": report_name or None,
        "export_type": export_type,
        "file_path": abs_path,
        "file_size": len(response.content),
        "parameters_used": parameters,
        "message": "文件已导出到桌面" if not args.output else None
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


# ── 主入口 ──────────────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Smartbi报表查询与导出CLI（需AD域登录）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
子命令:
  login      AD域登录，获取Token
  logout     登出，删除本地Token
  list       查询/搜索报表列表
  params     查询报表参数及备选值（JSON输出，供AI解析）
  info       查询报表参数（表格输出，供用户查看）
  export     导出报表文件

示例:
  # AD域登录
  python smartbi_report.py login -u zhangsan

  # 登出
  python smartbi_report.py logout

  # 查询当前用户所有报表
  python smartbi_report.py list --json

  # 搜索包含"产品"的报表
  python smartbi_report.py list -s "产品" --json

  # 按报表ID精确查询
  python smartbi_report.py list --id "I8a8a86..." --json

  # 仅输出报表ID
  python smartbi_report.py list -s "产品" --id-only

  # 查询报表参数(JSON格式，供AI使用)
  python smartbi_report.py params -r "I8a8a86..."

  # 查看报表参数(表格格式，供人阅读)
  python smartbi_report.py info -r "I8a8a86..."

  # 无参数报表直接导出
  python smartbi_report.py export -r "I8a8a86..."

  # 带参数导出Excel
  python smartbi_report.py export -r "I8a8a86..." -t EXCEL2007 -p '[{"paramId":"date","realValue":"2024-01-01","displayValue":"2024-01-01"}]'

  # 导出PDF到指定路径
  python smartbi_report.py export -r "I8a8a86..." -t PDF -o "D:/reports/report.pdf"

注意: 首次使用需通过 login 命令登录AD域，Token将保存到 ~/.smartbi/token.json
        """)

    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # ── login 子命令
    p_login = subparsers.add_parser('login', help='AD域登录，获取Token')
    p_login.add_argument('-u', '--username', required=True, help='AD域用户名')

    # ── logout 子命令
    p_logout = subparsers.add_parser('logout', help='登出，删除本地Token')

    # ── list 子命令
    p_list = subparsers.add_parser('list', help='查询/搜索报表列表')
    p_list.add_argument('-s', '--search', help='搜索关键词（模糊匹配报表名称或路径）')
    p_list.add_argument('--id', help='按报表ID精确查询')
    p_list.add_argument('-l', '--limit', type=int, help='显示数量限制')
    p_list.add_argument('--json', action='store_true', help='JSON格式输出（供程序解析）')
    p_list.add_argument('--id-only', action='store_true', help='仅输出报表ID（每行一个）')

    # ── params 子命令
    p_params = subparsers.add_parser('params', help='查询报表参数（JSON输出）')
    p_params.add_argument('-r', '--report-id', required=True, help='报表ID')

    # ── info 子命令
    p_info = subparsers.add_parser('info', help='查询报表参数（表格输出）')
    p_info.add_argument('-r', '--report-id', required=True, help='报表ID')

    # ── export 子命令
    p_export = subparsers.add_parser('export', help='导出报表')
    p_export.add_argument('-r', '--report-id', required=True, help='报表ID')
    p_export.add_argument('-t', '--type', default=None,
                          choices=['EXCEL2007', 'PDF', 'PNG', 'WORD', 'HTML', 'CSV'],
                          help='导出类型 (默认: EXCEL2007)')
    p_export.add_argument('-p', '--params', default=None,
                          help='参数JSON字符串，如: \'[{"paramId":"date","realValue":"2024-01-01","displayValue":"2024-01-01"}]\'')
    p_export.add_argument('-o', '--output', default=None, help='输出文件路径')
    p_export.add_argument('--skip-params', action='store_true',
                          help='跳过参数查询，不传任何参数（用于无参数报表）')

    args = parser.parse_args()

    if args.command == 'login':
        cmd_login(args)
    elif args.command == 'logout':
        cmd_logout(args)
    elif args.command == 'list':
        cmd_list(args)
    elif args.command == 'params':
        cmd_params(args)
    elif args.command == 'info':
        cmd_info(args)
    elif args.command == 'export':
        cmd_export(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
