# Wind基金知识库 - 摘要

> 包含表基本信息 + 业务主键字段，覆盖90%查询场景。

---

## Wind兼容代码

- **英文表名**: `WindCustomCode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录Wind定义的唯一标识证券的代码
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 国家及地区代码表

- **英文表名**: `Countryandareacode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录国家及地区标准名称和ISO编码
- **业务主键**: `NAME` (国家及地区名称)

## 货币代码表

- **英文表名**: `Currencycode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录各类货币的国际标准三位代码
- **业务主键**: `CRNCY_NAME` (货币名称), `LATEST_LOGO` (最新标志)

## 指数板块对照

- **英文表名**: `IndexContrastSector`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录指数对应成份板块
- **业务主键**: `S_INFO_INDEXCODE` (指数万得代码), `S_INFO_INDUSTRYCODE` (板块代码)

## 公司机构代码表

- **英文表名**: `CompOrganizationcode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录公司的组织机构代码、统一社会代码信息
- **业务主键**: `COMP_ID` (公司ID), `TYPE_CODE` (业务类型代码), `S_CODE` (业务代码)

## 行业代码

- **英文表名**: `AShareIndustriesCode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录板块列表，包括证监会行业分类、上交所行业分类、地域板块、概念板块、同系公司5套体系近千个板块
- **业务主键**: `INDUSTRIESCODE` (行业代码), `INDUSTRIESNAME` (行业名称)

## 类型编码表

- **英文表名**: `AShareTypeCode`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录类型字段数值、名称间的映射关系
- **业务主键**: `OBJECT_ID` (对象ID)

## Wind代码变更表

- **英文表名**: `ChangeWindcode`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录证券代码变更的情况
- **业务主键**: `OBJECT_ID` (对象ID)

## 业务代码及简称

- **英文表名**: `CodeAndSName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金前后端代码，配股代码，跨市场债券等信息，不保留历史信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (业务类型代码), `S_CODE` (业务代码)

## 证券关系表

- **英文表名**: `RalatedSecuritiesCode`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录证券和证券之间的关系
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_RALATEDCODE` (关联证券Wind代码), `S_RELATION_TYPCODE` (关系类型代码), `S_INFO_EFFECTIVE_DT` (生效日期)

## 公司简介

- **英文表名**: `CompIntroduction`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录各种类型公司的基础信息。除上市公司外，还包括各类市场主体，如：债券发行人、大股东、关联方、交易方、中介机构、券商、银行、保险公司、投资机构等，用于和业务表关联使用。
- **业务主键**: `COMP_ID` (公司ID)

## 全球市场交易时间

- **英文表名**: `GlobalMarketTradingTime`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录全球市场的交易时间
- **业务主键**: `EXCHANGE_SNAME_ENG` (交易所英文简称), `SECURITIES_TYPE` (交易品种描述), `TRADING_HOURS_CODE` (交易时段编码), `TRADING_HOURS` (交易时段)

## 全球工作日安排

- **英文表名**: `GlobalWorkingDay`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录全球各国工作日信息
- **业务主键**: `WORKING_DATE` (日期), `COUNTRY_CODE` (国家或地区代码)

## 公司曾用名

- **英文表名**: `CompanyPreviousNames`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录公司历次更名的数据，包括变动日期、更名原因等信息。
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `CHANGE_DT` (变动日期)

## 沪深市场总体指标(月)

- **英文表名**: `AShareMarketOverallindex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深交易所每月各项总体指标值及变动幅度
- **业务主键**: `MONTH1` (月份), `EXCHANGE` (交易所)

## IPO初步询价明细

- **英文表名**: `IPOInquiryDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股IPO询价对象、配售对象、申报价格、配售数量等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `INQUIRER` (询价对象名称), `ISSUETARGET` (配售对象名称), `DEDAREDPRICE` (申报价格(元/股))

## IPO审核申报企业情况

- **英文表名**: `IPOCompRFA`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股IPO申报预计发行股数、募集资金额度、中介机构等信息
- **业务主键**: `S_INFO_COMPANYID` (公司ID), `SCH_CODE` (进度类型代码), `ST_DATE` (状态起始日期)

## IPO申报预披露日

- **英文表名**: `IPODeclareDisclosureDate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股IPO起始申报披露日
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `PER_DISCLOSUREDATE` (纳入日期)

## 发审委员基本资料

- **英文表名**: `IECMemberList`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股申请IPO时发审委相关委员的个人信息
- **业务主键**: `TERM` (发审委届次), `ANN_DT` (公告日期), `NAME` (姓名), `GENDER` (性别), `POST` (职务), `TYPECODE` (委员会类型代码), `VALID_DT` (有效截止日期)

## 非公开发行股票审核申报企业情况

- **英文表名**: `NOPUBLICSTOCKCompRFA`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非公开发行股票审核申报企业数据，包括保荐机构、申请事项、进度等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SCH_CODE` (进度类型代码), `ST_DATE` (状态起始日期)

## 中国券商月报

- **英文表名**: `AShareMonthlyReportsofBrokers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录证券公司月度披露的营业收入、净利润、股权权益等数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPECODE` (报表类型代码)

## 银行业存款结构

- **英文表名**: `CBankDepositStructure`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行类公司的存款结构，如存款平均余额、存款利息支出等
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码), `CRNCY_TYPE_CODE` (币种类型代码), `LOAN_TYPE_CODE` (项目类别代码), `DEPOSIT_ITEM_CODE` (存款项目代码)

## 银行业贷款结构

- **英文表名**: `CBankLoanStructure`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行类公司的贷款结构，如贷款利息收入、不良贷款余额等
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码), `CRNCY_TYPE_CODE` (币种类型代码), `LOAN_TYPE_CODE` (项目类别代码), `LOAN_ITEM_CODE` (贷款项目代码)

## 银行五级分类贷款明细

- **英文表名**: `BankLoan5LClassification`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行类公司的五级分类贷款明细
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `LOAN_TYPE` (贷款类型)

## 财务附注项目类别配置表

- **英文表名**: `FinancialNoteCategory`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录财务附注辅助表中的项目类别
- **业务主键**: `S_SEGMENT_ITEMCODE` (项目类别代码)

## 主营及附注科目对应关系表

- **英文表名**: `AShareSalesSegmentMapping`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国A股主营及附注科目对应关系信息，包括主科目名称、子科目名称等。
- **业务主键**: `MAIN_ACCOUNTS_ID` (主科目ID), `SUB_ACCOUNTS_ID` (子科目ID)

## 深股通/QFII/RQFII投资者信息

- **英文表名**: `SZSCQFIIRQFIIInvestorInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录深股通/QFII/RQFII投资者信息，包括证券ID、境外投资者持股数量、境外投资者持股占比等。
- **业务主键**: `SEC_ID` (证券id), `TRADE_DT` (日期)

## 中国ETF申购赎回清单

- **英文表名**: `ChinaETFPchRedmList`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录ETF申购赎回基本信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国ETF申购赎回成份

- **英文表名**: `ChinaETFPchRedmMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录ETF申购赎回销成份股信息
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码), `TRADE_DT` (交易日期), `S_CON_WINDCODE` (成份股Wind代码)

## 中证800指数权重

- **英文表名**: `AIndexCSI800Weight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中证800指数成份股的权重信息
- **业务主键**: `TRADE_DT` (生效日期), `S_INFO_WINDCODE` (Wind代码), `S_CON_WINDCODE` (标的Wind代码)

## 中证1000指数权重

- **英文表名**: `AIndexCSI1000Weight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中证1000指数成份股的权重信息
- **业务主键**: `TRADE_DT` (生效日期), `S_INFO_WINDCODE` (Wind代码), `S_CON_WINDCODE` (Wind代码)

## 中信标普指数成份

- **英文表名**: `ASPCITICIndexWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中信标普指数的成份股明细数据
- **业务主键**: `F_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份Wind代码), `TRADE_DT` (日期)

## 中信标普指数行情

- **英文表名**: `ASPCITICIndexEOD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中信标普指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `TRADE_DT` (交易日期)

## 中信标普GICS行业分类(废弃)

- **英文表名**: `AShareGICSIndustriesClass`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中信标普300成份股4级行业及中标综指GICS2级行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `GICS_IND_CODE` (GICS行业代码), `ENTRY_DT` (纳入日期)

## 申万行业分类

- **英文表名**: `AShareSWIndustriesClass`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股申万行业分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SW_IND_CODE` (申万行业代码), `ENTRY_DT` (纳入日期)

## FileSync转档时间

- **英文表名**: `FileSyncTimeSchedule`
- **更新频率**: week
- **全量产品**: 是
- **说明**: 记录FileSync产品的转档时间

## Wind一致预测个股滚动指标

- **英文表名**: `AShareConsensusRollingData`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股个股一致预测滚动指标，每日滚动生成
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EST_DT` (日期), `ROLLING_TYPE` (类型)

## Wind一致预测指数滚动指标

- **英文表名**: `AIndexConsensusRollingData`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股指数一致预测滚动指标，每日滚动生成
- **业务主键**: `S_INFO_WINDCODE` (证券ID), `EST_DT` (日期), `ROLLING_TYPE` (类型)

## 中国债券基本资料

- **英文表名**: `CBondDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录固定收益类证券(不含央行票据)的基本资料(票面利率、发行量、发行人、付息方式、相关日期等数据)
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国债券中介机构

- **英文表名**: `CBondAgency`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券发行时的中介机构信息
- **业务主键**: `B_INFO_WINDCODE` (Wind代码), `B_RELATION_TYPCODE` (关系类型代码), `B_AGENCY_NAMEID` (机构名称ID)

## 中国债券Wind分类板块

- **英文表名**: `CBondIndustryWind`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券的Wind债券分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国债券Wind概念板块

- **英文表名**: `CBondPlateWind`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券的Wind概念板块信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_INDUSTRYCODE` (板块代码)

## 中国债券证监会行业分类

- **英文表名**: `CBondSECIndustriesClass`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券新版证监会行业分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SEC_IND_CODE` (所属板块代码), `ENTRY_DT` (纳入日期)

## 中国债券证监会行业分类(旧)

- **英文表名**: `CBondOldSECIndustriesClass`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券旧版证监会行业分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SEC_IND_CODE` (证监会行业代码), `ENTRY_DT` (纳入日期)

## 中国债券质押券代码

- **英文表名**: `PledgeCode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券的质押券代码信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (业务类型代码), `PLEDGE_CODE` (质押券代码)

## 中国债券特殊条款

- **英文表名**: `CBondSpecialConditions`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券回售、赎回、延期等特殊条款信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_INFO_PROVISIONTYPE` (条款类型), `B_INFO_CALLBKORPUTBKDATE` (赎回/回售日期)

## 中国债券可转债回售赎回条款

- **英文表名**: `CBondConvertiblePACTerms`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录可转债回售、赎回条款信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国债券市场承销团成员明细

- **英文表名**: `CBondUnderwritingmember`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行间债券市场各类承销团（国债承销团、国家开发银行金融债承销团、中国进出口银行金融债承销团、凭证式国债承销团）的成员名单和类型。
- **业务主键**: `MEMBER_NAME` (成员名称), `UNDERWRITING_GROUP_TYPE` (承销团类型), `B_YEAR` (年度)

## 中国债券赎回条款执行说明

- **英文表名**: `CBondCall`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券赎回条款执行说明，如赎回日、赎回代码、赎回价格等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_INFO_REDEMPTIONDATE` (赎回日)

## 中国债券回售条款执行说明

- **英文表名**: `CBondPut`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券回售条款执行说明，如回售日、回售代码、回售价格等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_INFO_REPURCHASEDATE` (回售资金到帐日), `B_INFO_REPURCHASESTARTDATE` (回售行使开始日)

## 中国债券浮息债基础利率属性

- **英文表名**: `CBondFloatingRate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录浮动利率债券的特有属性，如基准利率、利率精度、首个定价日等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国可转债有条件回售价格和触发比例

- **英文表名**: `CCBondRepurchasePriceRate`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录可转债有条件回售的价格和触发比例信息
- **业务主键**: `B_INFO_WINDCODE` (Wind代码), `B_INFO_BGNDT` (起始日期)

## 中国可转债有条件赎回价格和触发比例

- **英文表名**: `CCBondRedemptionPriceRate`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录可转债有条件赎回的价格和触发比例信息
- **业务主键**: `B_INFO_WINDCODE` (Wind代码), `B_INFO_BGNDT` (起始日期)

## 中国债券国债预发行资料

- **英文表名**: `CBondPreRelease`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录国债预发行的信息，如预发行代码、交易日等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国债券抵押品信息

- **英文表名**: `CBondCollateralinformation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券的抵押品信息
- **业务主键**: `S_INFO_WINDCODE` (wind代码), `B_AGENCY_GRNTTYPECODE` (担保方式代码), `B_AGENCY_COLLATERALTYPECODE` (担保物类型代码), `EQY_TARGETCOMP` (股权标的)

## 中国债券利率品种简介条款

- **英文表名**: `InterestrateIntroduction`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券利率品种的简介条款
- **业务主键**: `B_INFO_WINDCODE` (品种ID), `START_DT` (起始日期)

## 中国债券信用风险缓释工具基本资料

- **英文表名**: `CRMWDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录CRMW、CLN等信用风险缓释工具的基本资料
- **业务主键**: `B_INFO_WINDCODE` (Wind代码)

## 中国可转债发行

- **英文表名**: `CCBondIssuance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录可转债的基本资料和发行情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CB_INFO_PREPLANDATE` (预案公告日), `CB_INFO_LISTDATE` (方案进度), `S_INFO_COMPCODE` (转股公司ID), `SEC_ID` (证券ID)

## 中国债券发行涉及银行账号

- **英文表名**: `AccountRelatedWithBondIssue`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券发行时涉及的银行账号信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (发行类型代码), `ACCOUNT_NUM` (账号), `BANK_NUM` (清算行行号)

## 中国债券调换条款执行说明

- **英文表名**: `CBondChangeclause`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券可调换条款的执行说明，如行权日期、调换比例等
- **业务主键**: `S_INFO_WINDCODE` (证券ID), `S_INFO_WINDCODE2` (目标证券ID), `S_INFO_EXECDATE` (行权日期)

## 中国债券曾用名

- **英文表名**: `CBondPreviousName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券的曾用名信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `BEGINDATE` (起始日期)

## 中国债券板块代码

- **英文表名**: `CBondIndustriesCode`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券板块代码和名称的映射关系
- **业务主键**: `INDUSTRIESCODE` (板块代码)

## 中国债券国民经济行业分类

- **英文表名**: `CBondNEIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券国民经济行业分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `NE_IND_CODE` (国民经济行业代码), `ENTRY_DT` (纳入日期)

## 中资美元债基本资料

- **英文表名**: `CNUSDBonddesc`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中资企业发行的美元债信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国Wind债券分类板块(新)

- **英文表名**: `CBondNIndustryWind`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券的Wind债券分类信息，包括分类的历史变动数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ENTRY_DT` (纳入日期)

## 中国债券债券行情(沪深交易所)

- **英文表名**: `CBondEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深交易所债券的行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国债券大宗交易

- **英文表名**: `CBondBlockTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深交易所每天进行大宗交易的债券交易信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `S_BLOCK_BUYERNAME` (买方营业部), `S_BLOCK_SELLERNAME` (卖方营业部)

## 中国债券停复牌信息

- **英文表名**: `CBondTradingSuspension`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券停牌、复牌信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_DQ_SUSPENDDATE` (停牌日期)

## 中国债券交易日历

- **英文表名**: `CBondCalendar`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券市场的交易日信息
- **业务主键**: `TRADE_DAYS` (交易日), `S_INFO_EXCHMARKET` (交易所英文简称)

## 中国债券关键年期久期

- **英文表名**: `BondKeyTermDuration`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券关键年期久期信息
- **业务主键**: `S_INFO_WINDCODE` (债券Wind代码), `TRADE_DT` (交易日期)

## 中国债券行情-全价

- **英文表名**: `CBondPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券的全价行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国债券行情-净价

- **英文表名**: `CBondPricesNet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券的净价行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国债券衍生指标

- **英文表名**: `CBondValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券(不包括可转债)风险收益率指标
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国含权债行权衍生指标

- **英文表名**: `COptionEmbeddedBondValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录含权债的行权衍生数据，如行权收益率、行权剩余期限、行权久期等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期), `PRICE_TYPE_CODE` (价格类型代码)

## 中国债券同业拆借日行情

- **英文表名**: `CBondRepoAndIBLEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券市场债券回购、同业拆借的行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 银行间本币货币市场日行情

- **英文表名**: `CBondIBRMBMonDMarQuotation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行间本币市场同业拆借各期限品种成交情况和债券回购行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国债券远期交易行情(银行间)

- **英文表名**: `CBondForwardMarketN`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国银行间债券远期交易的行情数据，包括远期期限品种、前收盘净价、开盘净价、收盘净价及涨跌幅等信息。
- **业务主键**: `TRADE_DT` (日期), `WINDCODE` (Wind代码), `TERM_VARIETY` (远期期限品种)

## 中国债券招标

- **英文表名**: `CBondTender`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券招投标发行的信息，如招标日、招标方式、招标对象等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_TENDER_OBJECT` (招标标的)

## 中国债券招标结果

- **英文表名**: `CBondTenderResult`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券招投标的结果信息，如投标家数、投标笔数、中标总量等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_TENDER_OBJECT` (招标标的), `B_TENDRST_DOCUMTNUMBER` (招标书编号)

## 中国债券份额变动

- **英文表名**: `CBondAmount`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券的份额和变动原因
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_ENDDATE` (截止日期)

## 中国可转债转股价格变动

- **英文表名**: `CBondConvPrice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录可转债转股价格历次变动情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_ENDDATE` (变动日期)

## 中国可转债转股

- **英文表名**: `CCBondConversion`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录可转债转股的转换条件和转换情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国债券事件日期信息

- **英文表名**: `CBONDEventdateinformation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券事件发生信息，如发生日期、事件类型等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EVENT_TYPE` (事件类型编号), `OCCURRENCE_DATE` (发生日期), `S_INFO_CODE` (交易代码), `LANGUAGE1` (语言), `SRC_OBJID` (业务ID)

## 中国债券付息和兑付

- **英文表名**: `CBondPayment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录附息债券历次付息记录
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_INFO_ANNOUNCEMENTDATE` (公告日期), `B_INFO_PAYMENTDATE` (付息日)

## 中国债券票面利率调整幅度

- **英文表名**: `CBondrateadjustment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券票面利率调整幅度数据和后期变动情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_INFO_ENDDATE` (截止日期)

## 中国可转换债券份额变动

- **英文表名**: `CCBondAmount`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录可转债的份额和变动原因
- **业务主键**: `S_INFO_CHANGEDATE` (变动日期), `S_INFO_WINDCODE` (Wind代码)

## 中国可转债修正条款

- **英文表名**: `CCBondConversionreset`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录可转债的股价修正条件
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `START_DT` (特别修正起始时间), `CORRECTIONTYPE_CODE` (修正方向类型代码)

## 中国浮息债票面利率变动

- **英文表名**: `FloatingCouponsRate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录浮息债历次利率调整情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期)

## 中国含权债票面利率变动

- **英文表名**: `OptionEmbeddedBondRate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录累计利率债券的利率变动情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `START_DT` (起始日期)

## 中国可转债衍生指标

- **英文表名**: `CCBondValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录可转债的衍生数据，如应急利息、剩余期限、纯债价值、转股价值等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国债券应计利息

- **英文表名**: `CBondAccruedInterest`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券当天的应计利息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国债券本金提前偿还明细

- **英文表名**: `CBondERepayPrincipal`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券本金提前偿还明细
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_INFO_REPAYPRIDT` (本金偿还日期)

## 中国债券发行主承销商承销金额

- **英文表名**: `CBondLeadUnderwriter`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录可转债发行、债券发行的主承销商承销数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_LU_ISSUEDATE` (发行日期), `S_LU_ISSUETYPE` (发行类型), `S_LU_NAME` (主承销商名称)

## 中国债券违约兑付表

- **英文表名**: `CBondDefaultPayment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录违约债券实际兑付的情况
- **业务主键**: `B_INFO_WINDCODE` (Wind代码), `B_ACTUAL_PAYMENT` (实际兑付日)

## 中国债券持有人大会通知

- **英文表名**: `CBondholdersmeeting`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录股东大会的召开时间及审议事项
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期), `MEETING_DT` (会议日期), `MEETING_TYPE` (会议类型)

## 中国债券配售机构获配明细

- **英文表名**: `CBondPlacementDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录战略投资者和A类机构投资者在债券发行中获配数量
- **业务主键**: `S_INFO_WINDCODE` (证券ID), `LOCKMONTH` (冻结期限(月)), `TRADE_DT` (配售截止日期), `ANNOUNCE_INVESTOR_NAME` (公布获配公司名称)

## 中国债券违约报表

- **英文表名**: `CBondDefaultReportform`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录在国内公开市场发行交易的债券违约及违约相关事件详细信息表
- **业务主键**: `B_INFO_WINDCODE` (Wind代码), `B_DEFAULT_DATE` (违约发生日)

## 中国债券募集资金用途

- **英文表名**: `CBondFundUsing`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债主体募集资金的具体用途
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `START_DT` (起始日期)

## 中国债券持有人

- **英文表名**: `CBondHolder`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录可转债、公司债的前十大持有人
- **业务主键**: `OBJECT_ID` (对象ID)

## 中国债券现金流

- **英文表名**: `CBondCF`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券现金流信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_INFO_PAYMENTDATE` (现金流发放日)

## 中国债券实际现金流发生表

- **英文表名**: `CBondActualCF`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券实际发生的现金流
- **业务主键**: `B_INFO_WINDCODE` (Wind代码), `B_INFO_PAYMENTDATE` (现金流发生日)

## 中国债券发行主体信用评级

- **英文表名**: `CBondIssuerRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录评级机构对发债公司的信用评级
- **业务主键**: `ANN_DT` (评级日期), `B_RATE_STYLE` (评级类型), `B_INFO_CREDITRATINGAGENCY` (评级机构代码), `S_INFO_COMPCODE` (债券主体公司id)

## 中国债券评级定价估值(银行间)

- **英文表名**: `CBondPricingValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国银行间市场交易商协会公布的债券定价估值数据
- **业务主键**: `TRADE_DT` (日期), `VAL_AGENCY` (估值机构), `CREDIT_CODE` (信用评级代码), `TERM` (期限)

## 中国债券信用评级

- **英文表名**: `CBondRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录评级机构对债券的信用评级
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (评级日期), `B_RATE_STYLE` (评级类型), `B_INFO_CREDITRATINGAGENCY` (评级机构代码)

## 中国债券信用评估机构名单

- **英文表名**: `CBondRatingdefinition`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录信用评级机构代码(自定义)及名称
- **业务主键**: `B_INFO_CREDITRATINGAGENCY` (评估机构代码), `S_INFO_COMPCODE` (公司ID)

## 中国债券评级机构客户名单

- **英文表名**: `ClientOfCreditratingAgency`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录评级机构新承做信用评级企业名单
- **业务主键**: `S_INFO_COMPCODE` (评级机构ID), `CLIENT_COMPCODE` (公司(客户)ID), `ANN_DT` (公告日期)

## 中国债券主体信用评级观察名单明细

- **英文表名**: `CBondIssuerRatingWatchlist`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券主体评级被列入评级观察名单的信息
- **业务主键**: `B_SUBJECT_ID` (公司ID), `ANN_DT` (公告日期), `B_EVENT_CATEGORYCODE` (事件类型代码)

## 中国债券信用评级观察名单明细

- **英文表名**: `CBondRatingWatchlist`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券评级被列入评级观察名单的信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期), `B_EVENT_CATEGORYCODE` (事件类型代码)

## 中国债券信用等级定义

- **英文表名**: `CreditRatingDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录评级机构对信用等级的分类及定义
- **业务主键**: `B_EST_RATING_INST` (信用等级), `B_EST_INSTITUTE` (评估机构代码), `B_TYPCODE` (评级类型)

## 中国债券短融投资评级(中金)

- **英文表名**: `CBondRatingCICC`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录机构对短期融资券给予的投资评级
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (评级日期), `B_INFO_RATINGAGENCY` (机构)

## 中国债券负面事件

- **英文表名**: `CBondNegativeCreditEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券、发债主体相关负面事件信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ACU_DATE` ([内部]发生日期), `EVENT_TYPE` (事件类型), `S_INFO_COMPCODE` (公司ID), `EVENT_ID` (事件ID)

## 中国债券特别处理

- **英文表名**: `CBondST`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券被特别处理的实施和撤销、暂停/恢复上市，以及退市记录及原因
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_TYPE_ST` (特别处理类型代码), `ENTRY_DT` (实施日期)

## 中国债券重大事件汇总

- **英文表名**: `CBondMajorEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券和对应发债公司的重大事件信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_EVENT_CATEGORYCODE` (事件类型代码), `S_EVENT_HAPDATE` (发生日期), `S_EVENT_EXPDATE` (失效日期), `SEC_ID` (证券ID)

## 中国债券发行主体管理层成员

- **英文表名**: `CbondIssuerManagement`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司董、监、高成员的个人简历信息
- **业务主键**: `S_INFO_COMPCODE` (公司id), `S_INFO_MANAGER_NAME` (姓名), `S_INFO_MANAGER_STARTDATE` (任职日期), `S_INFO_MANAGER_POST` (公布职务名称)

## 中国债券发行主体担保数据(明细)

- **英文表名**: `CbondGuaranteeDetail`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司对外担保明细数据
- **业务主键**: `S_INFO_COMPCODE` (公司id), `ENDDATE` (截止日期), `COMPANY_GUARANTEED` (被担保公司名称), `GUARANTEECOMPANYTYPE` (担保公司类别), `CRNCY_CODE` (货币代码)

## 中国债券发行主体银行授信额度

- **英文表名**: `CompanyLineofCredit`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司获得的银行/商业信用明细
- **业务主键**: `COMP_ID` (公司id), `END_DT` (截止日期), `CREDIT_COMPNAME` (授信机构名称), `CRNCY_CODE` (货币代码)

## 中国债券发行主体担保数据(合计)

- **英文表名**: `CbondGuaranteeTotal`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司对外担保合计数据
- **业务主键**: `S_INFO_COMPCODE` (公司id), `ENDDATE` (截止日期)

## 中国债券发行主体管理层持股及报酬

- **英文表名**: `CBondManagementHoldReward`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司管理层持股和其薪酬信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `END_DATE` (截止日期), `S_INFO_MANAGER_NAME` (姓名), `S_INFO_MANAGER_POST` (职务)

## 中国债券发行主体

- **英文表名**: `CBondIssuer`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券、发债主体之间的关系
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_COMPCODE` (债券主体公司id), `USED` (是否有效), `S_INFO_TYPECODE` (关系类型代码)

## 中国债券发行主体公司曾用名

- **英文表名**: `CBondCompanyPreviousName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司历次变更信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `CHANGE_DT` (变动日期)

## 中国债券发行主体前十大股东

- **英文表名**: `CBondInsideHolder`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司的前十大股东持股信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `B_HOLDER_ENDDATE` (截止日期), `B_HOLDER_NAME` (股东名称), `B_HOLDER_QUANTITY` (持股数量), `B_HOLDER_ANAME` (股东名称)

## 中国债券发行主体实际控制人

- **英文表名**: `CBondEquityRelationships`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司的股权关系、实际控制人信息
- **业务主键**: `COMPCODE` (公司ID), `ENDDATE` (截止日期), `S_INFO_COMPNAME` (公司名称), `S_HOLDER_NAME` (股东名称)

## 中国债券发行主体控股参股

- **英文表名**: `CBondCompanyHoldShares`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司的控股参股信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ENDDATE` (截止日期), `S_CAPITALOPERATION_COMPANYNAME` (被参控公司名称)

## 中国债券主体国内办公城市(海外)

- **英文表名**: `CBondIssuerOfficeCity`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债主体为海外公司其在内地的办公地址
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `WIND_IND_CODE` (所属板块代码), `CUR_SIGN` (最新标志)

## 中国债券主体地域板块

- **英文表名**: `CBondRegional`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司的地域信息
- **业务主键**: `S_INFO_COMPCODE` (公司id), `WIND_SEC_CODE` (板块代码), `ENTRY_DT` (纳入日期)

## 中国债券发行主体违规事件

- **英文表名**: `CBondCompanyIllegality`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录各级主管部门公布的对发债公司违规行为的调查结果与处理决定
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DT` (公告日期)

## 中资美元债发行主体

- **英文表名**: `CNUSBondIssuer`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中资美元债券、发债主体之间的关系数据，包括债券wind代码、发债主体公司id以及关系类型等信息。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_COMPCODE` (债券主体公司id), `USED` (是否有效), `S_INFO_TYPECODE` (关系类型代码)

## 中国债券发行主体审计意见

- **英文表名**: `CBondAuditOpinion`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司历次财务报告（如经审计）的审计机构、审计费用及审计结果
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `AUDIT_AGENCY` (审计机构类别)

## 中国债券发行主体资产负债表

- **英文表名**: `CBondBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司的资产负债表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国债券发行主体财务指标

- **英文表名**: `CBondFinancialIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司的财务衍生数据，如每股营收、每股净资产、每股收益等
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期)

## 中国债券发行主体公布重要指标

- **英文表名**: `CBONDImportantindicators`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司在定期报告中公布的财务指标和分配预案
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `STATEMENT_TYPE` (报表类型), `REPORT_PERIOD` (报告期)

## 中国债券发行主体利润表

- **英文表名**: `CBondIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司的利润表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国债券发行主体现金流量表

- **英文表名**: `CBondCashFlow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司的现金流量表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国债券发行主体TTM财务指标

- **英文表名**: `CBondTTMHis`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司TTM与MRQ指标的历史数据
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (截止日期)

## 中国债券发行主体定期报告披露日期

- **英文表名**: `CBondIssuingDatePredict`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司财务报告的预计披露日期
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期)

## 中国债券发行主体财务费用明细

- **英文表名**: `CBondFinancialExpense`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司财务费用明细数据
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPECODE` (报表类型代码)

## 中国债券发行主体主营业务构成

- **英文表名**: `CBondSalesSegment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司主营业务构成数据
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_SEGMENT_ITEM` (主营业务项目), `S_REPORT_PERIOD` (报告期)

## 中国债券担保人

- **英文表名**: `CbondGuaranteeInfo`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券和担保人之间的关系信息
- **业务主键**: `S_INFO_WINDCODE` (债券Wind代码), `GUARANTOR` (担保人), `B_INFO_EFFECTIVE_DT` (生效日期)

## 中国债券担保人资产负债表

- **英文表名**: `CBondGuaranteeBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券担保人的资产负债表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 中国债券担保人利润表

- **英文表名**: `CBondGuaranteeIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券担保人的利润表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 中国债券担保人现金流量表

- **英文表名**: `CBondGuaranteeCashFlow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券担保人的现金流量表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 央行公开市场操作

- **英文表名**: `CBondRepo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录央行在公开市场的回购操作情况
- **业务主键**: `TRADE_DT` (交易日期), `B_INFO_TERM` (期限(天)), `B_TENDER_METHOD` (招标方式), `B_INFO_REPO_TYPE` (操作类型代码)

## 存贷款利率(央行)

- **英文表名**: `CBondBenchmark`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录自1990年以来历次存、贷款利率调整信息
- **业务主键**: `TRADE_DT` (交易日期), `B_INFO_BENCHMARK` (存贷款利率类型)

## 存款准备金率(央行)

- **英文表名**: `CBondReserveRate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录央行基准利率及存款准备金率信息
- **业务主键**: `TRADE_DT` (交易日期), `S_INFO_RESERVERATETYPE` (准备金率品种)

## 回购标准券折算率

- **英文表名**: `CBondConversionRatio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录交易所公布的有回购品种的国债、企债折算成标准券的比例
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_CVN_STARTDATE` (开始适用日)

## 资产支持证券基本资料

- **英文表名**: `ABSDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录资产支持证券的基本资料
- **业务主键**: `ABS_ID` (项目ID)

## 资产支持证券分档基本资料

- **英文表名**: `ABSSubfiledata`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录资产支持证券的分档基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 资产支持证券交易数据

- **英文表名**: `ABSTransaction`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录资产支持证券的交易数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `S_INC_INITEXECPRI` (成交价格)

## 资产支持证券本息兑付

- **英文表名**: `ABSPayment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录资产支持证券的本息兑付
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (报告日期)

## 中国债券指数基本资料

- **英文表名**: `CBIndexDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券指数的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国债券指数日行情

- **英文表名**: `CBIndexEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国债券指数成分

- **英文表名**: `CBIndexMembers`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券指数的成份股信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

## 中国债券指数权重

- **英文表名**: `CBIndexWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券指数的成份股权重信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份债Wind代码), `TRADE_DT` (交易日期)

## 中国债券指数业绩表现

- **英文表名**: `CBondIndexPerformance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录债券指数的衍生指标，如周涨跌幅、月涨跌幅、年化收益等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 万得中国债券指数基本资料

- **英文表名**: `CBIndexDescriptionWIND`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录万得债券指数的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 万得中国债券指数成份

- **英文表名**: `CBIndexMembersWIND`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录万得债券指数的成份股信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

## 万得中国债券指数日行情

- **英文表名**: `CBIndexEODPricesWIND`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录万得债券指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中债登债券投资者统计

- **英文表名**: `CNBDInvestorStatistics`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国债券网每月投资者类型统计信息
- **业务主键**: `MONTHS` (月份), `INVESTORTYPE` (投资者类型), `TRUSTTYPE` (托管类型)

## 中证估值

- **英文表名**: `CBondAnalysisCSI`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中证债券估值数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中证收益率曲线

- **英文表名**: `CBondCurveCSI`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中证指数提供的债券收益率曲线，债券类型包括国债、金融债、企业债、固定收益平台国债
- **业务主键**: `TRADE_DT` (交易日期), `B_ANAL_CURVENUMBER` (曲线编号), `B_ANAL_CURVETYPE` (曲线类型), `B_ANAL_CURVETERM` (年限)

## 上海清算所债券估值

- **英文表名**: `CBondAnalysisSHC`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录上海清算所债券估值数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中债登估值(国债金融债企债)

- **英文表名**: `CBondAnalysisCNBD1`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对国债、地方政府债、政策性银行债、企业债、商业银行债、银行间资产支持证券的估值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中债登估值(中票短融)

- **英文表名**: `CBondAnalysisCNBD2`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对中期票据、短融、超短融的估值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中债登估值(债务融资工具)

- **英文表名**: `CBondAnalysisCNBD3`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对PPN和其他债务融资工具的估值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中债登估值(同业存单)

- **英文表名**: `CBondAnalysisCNBD4`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对同业存单的估值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中债登估值(公司债)

- **英文表名**: `CBondAnalysisCNBD5`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对公司债的估值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中债登估值(资产支持证券)

- **英文表名**: `CBondAnalysisCNBD6`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对交易所资产支持证券和银行间资产支持票据的估值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中债登估值(CRMW)

- **英文表名**: `CBondAnalysisCNBD8`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对CRMW的估值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中债登估值(中资美元债)

- **英文表名**: `CBondAnalysisCNBD9`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对中资美元债的估值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中债-1-3年国开行债券财富(总值)指数权重

- **英文表名**: `CBACDB1To3IndexWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债-1-3年国开行债券财富(总值)指数成份权重数据
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份债Wind代码), `TRADE_DT` (交易日期)

## 中债-1-3年政策性金融债财富(总值)指数权重

- **英文表名**: `CBA1To3PBBIndexWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债-1-3年政策性金融债财富(总值)指数成份权重数据
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份债Wind代码), `TRADE_DT` (交易日期)

## 中债-信用债总财富(总值)指数权重

- **英文表名**: `CBACreditBIndexTOTRTWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债-信用债总财富(总值)指数成份权重数据
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份债Wind代码), `TRADE_DT` (交易日期)

## 中债-高信用等级债券财富(总值)指数权重

- **英文表名**: `CBAHGBIndexTOTRTWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债-高信用等级债券财富(总值)指数成份权重数据
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份债Wind代码), `TRADE_DT` (交易日期)

## 中债登债券收益率曲线

- **英文表名**: `CBondCurveCNBD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登债券收益率曲线，包含到期、即期
- **业务主键**: `TRADE_DT` (交易日期), `B_ANAL_CURVENUMBER` (曲线编号), `B_ANAL_CURVETYPE` (曲线类型), `B_ANAL_CURVETERM` (标准期限(年))

## 中债登收益率曲线成分样本

- **英文表名**: `CBondCurveMembersCNBD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登收益率曲线和成份债券间的对应关系
- **业务主键**: `TRADE_DT` (交易日期), `B_ANAL_CURVENUMBER` (曲线编号), `S_INFO_WINDCODE` (债券代码)

## 银行柜台债券行情

- **英文表名**: `CBondCounterPrice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行柜台债券市场交易品种的行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期), `BANK_ID` (银行ID)

## 上证所固定收益平台确定报价行情

- **英文表名**: `CBondFixedincomeplatform`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录上证所固定收益平台发布的确定报价行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期), `BID_TRADE_TIME` (买入报价时间), `BID_QUOTINGPARTY` (买入报价方), `ASK_TRADE_TIME` (卖出报价时间), `ASK_QUOTINGPARTY` (卖出报价方)

## 中债登指数行情

- **英文表名**: `CBondIndexEODCNBD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国债券中债登债券分类板块

- **英文表名**: `CBondIndustryCNBD`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录债券的中债登债券分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_INDUSTRYCODE` (板块代码)

## 利率互换行情

- **英文表名**: `CBondPricesIRS`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录外汇交易中心提供的银行间本币利率互换行情，包括固定-浮动和浮动-浮动
- **业务主键**: `TRADE_DT` (日期), `B_INFO_IRSTYPE` (利率互换类型), `B_INFO_REFERENCERATE1` (参考利率1), `B_INFO_REFERENCERATE2` (参考利率2), `B_INFO_TERM` (期限)

## 中国债券第三方信用评级(中债资信)

- **英文表名**: `CBondThirdPartyRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债资信对发债主体的信用评级信息
- **业务主键**: `S_INFO_COMPCODE` (品种ID), `B_RATE_STYLE` (品种类别代码), `B_INFO_LISTDATE` (发布日期), `B_TYPCODE` (评级类型代码), `B_EST_INSTITUTE` (评估机构公司)

## 利率互换收益率曲线

- **英文表名**: `IRSRateYield`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录利率互换收益率曲线
- **业务主键**: `TRADE_DT` (交易日期), `B_ANAL_CURVETYPECODE` (曲线类型代码), `B_ANAL_CURVETERM` (期限(年))

## 上证所固定收益平台成交行情

- **英文表名**: `SSEFixedIncomePlatformPrice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录上证所固定收益平台成交行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 上证所固定收益平台成交明细

- **英文表名**: `SSETransactionDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录上证所固定收益平台成交明细数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期), `TRADE_TIME` (成交时间)

## 银行间债券市场现券行情

- **英文表名**: `CFETSEODPrice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行间债券市场现券品种的日行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国债券存款机构间回购行情

- **英文表名**: `CBondPricesRepo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录交易所和银行间的质押式回购的日行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国共同基金基本资料

- **英文表名**: `ChinaMutualFundDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的基本资料
- **业务主键**: `F_INFO_WINDCODE` (Wind代码)

## 中国共同基金基金经理

- **英文表名**: `ChinaMutualFundManager`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金对应的基金经理信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `F_INFO_FUNDMANAGER` (姓名), `F_INFO_MANAGER_STARTDATE` (任职日期)

## 中国开放式基金费率表

- **英文表名**: `CMFSubredFee`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录开放式基金的申购、赎回费率信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DATE` (公告日期), `FEETYPECODE` (费率类型)

## 中国LOF基金基本资料

- **英文表名**: `LOFDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录LOF基金的基本资料
- **业务主键**: `S_INFO_WINDCODE` (wind代码)

## 中国保本基金基本资料

- **英文表名**: `CPFundDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录保本基金的基本资料
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `START_DT` (保本周期起始日期)

## 中国共同基金代销机构

- **英文表名**: `CMFSellingAgents`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的代销机构
- **业务主键**: `F_INFO_WINDCODE` (WIND代码), `F_AGENCY_NAMEID` (中介机构公司ID), `F_AGENCY_NAME` (机构名称), `F_BEGIN_DATE` (起始日期), `CUR_SIGN` (最新标志)

## 中国共同基金金融机构资格

- **英文表名**: `FinancialQualification`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录金融机构资格的相关情况
- **业务主键**: `ORGANIZATION_NAME` (机构公布名称), `FINANCIAL_TYPE` (金融机构资格类型), `ACQUISITION_DATE` (获得日期), `IS_EFFECTIVE` (是否有效)

## 中国共同基金申购赎回天数

- **英文表名**: `CFundPchRedm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金申购、赎回天数
- **业务主键**: `F_INFO_WINDCODE` (Wind代码)

## 中国共同基金优惠费率（废弃）

- **英文表名**: `CMFPreferentialFee`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的优惠费率数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (优惠活动类型代码), `ANN_DT` (公告日期)

## 中国共同基金暂停申购赎回

- **英文表名**: `ChinaMutualFundSuspendPchRedm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金暂停申购、赎回的信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_INFO_SUSPCHSTARTDT` (暂停申购起始日期), `F_INFO_SUSPCHTYPE` (暂停申购类型代码)

## 中国共同基金WIND行业板块主题分类

- **英文表名**: `CMFIndustryplate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的WIND行业板块主题分类信息
- **业务主键**: `S_INFO_SECTOR` (板块代码), `S_INFO_WINDCODE` (成份万得代码)

## 中国共同基金WIND概念板块主题分类

- **英文表名**: `CMFThemeConcept`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的WIND概念板块主题分类信息
- **业务主键**: `S_INFO_SECTOR` (板块代码), `S_INFO_WINDCODE` (成份万得代码)

## 中国共同基金风格系数

- **英文表名**: `CFundStyleCoefficient`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金根据股票的市值、财务数据计算出其对应的风格系数，同时根据基金的持股数据计算出基金的风格系数，用于判断股票或基金的风格属性
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_CHANGE_DATE` (变动日期)

## 中国共同基金股票风格分类门限值

- **英文表名**: `CFundStyleThreshold`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金股票风格分类门限值
- **业务主键**: `S_CHANGE_DATE` (变动日期)

## 中国共同基金Wind概念分类

- **英文表名**: `CMFConseption`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的Wind概念分类信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `S_INFO_SECTOR` (所属板块代码), `S_INFO_SECTORENTRYDT` (起始日期)

## 中国Wind基金分类

- **英文表名**: `ChinaMutualFundSector`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录基金的Wind分类信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `S_INFO_SECTOR` (所属板块), `S_INFO_SECTORENTRYDT` (起始日期)

## 中国共同基金滚动运作周期

- **英文表名**: `CMFundOperatePeriod`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金滚动运作信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `OPR_PERIOD` (期数), `BATCH1` (批次)

## 中国分级基金基本资料

- **英文表名**: `ChinaGradingFund`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录分级基金的基本资料
- **业务主键**: `F_INFO_FEEDER_WINDCODE` (子基金Wind代码)

## 中国联接基金基本资料

- **英文表名**: `ChinaFeederFund`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录联接基金的基本资料
- **业务主键**: `S_INFO_WINDCODE` (被联接基金指数Wind代码)

## 中国货币市场基金份额结转方式

- **英文表名**: `CMoneyMarketFSCarryOverm`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录货币市场基金收益分配的份额结转方式
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码)

## 中国共同基金被动型基金跟踪指数

- **英文表名**: `ChinaMutualFundTrackingIndex`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录被动型基金跟踪的指数信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_INDEXWINDCODE` (跟踪指数Wind代码), `ENTRY_DT` (生效日期)

## 中国共同基金业绩比较基准配置

- **英文表名**: `ChinaMutualFundBenchMark`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金业绩比较基准的相关配置信息
- **业务主键**: `S_INFO_BGNDT` (起始日期), `S_INFO_ENDDT` (截止日期), `SEC_ID` (证券ID), `SEC_ID2` (证券ID2)

## 中国共同基金初始风险等级

- **英文表名**: `CMFRiskLevel`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的初始风险等级信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码)

## 中国共同基金公司派系风格

- **英文表名**: `CFundFactionalStyle`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金公司的派系风格
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `SEC_IND_CODE` (所属板块代码), `ENTRY_DT` (纳入日期)

## 中国共同基金曾用名

- **英文表名**: `CFundPreviousName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金名称每次变动的信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `BEGINDATE` (起始日期)

## 中国共同基金公司曾用名

- **英文表名**: `CFundCompanyPreviousName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金公司的曾用名信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `CHANGE_DT` (变动日期)

## 中国共同基金业务代码及简称

- **英文表名**: `CMFCodeAndSName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金相关业务代码、简称信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (业务类型代码), `S_CODE` (业务代码)

## 中国共同基金投资品种比例信息

- **英文表名**: `CMFProportionOfInveObj`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的投资品种比例信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期), `INVEST_PCT_TYPECODE` (基金投资占比类型代码)

## 中国共同基金证监会分类

- **英文表名**: `CMFSECClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金所属证监会分类信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `S_INFO_SECTOR` (所属板块代码), `S_INFO_SECTORENTRYDT` (起始日期)

## 中国共同基金基本资料属性变更

- **英文表名**: `CMFDESCChange`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的属性变更前后文本描述信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ITEM` (变更字段名称), `CHANGE_DT` (变更日期)

## 中国共同基金中介机构

- **英文表名**: `ChinaMutualFundAgency`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国共同基金产品的相关中介机构，包括律师事务所、会计师事务、一级交易商所及境外托管人等信息。
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `S_AGENCY_ID` (中介机构ID), `S_RELATION_TYPCODE` (关系类型代码), `BEGINDATE` (起始日期)

## 中国共同基金事件日期信息

- **英文表名**: `CFundEventdateinformation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金相关事件的发生信息，如发生日期、事件类型等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EVENT_TYPE` (事件类型编号), `OCCURRENCE_DATE` (发生日期), `S_INFO_CODE` (交易代码), `LANGUAGE1` (语言)

## 中国共同基金发行

- **英文表名**: `ChinaMutualFundIssue`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金发行的相关情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国共同基金重大事件

- **英文表名**: `ChinaFundMajorEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的负面事件信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_EVENT_CATEGORYCODE` (事件类型代码), `S_EVENT_HAPDATE` (发生日期)

## 中国共同基金分红

- **英文表名**: `ChinaMFDividend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的分红信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_E_BCH_DT` (可分配收益基准日), `EX_DT` (除息日)

## 中国共同基金基金份额拆分与折算

- **英文表名**: `CMFundSplit`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金份额拆分与折算信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_INFO_SPLITTYPE` (类型), `F_INFO_SHARETRANSDATE` (拆分折算日)

## 中国共同基金转型

- **英文表名**: `ChinaMutualFundTransformation`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录基金的转型信息
- **业务主键**: `PREWINDCODE` (转型前基金Wind代码), `POSTWINDCODE` (转型后基金Wind代码), `F_INFO_PRENAME` (转型前基金简称), `F_INFO_POSTNAME` (转型后基金简称)

## 中国共同基金行政许可事项进度表

- **英文表名**: `CFundAdmPermitSchedule`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金注册的行政许可事项进度信息
- **业务主键**: `COMP_ID` (公司ID), `ANNDATE` (公告日期), `TYPE_NAME` (申请事项)

## 中国共同基金持有人大会通知

- **英文表名**: `Cfundholdersmeeting`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录股东大会的召开时间及审议事项
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期), `MEETING_DT` (会议日期), `MEETING_TYPE` (会议类型)

## 中国共同基金持有人

- **英文表名**: `CMFHolder`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的持有人信息
- **业务主键**: `S_INFO_WINDCODE` (证券ID), `S_FA_LATELYRD` (报告期), `B_INFO_HOLDER` (持有人)

## 中国共同基金持有人结构

- **英文表名**: `CMFHolderStructure`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的持有人结构情况
- **业务主键**: `SEC_ID` (证券ID), `END_DT` (截止日期)

## 中国共同基金单一投资者持有基金份额比例异常信息

- **英文表名**: `CMFHoldingratioanomaly`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录单一投资者持有基金份额比例异常的信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `F_UNIT_RPSTARTDATE` (报告期开始日期), `F_UNIT_RPENDDATE` (报告期截止日期), `F_INQUIRER_TYPE` (投资者类别), `F_INQUIRER_TYPE_NUM` (投资者序号)

## 中国共同基金违规事件

- **英文表名**: `CFundIllegality`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金公司的违规事件
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DT` (公告日期), `SUBJECT` (违规主体), `PROCESSOR` (处理人)

## 中国共同基金比例认购

- **英文表名**: `CMFRatioSubscribe`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金比例认购的结果，包括比例确认比例、有效认购申请金额、有效认购金额等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (比例确认公告日期)

## 中国共同基金清算

- **英文表名**: `CMFLiquidation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国共同基金清算阶段的数据，包括清算类型代码、清算起始日及清算原因说明等信息。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期), `CLEARINGTYPE_CODE` (清算类型代码)

## 基金关联方持有份额

- **英文表名**: `CMFRelatedPartiesHolder`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金关联方持有该基金的份额数据，包括持有人名称、持有份额及持有比例等信息。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `END_DATE` (截止日期), `HOLDER_COMPCODE` (持有人公司ID)

## 中国共同基金份额

- **英文表名**: `ChinaMutualFundShare`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的份额信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `CHANGE_DATE` (变动日期)

## 中国共同基金净值操作记录表

- **英文表名**: `CMFNAVOperationrecord`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金净值变动操作的流水信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `PRICE_DATE` (净值截止日期), `F_NAV_OLD` (调整前净值)

## 中国货币式基金日收益(拆分)

- **英文表名**: `CMoneyMarketDailyFIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录货币市场基金每万份基金每天的单位收益及最近七日收益所折算的年资产收益率
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_INFO_BGNDATE` (起始日期), `F_INFO_ENDDATE` (截止日期)

## 中国共同基金净值

- **英文表名**: `ChinaMutualFundNAV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期（每周末）或不定期（上市、扩募、摘牌）公布的基金净值和累计净值
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `PRICE_DATE` (截止日期)

## 中国货币式基金日收益

- **英文表名**: `CMoneyMarketFIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录货币市场基金每万份基金单位收益及最近七日收益所折算的年资产收益率
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_INFO_ENDDATE` (截止日期)

## 中国上市基金日行情

- **英文表名**: `ChinaClosedFundEODPrice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录的是在上交所、深交所上市的所有的开放式和封闭式基金的行情。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国共同基金停复牌

- **英文表名**: `CMFTradingSuspension`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金停牌、复牌信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_DQ_SUSPENDDATE` (停牌日期)

## 中国共同基金业绩比较基准行情

- **英文表名**: `ChinaMutualFundBenchmarkEOD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金对应的业绩比较基准指数行情数据
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `TRADE_DT` (交易日期)

## 中国共同基金场内流通份额

- **英文表名**: `ChinaMutualFundFloatShare`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录深圳证券交易所披露的LOF和ETF场内流通份额
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国共同基金Wind基金仓位估算

- **英文表名**: `ChinaMutualFundPosEstimation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期报告公布持有股票的组合类别(大市值组合、中市值组合、小市值组合)，估算基金分别持有各个组合的权重、持有股票占净资产的比例、以及下一交易日利用该比例估算出的基金收盘净值
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码), `F_EST_DATE` (估算日期)

## 中国共同基金席位交易量及佣金

- **英文表名**: `ChinaMutualFundSeatTrading`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金在各券商席位上各交易品种分别的成交量，定期（中期、年度）公布
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_REPORTPERIOD` (报告期), `S_INFO_SECURNAME` (证券公司简称)

## 中国共同基金净值表现(报告期)

- **英文表名**: `ChinaMutualFundRepNAVPer`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金报告期的净值表现情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_INFO_REPORTPERIOD` (报告期), `PERIOD_CODE` (期间代码)

## 中国共同基金利率敏感分析

- **英文表名**: `Cfundratesensitive`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金利率的敏感分析
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `PRICE_FLUNCUATION` (价格变动), `TYPE_CODE` (敏感分析价格类型代码)

## 中国货币式基金重要指标(报告期)

- **英文表名**: `CMMQuarterlydata`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录货币市场基金季度重要数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_INFO_BGNDATE` (报告期起始日期), `F_INFO_ENDDATE` (报告期截止日期)

## 中国上市基金IOPV收盘净值

- **英文表名**: `CMFIOPVNAV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的IOPV收盘净值
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `PRICE_DATE` (日期)

## 中国共同基金基金经理业绩表现

- **英文表名**: `ChinaMFMPerformance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金经理的业绩表现
- **业务主键**: `FUNDMANAGER_ID` (基金经理ID), `TRADE_DATE` (日期), `FMINDEX_TYPE` (基金经理指数类型)

## 中国共同基金业绩表现

- **英文表名**: `ChinaMFPerformance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的业绩表现
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国共同基金指数业绩表现

- **英文表名**: `FIndexPerformance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金指数的业绩表现
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国共同基金定投收益率及排名表

- **英文表名**: `CMFFixedinvestmentRate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金进行定投的收益率及排名信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `F_TYPE_CODE` (投资类型代码)

## 中国共同基金风险分析指标

- **英文表名**: `ChinaMFRiskanalysisIndex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国共同基金风险分析指标的数据，包括风险分析指标类型代码、指标名称及指标数值等信息。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `RISKANALYSIS_CODE` (指标类型代码)

## 中国共同基金指数风险分析指标

- **英文表名**: `FIndexRiskanalysis`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国共同基金指数风险分析指标的数据，包括风险分析指标类型代码、指标名称及指标数值等信息。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `RISKANALYSIS_CODE` (指标类型代码)

## 中国封闭式基金场内申购赎回

- **英文表名**: `ClosedFundPchRedm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录封闭式基金场内申购赎回情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_EXCHMARKET` (交易所)

## 中国ETF申购赎回

- **英文表名**: `ETFPchRedm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录ETF基金申购赎回情况
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码)

## 中国开放式基金场内申购赎回

- **英文表名**: `LOFPchRedm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录开放式基金场内申购赎回情况
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码)

## 中国共同基金申购赎回情况

- **英文表名**: `ChinaMutualFundPchRedm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的申购赎回情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_UNIT_RPSTARTDATE` (报告期开始日期), `F_UNIT_RPENDDATE` (报告期结束日期)

## 中国共同基金投资组合重大变动(报告期)

- **英文表名**: `CFundPortfoliochanges`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期（季度）公布的投资组合重大变动信息
- **业务主键**: `F_INFO_WINDCODE` (基金代码), `REPORT_PERIOD` (报告期), `S_INFO_WINDCODE` (股票代码), `CHANGE_TYPE` (变动类型)

## 中国共同基金投资组合——资产配置

- **英文表名**: `ChinaMutualFundAssetPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期（季度）公布的投资于各种类型证券资产的组合情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_PRT_ENDDATE` (截止日期)

## 中国共同基金投资组合——其他证券

- **英文表名**: `CMFOtherPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期（季度）公布的持有其他证券明细
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `END_DT` (截止日期), `S_INFO_HOLDWINDCODE` (持有证券的Wind代码)

## 中国货币式基金投资组合剩余期限(报告期)

- **英文表名**: `CMMFPortfolioPTM`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录货币式基金定期（季度）公布的投资组合剩余期限信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `F_PTM_TOP` (剩余期下限), `TYPECODE` (类型)

## 中国共同基金投资组合——行业配置

- **英文表名**: `ChinaMutualFundIndPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期（季度）公布的持股分属于各行业的组合。行业分类采用证监会标准
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_PRT_ENDDATE` (截止日期), `S_INFO_CSRCINDUSNAME` (行业名称)

## 中国共同基金投资组合——持股明细

- **英文表名**: `ChinaMutualFundStockPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期（季度）公布的持股明细
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码), `F_PRT_ENDDATE` (截止日期), `S_INFO_STOCKWINDCODE` (持有股票Wind代码)

## 中国共同基金投资组合——持券明细

- **英文表名**: `ChinaMutualFundBondPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期（季度）公布的持券明细
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码), `F_PRT_ENDDATE` (截止日期), `S_INFO_BONDWINDCODE` (持有债券Wind代码)

## 中国共同基金持有流通受限证券明细

- **英文表名**: `CFundHoldRestrictedCirculation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录报告期末基金持有的流通受限证券情况
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `ENDDATE` (截止日期), `F_INFO_RESTRICTEDCODE` (流通受限证券代码), `PLACING_DATE` (配售日期), `CIRCULATION_DATE` (可流通日期)

## 中国共同基金投资组合第三方行业配置

- **英文表名**: `CMFundThirdPartyIndPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国共同基金投资组合第三方行业配置信息，包括Wind代码、行业代码、持仓市值等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `PRT_ENDDATE` (截止日期), `IND_CODE` (行业代码)

## 中国共同基金第三方评级

- **英文表名**: `CMFundThirdPartyRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的第三方评级评级
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `RPTDATE` (日期（月份）), `RATING_INTERVAL` (评级区间), `RATING_GAGENCY` (评级机构), `RATING_TYPE` (评级类型)

## 中国共同基金Wind基金评级

- **英文表名**: `CMFundWindRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金的Wind评级信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `RPTDATE` (日期), `RATING_INTERVAL` (评级区间), `RATE_STYLE` (评级类型)

## 中国共同基金机构奖项排名

- **英文表名**: `CompanyAward`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录新财富券商排名等机构奖项排名
- **业务主键**: `S_INFO_CHINESEINTRODUCTION` (机构简称), `S_INFO_AWARD_CODE` (奖项代码), `S_INFO_YEAR` (年度), `S_INFO_RANKING` (排名)

## 全球基金债券组合(分评级)

- **英文表名**: `FundBondportfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录全球基金持有的不同评级等级的债券组合信息
- **业务主键**: `S_INFO_CODE` (基金代码), `DEADLINE` (截止日期)

## 中国共同基金资产负债表

- **英文表名**: `CMFBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录封闭式基金和开放式基金历次财务报告公布的资产负债表
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期)

## 中国共同基金财务指标(报告期)

- **英文表名**: `CMFFinancialIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录Wind根据公布的基金财务数据，利用权威公式计算出的财务指标
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期)

## 中国共同基金利润表

- **英文表名**: `CMFIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录封闭式基金和开放式基金历次财务报告公布的利润表
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期)

## 中国共同基金定期报告披露日期

- **英文表名**: `CMFIssuingDatePredict`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期报告的披露日期
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `START_DT` (报告起始日), `END_DT` (报告截止日)

## 中国共同基金季报财务指标

- **英文表名**: `CMFQuarterlyFinancialIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金季报中披露的财务指标数据
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `F_UNIT_RPSTARTDATE` (报告期开始日期), `F_UNIT_RPENDDATE` (报告期结束日期)

## 中国共同基金公允价值变动收益(报告期)

- **英文表名**: `CMFfairvalueChangeProfit`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金报告期内公允价值变动收益(损失)项目说明，此数据是新会计准则新增内容
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期)

## 中国共同基金净值变动表

- **英文表名**: `CMFNAVChange`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金定期报告披露的净值变动表，属于基金财务报表的一种
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `RPSTARTDATE` (报告期开始日期), `RPENDDATE` (报告期结束日期)

## 中国分级基金条款

- **英文表名**: `SCFClause`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录分级基金的条款信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (条款属性类型代码), `START_DT` (起始日期)

## 中国分级基金折算

- **英文表名**: `SCFConvert`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录分级基金的折算信息
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码), `CONVERT_REASON` (折算原因代码), `CONVERT_DT` (折算基准日), `NAV_MIN` (基金净值下限(元))

## 中国分级基金收益分配

- **英文表名**: `SCFReturnDistribution`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录分级基金的收益分配信息
- **业务主键**: `F_INFO_FEEDER_WINDCODE` (子基金Wind代码), `RULE_STARETDT` (收益分配条约起始日期), `F_NAV_LMT` (基金净值下限(元))

## 中港互认基金名单

- **英文表名**: `CHFundList`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中港互认基金的明细清单
- **业务主键**: `F_INFO_COMPCODE` (基金ID), `START_DT` (纳入日期)

## 中港互认基金分类

- **英文表名**: `CHFundSector`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中港互认基金的基金分类信息
- **业务主键**: `F_INFO_COMPCODE` (基金ID), `F_INFO_WINDCODE` (子基金Wind代码), `S_INFO_SECTORNAME` (所属板块名称), `S_INFO_SECTORENTRYDT` (起始日期)

## 中港互认基金费率

- **英文表名**: `CHFundFee`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中港互认基金申购、赎回费率信息
- **业务主键**: `F_INFO_COMPCODE` (基金ID), `S_INFO_WINDCODE` (子基金Wind代码), `FEETYPECODE` (费率类型), `CHANGE_DT` (变动日期)

## 中港互认基金基金经理

- **英文表名**: `CHFundManager`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中港互认基金的基金经理信息
- **业务主键**: `F_INFO_COMPCODE` (基金ID), `F_INFO_FUNDMANAGER` (基金经理姓名), `F_INFO_MANAGER_STARTDATE` (任职日期)

## 中港互认基金基本资料

- **英文表名**: `CHFundDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中港互认基金的基本资料
- **业务主键**: `F_INFO_COMPCODE` (基金ID), `SEC_ID` (子基金ID)

## 中港互认基金中介机构

- **英文表名**: `CHFundAgency`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中港互认基金发行相关中介结构
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_RELATION_TYPCODE` (关系类型代码), `S_AGENCY_NAMEID` (机构名称ID), `ANN_DT` (公告日期)

## QFII基本资料

- **英文表名**: `QFIIDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录QFII的基本资料
- **业务主键**: `F_INFO_COMPCODE` (公司ID), `TRUSTEE_NAME` (公司名称), `APPROVAL_DATE_ACCOUNT` (帐户获准日期), `ANN_DATE` (信息披露日期)

## QFII额度变动

- **英文表名**: `QFIIQuotaChange`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录QFII的额度变动情况
- **业务主键**: `F_INFO_COMPCODE` (公司ID), `CHANGE_DT` (变动日期), `TYPE` (类型代码)

## 中国共同基金跟踪基准指数偏离度阀值

- **英文表名**: `CFundindextable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金跟踪的基准指数偏离度阀值
- **业务主键**: `F_INFO_WINDCODE` (Wind代码)

## 中国共同基金WIND指数对应成份板块

- **英文表名**: `CFundWindIndexcomponent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金WIND指数对应的成份板块
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_CODE` (成份板块代码)

## 中国共同基金WIND指数最新成份明细

- **英文表名**: `CFundWindIndexMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金WIND指数的最新成份明细
- **业务主键**: `S_CON_CODE` (板块代码), `S_INFO_WINDCODE` (成份万得代码)

## 中国共同基金指数基本资料

- **英文表名**: `CMFIndexDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金指数的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国共同基金指数行情

- **英文表名**: `CMFIndexEOD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国基金指数成份

- **英文表名**: `CFundIndexMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金指数成份股信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

## 中国国债基准收益率

- **英文表名**: `CGBbenchmark`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国国债基准收益率信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国权证基本资料

- **英文表名**: `CWarrantDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国权证的基本资料
- **业务主键**: `WINDCODE` (权证证券id), `UNDERLYINGWINDCODE` (标的证券id), `DURATION_DAYS` (存续期限(天))

## 中国权证持有人

- **英文表名**: `CWarrantHolder`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国权证的持有人信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `END_DATE` (日期), `HOLDER` (持有人)

## AH股关联证券

- **英文表名**: `SHSZRelatedsecurities`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股和A股代码的对应关系
- **业务主键**: `EXCHANGE_A` (交易所1), `S_INFO_WINDCODE` (WIND代码1), `EXCHANGE_B` (交易所2), `S_INFO_WINDCOD2` (WIND代码2)

## 证券类型代码配置表

- **英文表名**: `SecuritiesTypecode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 证券类型和代码的配置表
- **业务主键**: `TYPE_CODE` (证券类型代码)

## 陆港通通道持股数量统计(中央结算系统)

- **英文表名**: `SHSCChannelholdings`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪、深港通标的股票各自通过通道持股的情况
- **业务主键**: `S_INFO_WINDCODE` (WIND代码), `TRADE_DT` (持股日期)

## 陆港通卖空数据

- **英文表名**: `SHSCShortselling`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪股通卖空数据，包含成分股、可供卖空股数和卖空
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 陆港通日交易统计

- **英文表名**: `SHSCDailyStatistics`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪、深港通每日交易统计情况
- **业务主键**: `TRADE_DT` (日期), `S_INFO_EXCHMARKET` (交易所英文简称), `ITEM_CODE` (项目代码)

## 陆港通日十大成交活跃股统计

- **英文表名**: `SHSCTop10ActiveStocks`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪、深港通每日十大成交活跃股成交信息，包含买入\卖出\成交金额
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期), `S_INFO_EXCHMARKETNAME` (交易所英文简称)

## 香港交易所交易日历

- **英文表名**: `HKEXCalendar`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港交易所的交易日信息
- **业务主键**: `TRADE_DAYS` (日期), `S_INFO_EXCHMARKET` (交易所英文简称)

## 香港证券回购信息

- **英文表名**: `HKStockRepo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港联交所的证券回购信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 香港ETF日行情

- **英文表名**: `HKETFEODPrice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港ETF基金的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 香港基金日行情估值指标

- **英文表名**: `HKFundEODDerivativeIndex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港基金的日估值和财务指标，如市值、市盈
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `FINANCIAL_TRADE_DT` (交易日期)

## 香港牛熊证日行情

- **英文表名**: `HKCBBCEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港牛熊证的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 香港衍生权证日行情

- **英文表名**: `HKWarrantEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港权证的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 香港牛熊证基本资料

- **英文表名**: `HKCBBCInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港牛熊证的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CORR_WINDCODE` (Wind代码), `NAME` (中文名称), `RELEASEDATE` (推出日)

## 香港权证基本资料

- **英文表名**: `HKWarrantInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港权证的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 香港权证街货量

- **英文表名**: `HKOutstandingWarrantVolume`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港联交所公布的收市后由公众投资者持有的权证数量。
- **业务主键**: `SEC_ID` (权证证券id), `TRADE_DT` (交易日期)

## 中国券商理财基本资料

- **英文表名**: `ChinaInhouseFundDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财的基本资料
- **业务主键**: `F_INFO_WINDCODE` (Wind代码)

## 中国券商理财中介机构

- **英文表名**: `SAMFundAgency`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财发行的相关中介机构
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期), `S_AGENCY_NAME` (中介机构名称), `S_AGENCY_ID` (中介机构ID), `S_RELATION_TYPCODE` (关系类型代码), `BEGINDATE` (起始日期), `CUR_SIGN` (最新标志)

## 中国券商理财费率

- **英文表名**: `FundSAMFee`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财申购、赎回的费率
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期), `FEETYPECODE` (费率类型代码), `CHARGEWAY` (收费类型)

## 中国券商理财基金经理

- **英文表名**: `ChinaInhouseFundManager`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录券商理财的基金经理
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `F_INFO_FUNDMANAGER` (姓名), `F_INFO_MANAGER_STARTDATE` (任职日期)

## 中国券商理财板块

- **英文表名**: `ChinaInhouseFundSector`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录券商理财的wind分类板块
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `S_INFO_SECTOR` (所属板块), `CUR_SIGN` (最新标志)

## 中国券商理财滚动运作周期

- **英文表名**: `SAMFundOperatePeriod`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录券商理财的滚动运作周期，如定价申购、赎回周期

## 中国券商理财基金业协会编码

- **英文表名**: `SAMFundAssociationCode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财基金业协会公布的注册编码
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (业务代码类型), `S_CODE` (业务代码)

## 中国券商理财分级基金基本资料

- **英文表名**: `SAMGradingFund`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国券商理财分级基金的基本资料
- **业务主键**: `S_INFO_WINDCODE` (母基金Wind代码), `F_INFO_FEEDER_WINDCODE` (子基金Wind代码)

## 中国券商理财份额

- **英文表名**: `ChinaInhouseFundShare`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财的份额信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `CHANGE_DATE` (变动日期), `BEGINDATE` (起始日期)

## 中国券商理财净值

- **英文表名**: `ChinaInhouseFundNAV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财的净值信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `ANN_DATE` (公告日期), `PRICE_DATE` (截止日期)

## 中国券商理财(货币式)收益率

- **英文表名**: `ChinaInHouseFundMarketFIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录货币式券商理财的收益率
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `F_INFO_BGNDATE` (起始日期), `F_INFO_ENDDATE` (截止日期)

## 中国券商理财业绩表现

- **英文表名**: `FundSAMPerformance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财的业绩表现，如周涨跌幅、月涨跌幅等
- **业务主键**: `SEC_ID` (证券ID), `TRADE_DT` (交易日期)

## 中国券商理财风险分析指标

- **英文表名**: `FundSAMRiskanalysisIndex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国券商理财风险分析指标，包含信息比率（近1周）、信息比率（近3月）、信息比率（近6月）、信息比率（近1年）、信息比率（近3年）等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `RISKANALYSIS_CODE` (指标类型代码)

## 中国券商集合理财分红

- **英文表名**: `ChinaInhouseFundDividend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财的分红信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EX_DT` (除息日)

## 中国券商理财投资组合-资产配置

- **英文表名**: `SAMFundAssetPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商集合理财公布的投资于各种类型证券资产的组合情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_PRT_ENDDATE` (截止日期)

## 中国券商集合理财投资组合-行业

- **英文表名**: `SAMFundIndPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商集合理财公布的持股分属于各行业的组合。行业分类采用证监会标准
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `F_PRT_ENDDATE` (截止日期), `F_INFO_CSRCINDUSCODE` (行业编号)

## 券商集合理财投资组合-持仓明细

- **英文表名**: `SAMFundStockPortfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商集合理财公布的持仓明细
- **业务主键**: `F_INFO_WINDCODE` (集合理财Wind代码), `F_PRT_ENDDATE` (截止日期), `S_INFO_WINDCODE` (持有证券Wind代码)

## 中国券商集合理财资产负债表

- **英文表名**: `SAMFundBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录集合理财股票投资、负债、未分配利润等财务信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (截止日期)

## 中国券商集合理财经营业绩表

- **英文表名**: `SAMFundIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录集合理财收入、费用、支出等财务信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `START_DATE` (起始日期), `CLOSING_DATE` (截止日期)

## 中国券商集合理财财务指标

- **英文表名**: `SAMFundFinancialIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录集合理财产品相关财务指标，如本期单位净收益、期末资产净值等
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `F_STARTDATEINST` (起始日期), `F_ENDDATEINST` (截止日期)

## 保险资管产品净值

- **英文表名**: `IAMFundNAV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录保险资管产品的净值信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `PRICE_DATE` (日期)

## 基金子公司资管产品净值

- **英文表名**: `FSAMNAV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金子公司资管产品的净值信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `PRICE_DATE` (日期)

## 基金专户资管产品净值

- **英文表名**: `FSACMPNAV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金专户资管产品的净值信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `PRICE_DATE` (日期)

## 中国私募基金管理人资料

- **英文表名**: `CHFManagerInformation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录私募基金管理人的资料
- **业务主键**: `F_INFO_CORP_FUNDMANAGEMENTCOMP` (基金管理人全称(中文)), `ANN_DATE` (公告日期)

## 中国私募基金基本资料

- **英文表名**: `ChinaHedgeFundDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录私募基金的基本资料
- **业务主键**: `F_INFO_WINDCODE` (Wind代码)

## 中国私募基金费率

- **英文表名**: `ChinaHedgeFundFee`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录私募基金的申购、赎回费率

## 中国私募基金基金经理

- **英文表名**: `ChinaHedgeFundManager`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录私募基金任职的基金经理
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `F_INFO_FUNDMANAGER` (姓名), `F_INFO_MANAGER_STARTDATE` (任职日期)

## 中国私募基金Wind板块

- **英文表名**: `ChinaHedgeFundSector`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录私募基金的Wind板块分类信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `S_INFO_SECTOR` (所属板块), `S_INFO_SECTORENTRYDT` (起始日期)

## 中国私募基金基本资料(基金业协会)

- **英文表名**: `AMACCHFDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金业协会披露的私募基金基本资料
- **业务主键**: `F_INFO_FULLNAME` (基金名称), `F_DISCLOSUR_WEBSITES` (产品信息披露网址)

## 中国私募基金净值

- **英文表名**: `ChinaHedgeFundNAV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录私募基金的净值信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `ANN_DATE` (公告日期), `PRICE_DATE` (截止日期)

## 中国私募基金业绩表现

- **英文表名**: `ChinaHedgeFundPerformance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录私募基金的业绩表现，如周涨跌幅、月涨跌幅等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `F_SFRANK_RECENTTWOYEAR` (最近两年同类排名), `F_SFRANK_RECENTTHREEYEAR` (最近三年同类排名), `F_SFRANK_RECENTFIVEYEAR` (最近五年同类排名), `F_SFRANK_SINCEFOUND` (成立以来同类排名)

## 中国私募基金指数基本资料

- **英文表名**: `CHFIndexDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录私募基金指数的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国私募基金指数行情

- **英文表名**: `CHFIndexEOD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录私募基金指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国银行理财产品基本资料

- **英文表名**: `ChinaBWMDesc`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行理财产品的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国银行理财产品收益率曲线

- **英文表名**: `ChinaBWMCurve`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行理财产品的收益率曲线
- **业务主键**: `TRADE_DT` (日期), `CODE` (理财产品收益率曲线代码), `TERM` (曲线期限), `CRNCY_CODE` (币种)

## 中国银行理财产品净值

- **英文表名**: `ChinaBWMNAV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行理财产品的净值信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `PRICE_DATE` (截止日期)

## 中国银行理财产品阶段收益

- **英文表名**: `ChinaBWMSTAGEINCOME`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国银行理财产品的阶段收益情况，包括收益起始日、区间收益率、复权单位净值等相关信息。
- **业务主键**: `PRODUCT_ID` (产品证券ID), `INCOMEENDDATE` (收益截止日), `INTERVAL_YIELD` (区间收益率)

## 国内银行业金融机构分类(银监会)

- **英文表名**: `BankingFIClassCBRC`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录国内银行业各金融机构的银监会行业分类
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_TYPECODE` (分类代码), `ENTRY_DT` (纳入日期)

## 国内保险业金融机构分类

- **英文表名**: `InsuranceFIClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录国内保险机构的行业分类
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_TYPECODE` (分类代码), `ENTRY_DT` (纳入日期)

## 非上市银行资产负债表

- **英文表名**: `UnlistedBankBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市银行的资产负债表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市银行利润表

- **英文表名**: `UnlistedBankIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市银行的利润表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市银行现金流量表

- **英文表名**: `UnlistedBankCashFlow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市银行的现金流量表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市银行专用指标

- **英文表名**: `UnlistedBankIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市银行公布的一些特殊的财务指标
- **业务主键**: `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `S_INFO_COMPCODE` (公司id)

## 非上市保险资产负债表

- **英文表名**: `UnlistedInsuranceBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市保险的资产负债表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市保险利润表

- **英文表名**: `UnlistedInsuranceIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市保险的利润表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市保险现金流量表

- **英文表名**: `UnlistedInsuranceCashFlow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市保险的现金流量表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市保险专用指标

- **英文表名**: `UnlistedInsuranceIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市保险公布的一些特殊的财务指标
- **业务主键**: `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `S_INFO_COMPCODE` (公司id)

## 非上市券商资产负债表

- **英文表名**: `UnlistedBrokerBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市券商的资产负债表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市券商利润表

- **英文表名**: `UnlistedBrokerIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市券商的利润表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市券商现金流量表

- **英文表名**: `UnlistedBrokerCashFlow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市券商的现金流量表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 非上市券商专用指标

- **英文表名**: `UnlistedIBrokerIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非上市券商公司的一些特殊的财务指标
- **业务主键**: `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `S_INFO_COMPCODE` (公司id)

## 国家主权信用评级

- **英文表名**: `SovereignCreditRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录国家主权债务评级等
- **业务主键**: `COUNTRY_CODES` (ISO国家及地区编码(3位)), `ANN_DT` (评级日期), `B_INFO_CREDITRATINGAGENCY` (评级机构代码), `CRNCY_TYPE` (货币类别), `B_RATE_STYLE` (信用评级期限类别)

## 沪深公司公告栏目

- **英文表名**: `AShareAnnColumn`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录沪深公司公告栏目信息
- **业务主键**: `N_INFO_CODE` (Wind栏目代码)

## 沪深公司公告信息

- **英文表名**: `AShareAnnInf`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深公司发布的公告详细信息
- **业务主键**: `ID` (公告ID)

## 沪深公司公告文本

- **英文表名**: `AShareAnnText`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `ANN_OBJECT_ID` (公告ID)

## 债券公告栏目

- **英文表名**: `BondAnnColumn`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录发债公司公告栏目信息

## 债券公告信息

- **英文表名**: `BondAnnInf`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录发债公司发布的公告详细信息

## 基金公告栏目

- **英文表名**: `FundAnnColumn`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录基金公司公告栏目信息

## 基金公告信息

- **英文表名**: `FundAnnInf`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金公司发布的公告详细信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `N_INFO_STOCKID` (证券ID), `ID` (公告ID)

## 基金公告文本

- **英文表名**: `FundAnnInfText`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录文本格式的基金公告
- **业务主键**: `ANN_OBJECT_ID` (公告主表对象ID)

## 中国概念股wind兼容代码

- **英文表名**: `CCStockWindCustomCode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国概念股Wind定义的唯一标识证券的代码
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 股市负面新闻V2018

- **英文表名**: `StockNegativeNews2`
- **更新频率**: nan
- **全量产品**: 否
- **说明**: 记录2018年股市负面新闻信息，包括新闻标题、新闻内容、新闻来源、新闻链接等。

## 陆港通机构持股

- **英文表名**: `SHSCmechanismownership`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录陆港通机构持股数据，包括持股数量、机构名称、截止日等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_HOLDER_ENDDATE` (截止日期), `S_HOLDER_NAME` (机构名称), `S_HOLDER_NUM` (机构编号)

## 债券负面新闻V2018

- **英文表名**: `BondNegativeNews2`
- **更新频率**: nan
- **全量产品**: 否
- **说明**: 记录2018年债券负面新闻信息，包括新闻标题、新闻内容、新闻来源、新闻链接等。

## 债券负面新闻

- **英文表名**: `BondNegativeNews`
- **更新频率**: nan
- **全量产品**: 否
- **说明**: 记录债券负面新闻信息，包括新闻标题、新闻内容、新闻来源、新闻链接等。

## 中小微企业分类

- **英文表名**: `EnterpriseDivision`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中小微企业的分类数据，包括公司名称和企业类型。
- **业务主键**: `COMP_ID` (公司ID)

## 金融企业分类

- **英文表名**: `FinancialInstitutionClassify`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录金融企业的分类数据，包括公司名称和企业类型。
- **业务主键**: `COMP_ID` (公司ID)

## 高新技术企业分类

- **英文表名**: `HightechEnterprise`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录高新技术企业的分类数据，包括公司名称和企业类型。

## 中国债券基本资料(增量)

- **英文表名**: `CBondDescriptionZL`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国债券担保信息(增量)

- **英文表名**: `CbondGuaranteeInfoZL`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (债券Wind代码), `GUARANTOR` (担保人), `B_INFO_EFFECTIVE_DT` (生效日期)

## 中港互认基金基本资料(增量)

- **英文表名**: `CHFundDescriptionZL`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `F_INFO_COMPCODE` (基金ID), `SEC_ID` (子基金ID)

## 上市公司ESG评级数据(社投盟细分指标明细)(试用)

- **英文表名**: `AShareESGRatingDatatest`
- **更新频率**: month
- **全量产品**: 否
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (年份)

## 上市公司ESG评级数据(社会价值投资联盟)(试用)

- **英文表名**: `CASVIESGRatingDatatest`
- **更新频率**: month
- **全量产品**: 否

## 上市公司ESG评级数据(商道融绿)(试用)

- **英文表名**: `SynTaoESGRatingDatatest`
- **更新频率**: month
- **全量产品**: 否

## 上市公司ESG评级数据(商道融绿细分指标明细)(试用)

- **英文表名**: `AShareESGRatingData1test`
- **更新频率**: month
- **全量产品**: 否
- **业务主键**: `S_INFO_COMPCODE` (公司id), `ANN_DT` (公告日期)

## 上市公司ESG评级数据(华证指数)(试用)

- **英文表名**: `SSIESGRatingDatatest`
- **更新频率**: month
- **全量产品**: 否

## 上市公司ESG评级数据(华证细分指标明细)(试用)

- **英文表名**: `SSIESGRatingDetailsDatatest`
- **更新频率**: month
- **全量产品**: 否
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (年份)

## 华证ESG尾部风险名单(试用)

- **英文表名**: `SSIESGTailRiskListtest`
- **更新频率**: month
- **全量产品**: 否

## 华证ESG风险预警名单(试用)

- **英文表名**: `SSIESGRiskWarningListtest`
- **更新频率**: month
- **全量产品**: 否

## 上市公司ESG评级数据(嘉实基金)（试用）

- **英文表名**: `HarvestFundESGRatingDatatest`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (年份)

## 上市公司ESG评级数据(嘉实基金细分指标明细)（试用）

- **英文表名**: `JSFundESGRatingDetailData`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (年份)

## 公告表

- **英文表名**: `companytxtinfo`
- **更新频率**: day
- **全量产品**: 否

## 公告新闻栏目配置表

- **英文表名**: `zxfinancialcolumn`
- **更新频率**: day
- **全量产品**: 是

## 中债登指数权重(废弃)

- **英文表名**: `CBIndexWeightCNBD`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份债Wind代码), `TRADE_DT` (交易日期), `S_INFO_EXCHMARKET` (流通场所)

## 中债登估值(废弃)

- **英文表名**: `CBondAnalysisCNBD`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `B_ANAL_EXCHANGE` (流通场所), `B_ANAL_CREDIBILITY` (可信度), `B_ANAL_PRIORITY` (优先级)

## 中国债券Wind代码变更表

- **英文表名**: `CBondChangeWindcode`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_OLDWINDCODE` (变更前代码), `CHANGE_DATE` (代码变更日期)

## 中国债券业务代码及简称

- **英文表名**: `CBondCodeAndSName`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `SEC_ID` (品种ID), `TYPE_CODE` (业务代码类型), `S_CODE` (业务代码)

## 中国债券公司简介

- **英文表名**: `CBondIntroduction`
- **更新频率**: day
- **全量产品**: 是
- **业务主键**: `S_INFO_COMPCODE` (公司ID)

## 中国债券证券关系表

- **英文表名**: `CBondRalatedSecuritiesCode`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_RALATEDCODE` (关联证券Wind代码), `S_RELATION_TYPCODE` (关系类型代码), `S_INFO_EFFECTIVE_DT` (生效日期)

## 中国债券申万行业分类（不建议使用）

- **英文表名**: `CBondSWIndustriesClass`
- **更新频率**: day
- **全量产品**: 否

## 全球行业板块(废弃)

- **英文表名**: `GICSCode`
- **更新频率**: day
- **全量产品**: 是

## 类型编码表

- **英文表名**: `AShareTypeCode`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录类型字段数值、名称间的映射关系
- **业务主键**: `OBJECT_ID` (对象ID)

## 品种业务代码和简称

- **英文表名**: `TB_OBJECT_0014`
- **更新频率**: nan
- **全量产品**: 否

## 证券基本资料(Wind海外数据标准)

- **英文表名**: `GB_OBJECT_1001`
- **更新频率**: nan
- **全量产品**: 否

## Wind标准证券代码表

- **英文表名**: `TB_OBJECT_0001`
- **更新频率**: nan
- **全量产品**: 否

## 全球交易所信息表

- **英文表名**: `TB_OBJECT_0002`
- **更新频率**: nan
- **全量产品**: 否

## 沪深交易所交易日

- **英文表名**: `TB_OBJECT_1010`
- **更新频率**: nan
- **全量产品**: 否

## 证券

- **英文表名**: `TB_OBJECT_1090`
- **更新频率**: nan
- **全量产品**: 否

## 证券停牌信息

- **英文表名**: `TB_OBJECT_1674`
- **更新频率**: nan
- **全量产品**: 否

## 公司基本资料

- **英文表名**: `TB_OBJECT_1018`
- **更新频率**: nan
- **全量产品**: 否

## 板块

- **英文表名**: `TB_OBJECT_1022`
- **更新频率**: nan
- **全量产品**: 否

## 板块成份

- **英文表名**: `TB_OBJECT_1400`
- **更新频率**: nan
- **全量产品**: 否

## 证券和证券关系表

- **英文表名**: `TB_OBJECT_0018`
- **更新频率**: nan
- **全量产品**: 否

## 中介机构

- **英文表名**: `TB_OBJECT_1517`
- **更新频率**: nan
- **全量产品**: 否

## 分红

- **英文表名**: `TB_OBJECT_1093`
- **更新频率**: nan
- **全量产品**: 否

## 新股发行

- **英文表名**: `TB_OBJECT_1095`
- **更新频率**: nan
- **全量产品**: 否

## 询价基本资料

- **英文表名**: `TB_OBJECT_1660`
- **更新频率**: nan
- **全量产品**: 否

## 资产负债表

- **英文表名**: `TB_OBJECT_1040`
- **更新频率**: nan
- **全量产品**: 否

## 公布重要指标

- **英文表名**: `TB_OBJECT_1158`
- **更新频率**: nan
- **全量产品**: 否

## 财务衍生指标表

- **英文表名**: `TB_OBJECT_5034`
- **更新频率**: nan
- **全量产品**: 否

## 股本

- **英文表名**: `TB_OBJECT_1084`
- **更新频率**: nan
- **全量产品**: 否

## 股本2

- **英文表名**: `TB_OBJECT_1432`
- **更新频率**: nan
- **全量产品**: 否

## 自由流通股本

- **英文表名**: `TB_OBJECT_1931`
- **更新频率**: nan
- **全量产品**: 否

## 特别处理

- **英文表名**: `TB_OBJECT_1123`
- **更新频率**: nan
- **全量产品**: 否

## 股权分置方案

- **英文表名**: `TB_OBJECT_1673`
- **更新频率**: nan
- **全量产品**: 否

## 沪深交易所复权行情

- **英文表名**: `TB_OBJECT_1425`
- **更新频率**: nan
- **全量产品**: 否

## 资金流向表

- **英文表名**: `TB_OBJECT_5046`
- **更新频率**: nan
- **全量产品**: 否

## 香港和新加坡及海外中资股行情(Wind标准)

- **英文表名**: `GB_OBJECT_1038`
- **更新频率**: nan
- **全量产品**: 否

## 债券基本资料

- **英文表名**: `TB_OBJECT_1429`
- **更新频率**: nan
- **全量产品**: 否

## 浮息债票面利率

- **英文表名**: `TB_OBJECT_1430`
- **更新频率**: nan
- **全量产品**: 否

## 债券份额变动

- **英文表名**: `TB_OBJECT_1640`
- **更新频率**: nan
- **全量产品**: 否

## 浮息债基础利率属性

- **英文表名**: `TB_OBJECT_1641`
- **更新频率**: nan
- **全量产品**: 否

## 债券现金流表

- **英文表名**: `TB_OBJECT_1703`
- **更新频率**: nan
- **全量产品**: 否

## 非可转债特殊条款

- **英文表名**: `TB_OBJECT_1705`
- **更新频率**: nan
- **全量产品**: 否

## 债券赎回条款执行说明

- **英文表名**: `TB_OBJECT_1707`
- **更新频率**: nan
- **全量产品**: 否

## 债券回售条款执行说明

- **英文表名**: `TB_OBJECT_1708`
- **更新频率**: nan
- **全量产品**: 否

## 资产支持证券基本资料

- **英文表名**: `ABSDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录资产支持证券的基本资料
- **业务主键**: `ABS_ID` (项目ID)

## 债券本金提前偿还明细

- **英文表名**: `TB_OBJECT_1932`
- **更新频率**: nan
- **全量产品**: 否

## 债券调换条款执行说明

- **英文表名**: `TB_OBJECT_2075`
- **更新频率**: nan
- **全量产品**: 否

## 债券担保物明细

- **英文表名**: `TB_OBJECT_2080`
- **更新频率**: nan
- **全量产品**: 否

## 含权债实际利率

- **英文表名**: `TB_OBJECT_1447`
- **更新频率**: nan
- **全量产品**: 否

## 证券持有人

- **英文表名**: `TB_OBJECT_1450`
- **更新频率**: nan
- **全量产品**: 否

## 债券行情(全价)

- **英文表名**: `TB_OBJECT_1448`
- **更新频率**: nan
- **全量产品**: 否

## 债券行情(净价)

- **英文表名**: `TB_OBJECT_1621`
- **更新频率**: nan
- **全量产品**: 否

## 银行间债券市场现券行情

- **英文表名**: `CFETSEODPrice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录银行间债券市场现券品种的日行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 债券远期交易行情

- **英文表名**: `TB_OBJECT_1767`
- **更新频率**: nan
- **全量产品**: 否

## 人民币利率互换统计

- **英文表名**: `TB_OBJECT_1833`
- **更新频率**: nan
- **全量产品**: 否

## 沪深交易所行情

- **英文表名**: `TB_OBJECT_1120`
- **更新频率**: nan
- **全量产品**: 否

## 债券招投标发行资料

- **英文表名**: `TB_OBJECT_1710`
- **更新频率**: nan
- **全量产品**: 否

## 主体信用评级

- **英文表名**: `TB_OBJECT_1734`
- **更新频率**: nan
- **全量产品**: 否

## 债券信用评级

- **英文表名**: `TB_OBJECT_1735`
- **更新频率**: nan
- **全量产品**: 否

## [内部]信用评估机构

- **英文表名**: `TB_OBJECT_1738`
- **更新频率**: nan
- **全量产品**: 否

## 回购标准券折算率

- **英文表名**: `CBondConversionRatio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录交易所公布的有回购品种的国债、企债折算成标准券的比例
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `B_CVN_STARTDATE` (开始适用日)

## 银行间债券市场回购行情

- **英文表名**: `TB_OBJECT_1343`
- **更新频率**: nan
- **全量产品**: 否

## 各国交易日

- **英文表名**: `TB_OBJECT_3500`
- **更新频率**: nan
- **全量产品**: 否

## 中债登债券估值数据

- **英文表名**: `TB_OBJECT_1804`
- **更新频率**: nan
- **全量产品**: 否

## 中债登收益率曲线数据

- **英文表名**: `TB_OBJECT_1805`
- **更新频率**: nan
- **全量产品**: 否

## 中证债券估值数据

- **英文表名**: `TB_OBJECT_1991`
- **更新频率**: nan
- **全量产品**: 否

## 基金基本资料和发行

- **英文表名**: `TB_OBJECT_1099`
- **更新频率**: nan
- **全量产品**: 否

## 基金净值

- **英文表名**: `TB_OBJECT_1101`
- **更新频率**: nan
- **全量产品**: 否

## 货币市场基金收益

- **英文表名**: `TB_OBJECT_1449`
- **更新频率**: nan
- **全量产品**: 否

## 基金投资组合持股(债)明细

- **英文表名**: `TB_OBJECT_1102`
- **更新频率**: nan
- **全量产品**: 否

## 基金投资组合重大变动

- **英文表名**: `TB_OBJECT_1532`
- **更新频率**: nan
- **全量产品**: 否

## 基金分红

- **英文表名**: `TB_OBJECT_1245`
- **更新频率**: nan
- **全量产品**: 否

## 基金份额

- **英文表名**: `TB_OBJECT_1115`
- **更新频率**: nan
- **全量产品**: 否

## 基金申购与赎回情况

- **英文表名**: `TB_OBJECT_1495`
- **更新频率**: nan
- **全量产品**: 否

## QDII基金基本资料

- **英文表名**: `TB_OBJECT_1877`
- **更新频率**: nan
- **全量产品**: 否

## 理财产品基本资料

- **英文表名**: `TB_OBJECT_3552`
- **更新频率**: nan
- **全量产品**: 否

## 信托产品基本资料

- **英文表名**: `TB_OBJECT_3554`
- **更新频率**: nan
- **全量产品**: 否

## 集合理财基本资料

- **英文表名**: `TB_OBJECT_1744`
- **更新频率**: nan
- **全量产品**: 否

## 市场指数行情

- **英文表名**: `TB_OBJECT_1288`
- **更新频率**: nan
- **全量产品**: 否

## 指数权重

- **英文表名**: `TB_OBJECT_1807`
- **更新频率**: nan
- **全量产品**: 否

## 申万行业成份明细

- **英文表名**: `TB_OBJECT_1476`
- **更新频率**: nan
- **全量产品**: 否

## Wind行业成份明细

- **英文表名**: `TB_OBJECT_1576`
- **更新频率**: nan
- **全量产品**: 否

## Wind指数成份明细

- **英文表名**: `TB_OBJECT_1619`
- **更新频率**: nan
- **全量产品**: 否

## 法定存款利率

- **英文表名**: `TB_OBJECT_1255`
- **更新频率**: nan
- **全量产品**: 否

## 沪深市场总体指标(月)

- **英文表名**: `AShareMarketOverallindex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深交易所每月各项总体指标值及变动幅度
- **业务主键**: `MONTH1` (月份), `EXCHANGE` (交易所)

## 个人代码表

- **英文表名**: `TB_OBJECT_1014`
- **更新频率**: nan
- **全量产品**: 否

## 券商代码表

- **英文表名**: `TB_OBJECT_1020`
- **更新频率**: nan
- **全量产品**: 否

## 中介机构代码表

- **英文表名**: `TB_OBJECT_1021`
- **更新频率**: nan
- **全量产品**: 否

## 证券类型代码表

- **英文表名**: `TB_OBJECT_1024`
- **更新频率**: nan
- **全量产品**: 否
