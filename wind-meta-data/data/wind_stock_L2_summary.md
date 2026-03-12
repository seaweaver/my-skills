# Wind股票知识库 - 摘要

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

## 中国A股基本资料

- **英文表名**: `AShareDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股代码、上市日期、上市板等基础信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国A股公司简介

- **英文表名**: `AShareIntroduction`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司的名称、注册地址、注册资本等公司基础信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国A股Wind行业分类

- **英文表名**: `AShareIndustriesClass`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司所属wind行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `WIND_IND_CODE` (Wind行业代码), `ENTRY_DT` (纳入日期)

## 中国A股证监会新版行业分类

- **英文表名**: `AShareSECNIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司所属新版证监会行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SEC_IND_CODE` (证监会行业代码), `ENTRY_DT` (纳入日期)

## 中国A股证监会行业分类

- **英文表名**: `AShareSECIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司所属旧版证监会行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SEC_IND_CODE` (证监会行业代码), `ENTRY_DT` (纳入日期)

## 中国A股国证行业分类

- **英文表名**: `AShareCNIIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司所属国证行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SEC_IND_CODE` (国证行业代码), `ENTRY_DT` (纳入日期)

## 中国A股国民经济行业分类

- **英文表名**: `AShareNEIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司所属国民经济行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `NE_IND_CODE` (国民经济行业代码), `ENTRY_DT` (纳入日期)

## 中国A股上证所行业分类

- **英文表名**: `AShareSSEIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司所属上证所行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SSE_IND_CODE` (上证所行业代码), `ENTRY_DT` (纳入日期)

## 中国A股长江证券行业分类

- **英文表名**: `AShareCJZQIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国A股长江证券行业分类信息，包括wind代码、行业代码、剔除日期等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SEC_IND_CODE` (长江证券行业代码), `ENTRY_DT` (纳入日期)

## 中国A股企业所有制板块

- **英文表名**: `AShareOwnership`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司企业所有制情况，如国有、民营等
- **业务主键**: `S_INFO_COMPCODE` (公司id), `WIND_SEC_CODE` (板块代码), `ENTRY_DT` (纳入日期)

## 中国A股企业地域板块

- **英文表名**: `AShareRegional`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司注册省份、城市
- **业务主键**: `S_INFO_COMPCODE` (公司id), `WIND_SEC_CODE` (板块代码), `ENTRY_DT` (纳入日期)

## 中国A股证券曾用名

- **英文表名**: `ASharePreviousName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股名称历次更名情况，包括特别处理更名
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `BEGINDATE` (起始日期)

## 中国A股证券曾用英文名

- **英文表名**: `ASharePreviousENName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股英文名称历次更名信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期)

## 中国A股公司曾用名

- **英文表名**: `CompanyPreviousName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司历次更名信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期)

## 中国A股Wind概念板块

- **英文表名**: `AShareConseption`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股Wind概念板块
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `WIND_SEC_CODE` (Wind概念板块代码), `ENTRY_DT` (纳入日期)

## 中国A股科创板上市概念板块

- **英文表名**: `AShareSTIBConceptualPlate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录科创板上市概念板块信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `WIND_SEC_CODE` (Wind概念板块代码), `ENTRY_DT` (纳入日期)

## 中国A股科创板所属新兴产业分类

- **英文表名**: `AShareSTIBEmergingIndustries`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录科创板公司所属新兴产业信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `WIND_SEC_CODE` (Wind概念板块代码), `ENTRY_DT` (纳入日期)

## 中国A股科创板股份权益概念

- **英文表名**: `AShareSTIBInterest`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录科创板公司股份权益信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_INDUSTRYCODE` (板块代码)

## 中国A股IPO类型

- **英文表名**: `AShareIPOClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股IPO公司采用的发行制度，包括注册制、核准制、审批制等
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_TYPECODE` (分类代码), `ENTRY_DT` (纳入日期)

## 沪股通成分股

- **英文表名**: `SHSCMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪股通成份股进出信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ENTRY_DT` (纳入日期)

## 深股通成分股

- **英文表名**: `SZSCMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录深股通成份股进出信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ENTRY_DT` (纳入日期)

## 深股通只可卖出证券

- **英文表名**: `SZSCSELLMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录深股通只能卖出的股票列表
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ENTRY_DT` (纳入日期)

## 沪股通只可卖出证券

- **英文表名**: `SHSCSELLMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪股通只能卖出的股票列表
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ENTRY_DT` (纳入日期)

## 中国A股路演推介信息

- **英文表名**: `AShareIPORoadshow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国A股路演推介信息，包括路演类型、路演方式、路演日期等。
- **业务主键**: `COMP_ID` (公司ID), `ROADSHOW_TYPE` (路演类型代码), `ROADSHOW_MODE` (路演方式代码), `ROADSHOW_DATE` (路演日期), `PLACE` (路演地点)

## 中国A股日行情

- **英文表名**: `AShareEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深交易所自营业以来A股日行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国A股交易日历

- **英文表名**: `AShareCalendar`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股沪深交易所具体交易日期信息
- **业务主键**: `TRADE_DAYS` (交易日), `S_INFO_EXCHMARKET` (交易所英文简称)

## 中国A股停复牌信息

- **英文表名**: `AShareTradingSuspension`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股停牌、复牌信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_DQ_SUSPENDDATE` (停牌日期), `S_DQ_SUSPENDTYPE` (停牌类型代码)

## 中国A股除权除息记录

- **英文表名**: `AShareEXRightDividendRecord`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股发行、配股、增发、分红等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EX_DATE` (除权除息日)

## 中国A股交易异动

- **英文表名**: `AShareStrangeTradedetail`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股交易异常或深交所权证而披露的交易公开信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (异动类型), `END_DT` (截止日)

## 中国A股证券交易异动营业部买卖信息

- **英文表名**: `AShareStrangeTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股交易异动的证券及证券公司交易席位的买卖信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_STRANGE_BGDATE` (交易起始日), `S_STRANGE_ENDDATE` (交易截止日), `S_STRANGE_TRADERNAME` (营业部名称), `S_STRANGE_TRADERAMOUNT` (营业部买卖金额)

## 中国A股大宗交易数据

- **英文表名**: `AShareBlockTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股大宗交易具体信息

## 沪深市场总体指标(月)

- **英文表名**: `AShareMarketOverallindex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深交易所每月各项总体指标值及变动幅度
- **业务主键**: `MONTH1` (月份), `EXCHANGE` (交易所)

## 中国A股沪深交易所盘后行情

- **英文表名**: `AShareAfterEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深交易所盘后交易行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股盘后盘口指标

- **英文表名**: `AShareAfterEODPIndicators`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `INDICATOR_CODE` (指标代码)

## 中国A股日收益率

- **英文表名**: `AShareYield`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股每天的收益率、换手率、成交金额等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股日行情估值指标

- **英文表名**: `AShareEODDerivativeIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股每个交易日的当日总市值、PE、PB、当日总股本等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国A股资金流向数据

- **英文表名**: `AShareMoneyFlow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录根据level-2数据计算的A股资金流向数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股成交量技术指标

- **英文表名**: `AShareTechIndicators`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股成交量技术指标，如量比、成交量简单移动平均
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股强弱与趋向技术指标(后复权)

- **英文表名**: `AshareintensitytrendADJ`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股强弱、趋向指标，如MA5、MA10、MA20、MA30
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股强弱与趋向技术指标(不复权)

- **英文表名**: `Ashareintensitytrend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股强弱、趋向指标，如MA5、MA10、MA20、MA30
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股能量、量价与压力支撑技术指标(复权)

- **英文表名**: `AShareEnergyindexADJ`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股能量、量价与压力支撑技术指标，如BOLL布林带等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股能量、量价与压力支撑技术指标(不复权)

- **英文表名**: `AShareEnergyindex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股能量、量价与压力支撑技术指标，如BOLL布林带等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股摆动与反趋向技术指标(后复权)

- **英文表名**: `AShareswingReversetrendADJ`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股股票摆动、反趋向、超买超卖技术指标，如RC变化率等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股摆动与反趋向技术指标(不复权)

- **英文表名**: `AShareswingReversetrend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股股票摆动、反趋向、超买超卖技术指标，如RC变化率等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股融资融券交易明细

- **英文表名**: `AShareMarginTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股融资融券交易明细数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国A股融资融券交易汇总

- **英文表名**: `AShareMarginTradeSum`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深交易所公布的融资融券交易统计数据
- **业务主键**: `TRADE_DT` (日期), `S_MARSUM_EXCHMARKET` (交易所英文简称)

## 中国A股融资融券标的及担保物

- **英文表名**: `AShareMarginSubject`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股融资融券的保证金比例、折算率等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_MARGIN_SHARETYPE` (融资融券相关证券类型代码), `S_MARGIN_EFFECTDATE` (生效日), `S_MARGIN_RATEEFFECTDATE` (保证金比例或折算率生效日)

## 中国A股融资融券费率

- **英文表名**: `AShareMarginShortFeeRate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股融资融券的具体费率信息
- **业务主键**: `PUBLISHER_ID` (发布方ID), `ITEM_CODE` (项目类别代码), `EFFECTIVE_DATE` (生效日)

## 中国A股首次公开发行数据

- **英文表名**: `AShareIPO`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股首次发行记录，含异种股票增发记录（如原先发行B股的公司增发A股）
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国A股发行中介机构

- **英文表名**: `AShareAgency`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股发行所参与的中介结构，如会计师事务所、财务顾问、律师事务所等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_RELATION_TYPCODE` (关系类型代码), `S_AGENCY_NAMEID` (机构名称ID)

## 中国A股发行主承销商

- **英文表名**: `AShareLeadUnderwriter`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股发行所参与的保荐机构

## IPO初步询价明细

- **英文表名**: `IPOInquiryDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股IPO询价对象、配售对象、申报价格、配售数量等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `INQUIRER` (询价对象名称), `ISSUETARGET` (配售对象名称), `DEDAREDPRICE` (申报价格(元/股))

## 中国A股网下配售机构获配明细

- **英文表名**: `ASharePlacementDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股战略投资者和A类机构投资者（基金）在历次发行和增发中获配数量和冻结期限
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_HOLDER_NAME` (股东名称), `TRADE_DT` (截止日期), `LOCKMONTH` (锁定期(月))

## 中国A股网下配售机构获配统计

- **英文表名**: `ASharePlacementInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录按投资者类型统计的A股发行网下中签率、配售数量
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `PCT_CHANGE_1D` (投资者类型代码)

## 中国A股股本

- **英文表名**: `AShareCapitalization`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股各种类型股份的变动记录及变动原因
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期), `CHANGE_DT1` (变动日期1), `IS_VALID` (是否有效)

## 中国A股股票发行数量

- **英文表名**: `AShareIPOAmount`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股发行股份数、限售股数、无限售股份数等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DATE` (变动日)

## 中国A股自由流通股本

- **英文表名**: `AShareFreeFloat`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股自由流通股本，此数据为wind计算
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT1` (变动日期(上市日))

## 中国A股分红

- **英文表名**: `AShareDividend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股分红的全程记录，从董事会预案开始，历经股东大会通过（或否决）、实施、缴款，直到红股上市流通
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EQY_RECORD_DT` (股权登记日), `S_DIV_PRELANDATE` (预案公告日), `S_DIV_BASESHARE` (基准股本(万股)), `ANN_DT` (最新公告日期), `REPORT_PERIOD` (分红年度), `S_DIV_OBJECT` (分红对象)

## 中国A股配股

- **英文表名**: `AShareRightIssue`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股配股的全程记录，从董事会预案开始，历经股东大会通过（或否决）、获准（或否决）、实施、缴款，直到配股上市流通
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_RIGHTSISSUE_YEAR` (配股年度)

## 中国A股增发

- **英文表名**: `AShareSEO`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股增发的全程记录，从董事会预案开始，历经股东大会通过（或否决）、获准（或否决）、实施、缴款，直到增发股份上市流通
- **业务主键**: `OBJECT_ID` (对象ID)

## 中国A股回购

- **英文表名**: `AshareStockRepo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股回购数量、回购金额、股份注销等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EVENT_ID` (事件ID), `ANN_DT` (公告日期)

## 中国A股限售股流通日历

- **英文表名**: `AShareFreeFloatCalendar`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股限售股上市日期、上市流通股份数量
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_LISTDATE` (限售股上市日期)

## 中国A股限售股解禁公司明细

- **英文表名**: `AShareCompRestricted`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股限售股流通日期、可流通数量等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_LISTDATE` (可流通日期), `S_HOLDER_NAME` (股东名称), `S_SHARE_LSTTYPECODE` (股份类型代码), `S_SHARE_LST` (可流通数量(股)), `S_SHARE_PLACEMENT_ENDDT` (配售截止日期), `ANN_DT` (公告日期)

## 中国A股股权分置除权

- **英文表名**: `AShareDivisionElimination`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股股权分置对价因子、复权因子、实施复牌日等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国A股股权分置方案

- **英文表名**: `AShareEquityDivision`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股股权分置信息
- **业务主键**: `COMP_ID` (公司id), `PREPLANDATE` (董事会预案公告日), `IS_NEWPRO` (是否最新方案)

## 中国A股事件日期信息

- **英文表名**: `AShareEventdateinformation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股事件发生信息，如发生日期、事件类型等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EVENT_TYPE` (事件类型编号), `OCCURRENCE_DATE` (发生日期), `S_INFO_CODE` (交易代码), `LANGUAGE1` (语言), `SRC_OBJID` (业务ID)

## 中国A股募集资金用途

- **英文表名**: `AShareFundUsing`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股发行、增发、配股中募集资金的具体投向

## 中国A股发行审核一览

- **英文表名**: `AShareIssueCommAudit`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股IPO发行审核信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_IC_YEAR` (年度), `S_IC_SESSIONTIMES` (会议届次)

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

## 中国A股科创板公司股东表决权

- **英文表名**: `AShareSTIBHolderVote`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录科创板公司股东表决权信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `DEADLINE` (截止日期), `S_HOLDER_NAME` (股东名称), `S_HOLDER_LSTTYPECODE` (股份类型)

## 中国A股新股中签数据

- **英文表名**: `AShareWinning`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股IPO时的中签数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期), `LAST_DIGIT` (末尾位数)

## 中国A股科创板战投出借信息

- **英文表名**: `AShareSTIBInvestmentIending`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录科创板公司战略投资出借信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (交易日期)

## 中国A股行政许可事项进度表

- **英文表名**: `AShareAdmPermitSchedule`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司申请资质的行政许可事项进度信息
- **业务主键**: `COMP_ID` (公司ID), `ENDDATE` (截止日期), `TYPE_NAME` (申请事项), `TYPE_CODE` (审核类型代码)

## 非公开发行股票审核申报企业情况

- **英文表名**: `NOPUBLICSTOCKCompRFA`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录非公开发行股票审核申报企业数据，包括保荐机构、申请事项、进度等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SCH_CODE` (进度类型代码), `ST_DATE` (状态起始日期)

## 中国A股资产负债表

- **英文表名**: `AShareBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的资产负债表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国A股利润表

- **英文表名**: `AShareIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的利润表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `S_INFO_COMPCODE` (公司ID)

## 中国A股现金流量表

- **英文表名**: `AShareCashFlow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的现金流量表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `S_INFO_COMPCODE` (公司ID)

## 中国A股业绩快报

- **英文表名**: `AShareProfitExpress`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司业绩快报中披露的相关财务数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期)

## 中国A股业绩预告

- **英文表名**: `AShareProfitNotice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司在财务报告公布前发布的业绩预告
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_PROFITNOTICE_DATE` (公告日期), `S_PROFITNOTICE_PERIOD` (报告期)

## 中国券商月报

- **英文表名**: `AShareMonthlyReportsofBrokers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录证券公司月度披露的营业收入、净利润、股权权益等数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPECODE` (报表类型代码)

## 中国A股定期报告披露日期

- **英文表名**: `AShareIssuingDatePredict`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务报告的预计披露日期
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期)

## 中国A股审计意见

- **英文表名**: `AShareAuditOpinion`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司历次财务报告（如经审计）的审计机构、审计费用及审计结果
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期)

## 中国A股公司会计变更

- **英文表名**: `AShareAccountingChange`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司会计科目变更事项及影响金额
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `S_CHANGE_ITEMCODE` (变更项目代码), `BE_AFFECTED_ITEMCODE` (受影响的报表项目名称), `BE_AFFECTED_REPORT_PERIOD` (受影响的报告期), `BE_AFFECTED_REPORT_TYPE` (受影响的报表类型)

## 中国A股公布重要财务指标

- **英文表名**: `AShareANNFinancialIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司在定期报告中公布的财务指标和分配预案
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 中国A股财务指标

- **英文表名**: `AShareFinancialIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的财务衍生数据，如每股营收、每股净资产、每股收益等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期)

## 中国A股财务衍生指标表

- **英文表名**: `AShareFinancialderivative`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司衍生财务指标数据
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `BEGINDATE` (起始日期), `ENDDATE` (截止日期), `STATEMENT_TYPE` (报表类型)

## 中国A股WIND计算调整后财务指标

- **英文表名**: `AShareReportperiodindex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司因发行、分配、吸收合并等原因导致部分财务指标发生变动，为弥补财务报表的时滞性，Wind资讯即时计算出调整后财务指标
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `END_DATE` (截止日期)

## 中国A股TTM与MRQ

- **英文表名**: `AShareTTMAndMRQ`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股TTM与MRQ指标，本表指标无报告期参数，不区分新旧准则，全部用新准则数据计算
- **业务主键**: `S_INFO_WINDCODE` (万得代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国A股TTM指标历史数据

- **英文表名**: `AShareTTMHis`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的营业总收入、归属母公司净利润等几个重要财务指标各报告期的TTM数据
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (截止日期), `STATEMENT_TYPE` (报表类型)

## 中国A股银行专用指标

- **英文表名**: `AShareBankIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股银行类公司公布的一些特殊的财务指标
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

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

## 中国A股保险专用指标

- **英文表名**: `AShareInsuranceIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股保险类上市公司的一些特殊的财务指标
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `REPORT_TYPE` (报告类型代码)

## 中国A股券商专用指标

- **英文表名**: `AShareIBrokerIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股证券类上市公司的一些特殊的财务指标
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国A股金融机构经营分部业务数据

- **英文表名**: `AShareFinSegmentinfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股金融类公司分地区、分业务的各项目的经营数据
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码), `CLASS_CODE` (分部类别代码), `SUBJECT_CODE` (科目代码)

## 中国A股审计事项描述

- **英文表名**: `AShareAuditDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司审计报告中公布的审计事项
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `AUDIT_PROJECT_TYPE` (审计项目类型代码), `AUDIT_MATTERS_TYPE` (关键审计事项类型)

## 中国A股主营业务构成

- **英文表名**: `AShareSalesSegment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司按行业、项目、地区、产品分类的主营收入、主营利润、主营成本的金额及比例
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `S_SEGMENT_ITEM` (主营业务项目), `SUBJECT_CODE` (科目ID)

## 中国A股财务费用明细

- **英文表名**: `AShareFinancialExpense`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务费用明细信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPECODE` (报表类型代码)

## 中国A股应收账款大股东欠款

- **英文表名**: `AshareAccountsReceivable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司所有持股5％以上大股东的欠款金额
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `DEBTOR_NAME` (债务人名称)

## 中国A股应收账款账龄结构

- **英文表名**: `AshareAgingstructure`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司不同期限每类应收账款的金额及其计提数
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `STATEMENT_TYPE_NAME` (报表类型名称), `AGING` (帐龄), `REPORT_PERIOD` (报告期)

## 中国A股资产减值准备明细表

- **英文表名**: `AShareDevaluationPreparation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司八项计提(2001年中报以后整体公布)，期末数
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `STATEMENT_TYPE` (报表类型), `REPORT_PERIOD` (报告期)

## 中国A股担保统计

- **英文表名**: `AshareGuaranteestatistics`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司在定期报告中公布的担保合计数据
- **业务主键**: `S_INFO_COMPCODE` (公司id), `DEADLINE` (截止日期)

## 中国A股存货明细

- **英文表名**: `AshareInventorydetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司每一类存货的金额及相应计提数
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `INV_OBJECT` (项目)

## 中国A股主要其它应收款明细

- **英文表名**: `AshareMajorreceivables`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司主要其它应收款明细
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `DEBTOR_NAME` (债务人名称), `ARREARS` (金额), `DELAYTIME` (拖欠时间), `DELAYREASON` (拖欠原因)

## 中国A股公司货币资金明细

- **英文表名**: `AshareMonetaryfunds`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司货币资金明细数据
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期)

## 中国A股非经常性损益

- **英文表名**: `Asharenonprofitloss`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司新准则下的报告期非经常性损益明细
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国A股其它应收款帐龄结构

- **英文表名**: `AshareOtherAccountsreceivable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司其它应收款帐龄结构
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `AGING` (帐龄)

## 中国A股其它应收款大股东欠款

- **英文表名**: `AshareOtherreceivables`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司其它应收款大股东欠款
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `DEBTOR_NAME` (债务人名称)

## 中国A股坏帐准备提取比例

- **英文表名**: `AshareProvisionbaddebts`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司应收帐款和其他应收款的坏帐提取比例
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `AGING` (帐龄), `EXTRACTION_RATIO` (提取比例)

## 中国A股应交税费明细

- **英文表名**: `AshareTaxespayable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司应交税费明细信息（原名应交税金明细表，2007年半年报起改为应交税费明细表。核算内容除原应交税金科目外，还包括旧准则下的其他应交款科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国A股公司税率明细

- **英文表名**: `AShareTaxrate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司每年的所得税税率水平
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `BEGIN_MON` (起始月份)

## 中国A股财务附注明细

- **英文表名**: `FinNotesDetail`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注的明细数据，如坏账损失、商誉减值损失等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型代码)

## 中国A股应收账款余额前五名

- **英文表名**: `Top5ByAccountsReceivable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司应收账款前五名的公司名称、欠款金额及拖欠原因
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `S_INFO_COMPNAME` (债务人名称), `AMOUNT` (金额（元）)

## 中国A股长期借款前五名

- **英文表名**: `Top5ByLongTermBorrowing`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司长期借款前五名公司明细数据
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `S_INFO_COMPNAME` (单位名称), `TYPECODE` (往来资金类别代码)

## 中国A股营业收入前五名

- **英文表名**: `Top5ByOperatingIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司往来资金前五名公司明细数据
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `S_INFO_COMPNAME` (单位名称), `INTERCHANGE_CODE` (往来资金类别代码)

## 中国A股关联方债权债务往来

- **英文表名**: `AShareRelatedclaimsdebts`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司关联债权债务往来
- **业务主键**: `S_INFO_COMPCODE` (公司id), `ASSOCIATED_NAME` (关联方名称), `REPORT_PERIOD` (报告期)

## 中国A股贷款明细

- **英文表名**: `AShareLoandetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司贷款明细信息
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `LOAN_TYPE` (贷款类型)

## 中国A股政府补助明细

- **英文表名**: `AShareGovernmentgrants`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司获得政府补助的明细信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `ITEM_NAME` (项目)

## 中国A股关联方往来及委托理财合计

- **英文表名**: `AShareTrustinvestmentTOT`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司在定期报告中披露的重要事项
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期)

## 财务附注项目类别配置表

- **英文表名**: `FinancialNoteCategory`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录财务附注辅助表中的项目类别
- **业务主键**: `S_SEGMENT_ITEMCODE` (项目类别代码)

## 中国A股财务附注-利率风险

- **英文表名**: `AShareInterestRateRisk`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司利率风险明细信息
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--资本公积

- **英文表名**: `AShareCapitalSurplus`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的资本公积科目

## 中国A股财务附注--在建工程

- **英文表名**: `AShareEngineering`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的在建工程科目

## 中国A股财务附注--预付账款

- **英文表名**: `AShareAdvancePayment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的预付账款科目

## 中国A股财务附注--应收票据

- **英文表名**: `AShareNotesReceivable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的应收票据科目

## 中国A股财务附注--应付职工薪酬

- **英文表名**: `AShareCompensationPayable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的应付职工薪酬科目

## 中国A股财务附注--应付账款

- **英文表名**: `FinNotesAccountsPayable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的应付账款科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--一年内到期的非流动负债

- **英文表名**: `AShareNonCurrentLiabilities1Y`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的一年内到期的非流动负债科目

## 中国A股财务附注--研发支出

- **英文表名**: `AShareRDexpenditure`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的研发支出科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--投资性房地产

- **英文表名**: `AShareInvestmentRealEstate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的投资性房地产科目

## 中国A股财务附注--其他流动资产

- **英文表名**: `AShareOtherCurrentAssets`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他流动资产科目

## 中国A股财务附注--其他流动负债

- **英文表名**: `AShareOtherCurrentLiabilities`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他流动负债科目

## 中国A股财务附注--预收款项

- **英文表名**: `AShareAdvanceReceipt`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的预收款项科目

## 中国A股财务附注--应收利息

- **英文表名**: `AShareInterestReceivable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的应收利息科目

## 中国A股财务附注--应付票据

- **英文表名**: `AShareNotesPayable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的应付票据科目

## 中国A股财务附注--所得税

- **英文表名**: `AShareIncomeTax`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的所得税科目

## 中国A股财务附注--其他非流动资产

- **英文表名**: `AShareOtherNoncurrentAssets`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他非流动资产科目

## 中国A股财务附注--递延所得税负债

- **英文表名**: `AShareDeferredTaxLiability`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的递延所得税负债科目

## 中国A股财务附注--期限划分下的各类逾期贷款

- **英文表名**: `AShareKindsOveLoansTerm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的期限划分下的各类逾期贷款科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--固定资产

- **英文表名**: `AShareFixedAssets`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的固定资产科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--管理费用明细

- **英文表名**: `AShareManagementExpense`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的管理费用明细科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--销售费用明细

- **英文表名**: `AShareSaleExpense`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的销售费用明细科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--货币资金(按项目)

- **英文表名**: `AshareMonetaryfundOfProj`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的货币资金(按项目)科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--无形资产

- **英文表名**: `AShareIntangibleAssets`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的无形资产科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--投资收益

- **英文表名**: `AShareInvestmentIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的投资收益科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--商誉

- **英文表名**: `AShareGoodwill`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的商誉科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--融出证券合计

- **英文表名**: `AShareFinancialSecurities`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的融出证券合计科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--买入返售金融资产

- **英文表名**: `AshareBuyRESaleFINAssets`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的买入返售金融资产科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--流动性风险

- **英文表名**: `AShareLiquidityRisk`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的流动性风险科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--财务费用

- **英文表名**: `AShareFinancialEXP`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的财务费用科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--拆入资金

- **英文表名**: `AShareLoansOTHBanks`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的拆入资金科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--存货跌价准备

- **英文表名**: `AShareINVEFallPriceRES`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的存货跌价准备科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--递延收益政府补助

- **英文表名**: `AShareGovernmentSubsidyDEFIN`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的递延收益政府补助科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--递延所得税资产

- **英文表名**: `AShareDeferredTaxAssets`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的递延所得税资产科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--短期借款

- **英文表名**: `AShareSTLoan`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的短期借款科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--公允价值变动收益

- **英文表名**: `AShareFairValueChange`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的公允价值变动收益科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--敏感性分析

- **英文表名**: `AShareSensitAnalysis`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的敏感性分析科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--内含价值变动分析

- **英文表名**: `AShareEMBValueChangeANAL`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的内含价值变动分析科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--内含价值评估结果

- **英文表名**: `AShareEMBValueASSESSResults`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的内含价值评估结果科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--其他非流动负债

- **英文表名**: `AShareOtherNoncurrentLIAB`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他非流动负债科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--其他收益

- **英文表名**: `AShareOtherincome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他收益科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--其他应付款

- **英文表名**: `AShareOtherPayables`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他应付款科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--其他综合收益

- **英文表名**: `AShareOtherCOMPREHIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他综合收益科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--商誉减值准备

- **英文表名**: `AShareGoodwillDEValue`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的商誉减值准备科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--所得税调整过程

- **英文表名**: `AShareIncomeTaxADJProc`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的所得税调整过程科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--未分配利润

- **英文表名**: `AShareUndistributedProfit`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的未分配利润科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--现金及存放中央银行款项

- **英文表名**: `AShareCashADepositsWithCB`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的现金及存放中央银行款项科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--研发费用

- **英文表名**: `AShareRDExpense`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的研发费用科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--盈余公积

- **英文表名**: `AShareSurplusReserve`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的盈余公积科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--营业收入和营业成本

- **英文表名**: `AShareOPERREVAndCOST`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的营业收入和营业成本科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--营业税金及附加

- **英文表名**: `AShareTaxSurcharge`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的营业税金及附加科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--营业外收入

- **英文表名**: `AShareNONOPERREV`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的营业外收入科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--营业外支出

- **英文表名**: `AShareNONOPEREXP`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的营业外支出科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--应付利息

- **英文表名**: `AShareINTPayable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的应付利息科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--长期待摊费用

- **英文表名**: `AShareLTPrepaidEXP`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的长期待摊费用科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--长期股权投资

- **英文表名**: `AShareLTEQYInvest`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的长期股权投资科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--长期借款

- **英文表名**: `AShareLTLoan`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的长期借款科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--长期应付款

- **英文表名**: `AShareLTPayables`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的长期应付款科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--总投资收益

- **英文表名**: `AShareTotalInvest`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的总投资收益科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--总资产减值损失

- **英文表名**: `AShareIMPAIRLossAssets`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的总资产减值损失科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--应交税费

- **英文表名**: `AShareTaxesPay`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的应交税费科目
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 主营及附注科目对应关系表

- **英文表名**: `AShareSalesSegmentMapping`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国A股主营及附注科目对应关系信息，包括主科目名称、子科目名称等。
- **业务主键**: `MAIN_ACCOUNTS_ID` (主科目ID), `SUB_ACCOUNTS_ID` (子科目ID)

## 中国A股财务附注--债权投资

- **英文表名**: `AShareDebtinvestment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的债权投资科目，提供合并报表数据。
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--其他债权投资

- **英文表名**: `AShareOtherdebtinvestment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他债权投资科目，提供合并报表数据。
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--其他权益工具投资

- **英文表名**: `AShareOthereqtyinstrtinvesmt`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的其他权益工具投资，提供合并报表数据。
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股财务附注--交易性金融资产

- **英文表名**: `AShareTradingfinancialassets`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司财务附注表中的交易性金融资产，提供合并报表数据。
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `ITEM_TYPE_CODE` (项目类别代码), `ANN_ITEM` (项目公布名称)

## 中国A股公司管理层成员

- **英文表名**: `AShareManagement`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司董、监、高成员的个人简历信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_MANAGER_NAME` (姓名), `S_INFO_MANAGER_STARTDATE` (任职日期), `S_INFO_MANAGER_POST` (职务)

## 中国A股公司管理层持股及报酬

- **英文表名**: `AShareManagementHoldReward`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司历次财务报告中公布的董监事会成员和高管成员的持股和报酬情况

## 中国A股员工人数变更

- **英文表名**: `AShareStaff`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司各报告期的员工人数
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `END_DT` (截止日期)

## 中国A股股权激励基本资料

- **英文表名**: `AShareIncDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股权激励的基础信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INC_SEQUENCE` (序号)

## 中国A股股权激励数量与价格

- **英文表名**: `AShareIncQuantityPrice`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股权激励的数量与价格
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INC_SEQUENCE` (序号)

## 中国A股股权激励期权行权比例

- **英文表名**: `AShareIncExercisePct`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司股权激励期权每年的行权比例及行权条件
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INC_SEQUENCE` (序号), `S_INC_EXECBATCH` (行权/归属期)

## 中国A股股权激励期权行权数量与价格

- **英文表名**: `AShareIncExecQtyPri`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股权激励期权行权明细数量、合计数量、行权价格

## 中国A股股权激励数量明细

- **英文表名**: `AShareIncQuantityDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股权激励期权的数量明细
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INC_SEQUENCE` (序号), `S_INC_NAME` (姓名), `S_INC_POST` (职位)

## 中国A股公司员工持股计划基本资料

- **英文表名**: `AShareEsopDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司员工持股计划的基本信息，关联上市公司ID、初始资金规模等
- **业务主键**: `EVENT_ID` (事件ID)

## 中国A股公司员工持股计划股票买卖情况

- **英文表名**: `AShareEsopTradingInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司员工持股计划的买卖情况，一般包含成交均价、成交数量等
- **业务主键**: `END_DT` (截止日期), `EVENT_ID` (事件ID)

## 中国A股员工构成

- **英文表名**: `AShareStaffStructure`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司人才级别的分类信息
- **业务主键**: `STAFF_TYPE_CODE` (人数类别代码), `END_DT` (截止日期), `ITEM_TYPE_CODE` (项目分类代码), `ITEM_NAME` (项目), `S_INFO_WINDCODE` (Wind代码)

## 中国A股公司扶贫情况统计

- **英文表名**: `ASharePovertyAlleviationData`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国A股公司扶贫情况统计信息，包括精准扶贫发生额、扶贫捐款发生额、精准贷款发生额等。
- **业务主键**: `S_INFO_COMPCODE` (公司id), `ANN_DT` (公告日期)

## 中国A股前十大股东

- **英文表名**: `AShareInsideHolder`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股东持有的份额数量、比例和性质
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_HOLDER_ENDDATE` (截止日期), `S_HOLDER_NAME` (股东名称), `S_HOLDER_QUANTITY` (持股数量), `S_HOLDER_ANAME` (公布股东名称)

## 中国A股流通股东

- **英文表名**: `AShareFloatHolder`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司前十位流通股东持有的份额数量、性质等

## 中国A股股权关系

- **英文表名**: `AShareEquityRelationships`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司前10名股东关联关系及前10名流通股东关联关系
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ENDDATE` (截止日期), `S_INFO_COMPNAME` (公司名称), `S_HOLDER_NAME` (股东名称)

## 中国A股股东户数

- **英文表名**: `AShareHolderNumber`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股东户数
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_HOLDER_ENDDATE` (截止日期)

## 中国A股内部人交易

- **英文表名**: `AShareInsiderTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司董事、监事、高级管理人员持有本公司股份变动情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `RELATED_MANAGER_NAME` (相关管理层姓名), `REPORTED_TRADER_NAME` (变动人姓名), `TRADE_DT` (变动日期), `RELATED_MANAGER_POST` (相关管理层职务)

## 中国A股重要股东增减持

- **英文表名**: `AShareMjrHolderTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司流通股票发生增持或减持
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRANSACT_ENDDATE` (变动截至日期), `HOLDER_NAME` (持有人), `TRANSACT_TYPE` (买卖方向)

## 中国A股股东拟增减持计划

- **英文表名**: `ASarePlanTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股东拟增减持计划
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (首次披露公告日), `HOLDER_NAME` (持有方名称), `TRANSACT_TYPE` (变动方向)

## 中国A股股权质押信息

- **英文表名**: `AShareEquityPledgeInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股东质押股权的信息

## 中国A股股票质押比例

- **英文表名**: `ASharePledgeproportion`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股单一股票质押的信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_ENDDATE` (截止日期)

## 中国A股股权冻结信息

- **英文表名**: `AShareEquFroInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股股票冻结信息

## 中国A股股权冻结质押情况(报告期)

- **英文表名**: `AEquFroPleInfoRepperend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股股票被股东质押或被冻结的数量
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `PRICE_DATE` (报告期), `F_NAV_ACCUMULATED` (股东名称)

## 中国A股机构持股衍生数据

- **英文表名**: `AShareinstHolderDerData`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股股东总持股数、持有流通A股数量
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `S_HOLDER_COMPCODE` (股东公司id)

## 中国A股股东增持计划

- **英文表名**: `AShareMajorHolderPlanHold`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司大股东增持计划，如增持触发价格、增持数量上下限等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_HOLDER_NAME` (股东名称), `S_PH_STARTDATE` (增持计划起始日期), `S_PH_ENDDATE` (增持计划截止日期), `S_PH_TRIGGERPRICE` (增持触发价格)

## 中国A股召开股东大会

- **英文表名**: `AShareholdersmeeting`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司预告股东大会的召开时间及审议事项
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期), `MEETING_DT` (会议日期), `MEETING_TYPE` (会议类型)

## 中国A股立案调查

- **英文表名**: `AShareRegInv`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司被证监会等监管机构立案调查的信息
- **业务主键**: `COMP_ID` (公司ID), `SUR_INSTITUTE` (调查机构), `STR_DATE` (开始日期)

## 中国A股特别处理

- **英文表名**: `AShareST`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股被特别处理的实施和撤销、暂停/恢复上市，以及退市记录及原因
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_TYPE_ST` (特别处理类型), `ENTRY_DT` (实施日期)

## 中国A股担保事件

- **英文表名**: `AShareGuarantee`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司及其控股子公司对外担保信息

## 中国A股诉讼事件

- **英文表名**: `AShareProsecution`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司作为原告或被告的涉案情况和案件审理、判决、执行、上诉及二审判决情况

## 中国A股违规事件

- **英文表名**: `AShareIllegality`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录各级主管部门公布的对A股公司违规行为的调查结果与处理决定
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DT` (公告日期), `SUBJECT` (违规主体), `PROCESSOR` (处理人)

## 中国A股要约收购

- **英文表名**: `AshareOfferforoffer`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司要约收购基本资料
- **业务主键**: `S_INFO_COMPCODE` (被要约收购公司id), `START_DATE` (要约起始日期), `CIRCULATION_STOCK_NUM` (预定收购流通股数量(万股))

## 中国A股关联交易

- **英文表名**: `AShareRalatedTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司与各种控制或非控制主体之间的详细交易记录

## 中国A股证券投资

- **英文表名**: `AShareCapitalOperation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司投资其他上市公司股票及基金

## 中国A股股东大会投票情况

- **英文表名**: `AShareholdersmeetingVotes`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股东大会投票信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DT` (公告日期), `MEETING_DT` (会议日期), `MOTION_TITLE` (议案标题)

## 中国A股控股参股公司经营情况

- **英文表名**: `AShareholdingoperate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司主要控股参股公司经营信息
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (截止日期), `S_CAPITALOPERATION_COMPANYNAME` (被参控公司名称)

## 中国A股运营事件

- **英文表名**: `AShareOperationEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司运营事件信息
- **业务主键**: `SEC_ID` (品种ID), `ANN_DATE` (公告日期), `EVENT_TYPE` (事件类型)

## 中国A股重大事件汇总

- **英文表名**: `AShareMajorEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司证券和公司各类事件
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_EVENT_CATEGORYCODE` (事件类型代码), `S_EVENT_HAPDATE` (发生日期), `S_EVENT_EXPDATE` (失效日期), `SEC_ID` (证券ID)

## 中国A股控股参股

- **英文表名**: `AShareCompanyHoldShares`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司参控其他公司的信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ENDDATE` (截止日期), `S_CAPITALOPERATION_COMPANYNAME` (被参控公司名称)

## 中国A股股东大会议案网络投票表决情况

- **英文表名**: `AShareInternetvoting`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司股东大会议案网络投票表决信息
- **业务主键**: `S_EVENT_ID` (会议事件ID), `S_EVENT_NUM` (议案序号)

## 中国A股重大重组事件

- **英文表名**: `AshareRestructuringEvents`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司重大重组事件信息，如交易标的、交易完成日期、评估价值等
- **业务主键**: `EVENT_ID` (并购事件ID)

## 中国A股股票置换

- **英文表名**: `AShareStockSwap`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司股份换为其他公司股份(换股前后流通股东持股数量有变化)
- **业务主键**: `TRANSFERER_WINDCODE` (换股方万得代码), `TARGETCOMP_NAME` (标的方简称), `ANN_DT` (最新公告日)

## 中国A股公司资本运作

- **英文表名**: `AShareCOCapitaloperation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司资本运作的情况，如融资进程、融资利率、融资金额等
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_EVENT_ID` (事件ID)

## 中国A股购买理财产品

- **英文表名**: `AShareCorporateFinance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司购买理财产品的信息
- **业务主键**: `EVENT_ID` (事件ID)

## 中国A股函件基本资料

- **英文表名**: `AShareCorpoLetDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国A股函件基本资料信息，包括发函日期、函件标题、函件类型等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `LETTERS_EVENT_ID` (函件事件ID)

## 中国A股函件内容表

- **英文表名**: `AShareCorpoLetInfor`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国A股公司函件内容信息，包括函件事件ID、问题文本、回答文本等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `COMP_ID` (公司ID), `LETTERS_EVENT_ID` (函件事件ID)

## 中国A股并购事件

- **英文表名**: `MergerEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司并购事件信息，如交易标的、交易完成日期、评估价值等
- **业务主键**: `EVENT_ID` (并购事件ID)

## 中国A股并购事件参与方

- **英文表名**: `MergerParticipant`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司并购事件各参与方
- **业务主键**: `EVENT_ID` (情报ID(或事件ID)), `PARTY_NAME` (参与方名称), `PARTY_ROLE_CODE` (参与方角色代码)

## 中国A股并购事件中介机构

- **英文表名**: `MergerAgency`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司并购事件的各家中介机构
- **业务主键**: `EVENT_ID` (并购事件ID), `S_INFO_COMPCODE` (中介机构公司ID), `AGENCY_TYPCODE` (中介机构类型代码)

## 中国A股关联事件

- **英文表名**: `RelatedEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司并购事件的关联事件信息
- **业务主键**: `EVENT_ID` (事件ID), `RELATED_ID` (关联事件ID)

## 中国A股前瞻性情报

- **英文表名**: `MergerIntelligence`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司交易事件的前瞻性情报
- **业务主键**: `INTELLIGENCE_ID` (情报ID), `ANN_DATE` (发布日期)

## 中国A股盈利承诺明细表

- **英文表名**: `CommitProfit`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司并购事件的盈利承诺明细数据
- **业务主键**: `EVENT_ID` (事件ID), `TARGETCOMP_CODE` (标的公司ID), `REPORT_PERIOD` (报告期)

## 中国A股盈利承诺汇总表

- **英文表名**: `CommitProfitSummary`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司并购事件的盈利承诺汇总数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `TARGETCOMP` (标的公司)

## 中国A股机构调研活动

- **英文表名**: `AshareISActivity`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司投资者关系活动信息
- **业务主键**: `EVENT_ID` (事件ID)

## 中国A股机构调研参与主体

- **英文表名**: `AShareISParticipant`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司投资者关系活动的参与者、任职机构信息

## 中国A股机构调研问答明细

- **英文表名**: `AShareISQA`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司机构调研的问答明细信息

## 中国A股上市公司信息披露考评结果

- **英文表名**: `AShareCompDisclosureResults`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录上、深交所对于上市公司每年信息披露进行考评的评级结果数据，包括考评结果、考评起始日期及考评终止日期等信息。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期)

## 中国优先股基本资料

- **英文表名**: `CPSDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司发行优先股的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `DIV_FACERATE` (票面股息率), `DIV_RATETYPE` (股息率类型代码)

## 中国优先股发行

- **英文表名**: `CPSSEO`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司发行优先股的发行日期、发行价格、募集资金合计等信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_FELLOW_ISSUETYPE` (发行方式代码), `S_FELLOW_PROGRESS` (方案进度), `ANN_DT` (公告日期)

## 中国优先股发行中介机构

- **英文表名**: `CPSAgency`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司发行优先股的中介机构信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_AGENCY_NAMEID` (中介机构公司ID), `S_RELATION_TYPCODE` (关系类型代码), `BEGINDATE` (起始日期), `CUR_SIGN` (最新标志)

## 中国优先股发行获配明细

- **英文表名**: `CPSPlacementDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录优先股发行时的获配明细
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (配售截止日期)

## 中国优先股股本

- **英文表名**: `CPSCapitalization`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录优先股的股本信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日)

## 中国优先股分红

- **英文表名**: `CPSDividend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录优先股的分红信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_DIV_PROGRESS` (方案进度), `ANN_DT` (公告日期), `REPORT_PERIOD` (分红年度)

## 中国优先股主体信用评级

- **英文表名**: `CPSIssuerRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录优先股的主体信用评级信息
- **业务主键**: `S_INFO_COMPNAME` (公司中文名称), `ANN_DT` (公告日期), `S_INFO_CREDITRATINGAGENCY` (评级机构代码)

## 中国优先股信用评级

- **英文表名**: `CPSRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录优先股的信用评级
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DT` (公告日期), `S_INFO_CREDITRATINGAGENCY` (评级机构代码)

## 中国优先股日行情

- **英文表名**: `CPSEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国优先股日行情信息，包括开盘价、收盘价、涨跌幅、成交量等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国A股指数基本资料

- **英文表名**: `AIndexDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股指数的名称、发布单位和简介
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国A股指数成份股

- **英文表名**: `AIndexMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股指数的成份明细数据
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

## 中国A股指数日行情

- **英文表名**: `AIndexEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国A股Wind行业指数日行情

- **英文表名**: `AIndexWindIndustriesEOD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股Wind行业指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国A股万得指数成份股

- **英文表名**: `AIndexMembersWIND`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股万得指数的成份明细数据
- **业务主键**: `F_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

## 中国A股指数估值数据

- **英文表名**: `AIndexValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股指数的估值衍生指标，如市盈率、市净率、当日总市值等
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `TRADE_DT` (交易日期)

## 中国A股指数行情衍生指标

- **英文表名**: `SIndexPerformance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股指数的行情衍生指标，如周涨跌幅、月涨跌幅等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国A股指数财务衍生指标

- **英文表名**: `AIndexFinancialderivative`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股指数的财务衍生指标，如成份股数量、总资产、营业收入、净利润等
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `REPORT_PERIOD` (报告期)

## 中证500指数权重

- **英文表名**: `AIndexCSI500Weight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中证500指数成份股的权重信息
- **业务主键**: `TRADE_DT` (生效日期), `S_INFO_WINDCODE` (Wind代码), `S_CON_WINDCODE` (标的Wind代码)

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

## 中国A股中证行业成分明细

- **英文表名**: `AShareCSIndustriesClass`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股中证行业二级分类成份明细
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CS_IND_CODE` (中证行业代码), `ENTRY_DT` (纳入日期)

## 中国A股中证指数备选成分股名单

- **英文表名**: `AIndexAlternativeMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股中证指数备选成份股名单、日期及排序。加工频率：每年
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_CON_WINDCODE` (成分股Wind代码), `ANN_DATE` (公告日期)

## 沪深300免费指数权重

- **英文表名**: `AIndexHS300FreeWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深300免费指数成份股的权重信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `TRADE_DT` (交易日期)

## 沪深300指数成份股当日收盘权重

- **英文表名**: `AIndexHS300CloseWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深300指数成份股当日收盘权重信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `TRADE_DT` (交易日期)

## 沪深300指数成份股次日开盘权重

- **英文表名**: `AIndexHS300Weight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深300指数成份股次日开盘权重信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `TRADE_DT` (交易日期)

## 沪深300指数日行情

- **英文表名**: `HS300IEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录沪深300指数的日行情数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

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

## 中国A股中信指数成份股二级

- **英文表名**: `AIndexMembersCITICS2`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股中信行业二级分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_CON_WINDCODE` (Wind代码), `S_CON_INDATE` (纳入日期)

## 中国A股中信行业指数日行情

- **英文表名**: `AIndexIndustriesEODCITICS`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股中信行业指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国A股中信指数成份股

- **英文表名**: `AIndexMembersCITICS`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股中信行业一级分类信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

## 中国A股中信行业分类

- **英文表名**: `AShareIndustriesClassCITICS`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股中信行业分类数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CITICS_IND_CODE` (中信行业代码), `ENTRY_DT` (纳入日期)

## 中国A股中信指数成份股三级

- **英文表名**: `AIndexMembersCITICS3`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股中信行业三级分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_CON_WINDCODE` (Wind代码), `S_CON_INDATE` (纳入日期)

## 中信标普GICS行业分类(废弃)

- **英文表名**: `AShareGICSIndustriesClass`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中信标普300成份股4级行业及中标综指GICS2级行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `GICS_IND_CODE` (GICS行业代码), `ENTRY_DT` (纳入日期)

## 申万指数行情

- **英文表名**: `ASWSIndexEOD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股申万指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `TRADE_DT` (交易日期)

## 申万行业分类

- **英文表名**: `AShareSWIndustriesClass`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股申万行业分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SW_IND_CODE` (申万行业代码), `ENTRY_DT` (纳入日期)

## 申万指数成份明细

- **英文表名**: `SWIndexMembers`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股申万指数成份明细信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

## 申万指数成份日收盘权重

- **英文表名**: `ASWSIndexCloseWeight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股申万指数成份日收盘权重信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `TRADE_DT` (日期)

## 上证50指数权重

- **英文表名**: `AIndexSSE50Weight`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录上证50指数成份股的权重信息
- **业务主键**: `TRADE_DT` (生效日期), `S_INFO_WINDCODE` (标的Wind代码), `S_CON_WINDCODE` (Wind代码)

## FileSync转档时间

- **英文表名**: `FileSyncTimeSchedule`
- **更新频率**: week
- **全量产品**: 是
- **说明**: 记录FileSync产品的转档时间

## 中国A股投资评级汇总

- **英文表名**: `AShareStockRatingConsus`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股投资评级，此数据是wind根据机构对个股的投资评级汇总计算得出的
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `RATING_DT` (日期), `S_WRATING_CYCLE` (周期)

## 中国A股盈利预测汇总

- **英文表名**: `AShareConsensusData`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录万得根据机构对个股的盈利预测汇总计算的综合值
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EST_DT` (预测日期), `EST_REPORT_DT` (预测报告期), `CONSEN_DATA_CYCLE_TYP` (综合值周期类型)

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

## 中国A股上市定价预测

- **英文表名**: `AShareIPOPricingForecast`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录新股上市当天各大机构对价格的预测情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `RESEARCH_INST_ID` (机构ID)

## 中国A股投资评级明细

- **英文表名**: `AShareStockRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录研究机构对A股的投资评级明细数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_EST_INSTITUTE` (研究机构名称), `S_EST_RATINGANALYST` (分析师名称), `S_EST_ESTNEWTIME_INST` (评级日期)

## 中国A股盈利预测明细

- **英文表名**: `AShareEarningEst`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录研究机构的研究员对A股的盈利预测数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `RESEARCH_INST_NAME` (研究机构名称), `EST_DT` (预测日期), `REPORTING_PERIOD` (预测报告期), `REPORT_NAME` (报告标题)

## 中国A股行业投资评级

- **英文表名**: `AShareIndusRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录研究机构对wind行业的投资评级数据
- **业务主键**: `WIND_IND_CODE` (Wind行业ID), `RATING_INSTITUTE` (机构), `RATING_ANALYST` (分析师), `RATING_DT` (评级日期), `REPORT_IND` (原始行业)

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

## 中债登估值(优先股及其他)

- **英文表名**: `CBondAnalysisCNBD7`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债登对优先股及其他性质证券的估值
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

## 中国外汇牌价

- **英文表名**: `FXRMBMidRate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录每一工作日人民币中间价及人民币兑西方23种主要货币的牌价
- **业务主键**: `CRNCY_CODE` (货币代码), `TRADE_DT` (日期)

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

## 基金关联方持有份额

- **英文表名**: `CMFRelatedPartiesHolder`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录基金关联方持有该基金的份额数据，包括持有人名称、持有份额及持有比例等信息。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `END_DATE` (截止日期), `HOLDER_COMPCODE` (持有人公司ID)

## 中国货币式基金日收益(拆分)

- **英文表名**: `CMoneyMarketDailyFIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录货币市场基金每万份基金每天的单位收益及最近七日收益所折算的年资产收益率
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `F_INFO_BGNDATE` (起始日期), `F_INFO_ENDDATE` (截止日期)

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

## 中国封闭式基金场内申购赎回

- **英文表名**: `ClosedFundPchRedm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录封闭式基金场内申购赎回情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_EXCHMARKET` (交易所)

## 中国开放式基金场内申购赎回

- **英文表名**: `LOFPchRedm`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录开放式基金场内申购赎回情况
- **业务主键**: `S_INFO_WINDCODE` (基金Wind代码)

## 中国货币式基金投资组合剩余期限(报告期)

- **英文表名**: `CMMFPortfolioPTM`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录货币式基金定期（季度）公布的投资组合剩余期限信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `F_PTM_TOP` (剩余期下限), `TYPECODE` (类型)

## 全球基金债券组合(分评级)

- **英文表名**: `FundBondportfolio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录全球基金持有的不同评级等级的债券组合信息
- **业务主键**: `S_INFO_CODE` (基金代码), `DEADLINE` (截止日期)

## 中国期货基本资料

- **英文表名**: `CFuturesDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国期货相关品种的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_CODE` (交易代码), `FS_INFO_DLMONTH` (交割月份)

## 中国期货标准合约属性

- **英文表名**: `CFuturesContPro`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国期货标准合约的属性信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_CODE` (标准合约代码)

## 中国期货标准合约属性变更

- **英文表名**: `CFuturesContProChange`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货标准合约的属性信息的变更情况
- **业务主键**: `OBJECT_ID` (对象ID), `CONTRACT_ID` (合约ID), `CHANGE_DT` (变更日期)

## 中国期货标准合约价格波动限制变更

- **英文表名**: `CFuturesPriceChangeLimit`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货标准合约价格波动限制变更信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期)

## 中国期货交易所标准产品代码

- **英文表名**: `FuturesExchangeproductcode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货各品种交易所标准产品代码
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `BUSINESS_TYPE_CODE` (业务代码类型), `BUSINESS_CODE` (业务代码)

## 中国期货连续(主力)合约和月合约映射表

- **英文表名**: `CfuturesContractMapping`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国期货连续(主力)合约和月合约间的关系信息
- **业务主键**: `S_INFO_WINDCODE` (连续(主力)合约Wind代码), `STARTDATE` (起始日期)

## 中国期货保证金比例

- **英文表名**: `CFuturesmarginratio`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货品种的保证金比例信息
- **业务主键**: `S_INFO_WINDCODE` (合约Wind代码), `TRADE_DT` (变动日期)

## 中国期货交易日历

- **英文表名**: `CFuturesCalendar`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国期货相关品种的交易日信息
- **业务主键**: `TRADE_DAYS` (日期), `S_INFO_EXCHMARKET` (交易所英文简称)

## 中国期货套利合约关系表

- **英文表名**: `CFuturesArbitrageContract`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录期货套利合约的关系信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_RALATEDCODE` (关联证券Wind代码), `S_RELATION_TYPCODE` (关系类型代码), `S_INFO_EFFECTIVE_DT` (生效日期)

## 中国期货交易交割手续费

- **英文表名**: `CfuturesDeliveryFee`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货交易所公布的期货交割手续费，包括月合约证券ID、交易手续费额、交易手续费率等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DATE` (日期)

## 中国期货库存(仓单)

- **英文表名**: `CFuturesInstock`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货品种的仓单库存信息
- **业务主键**: `FS_INFO_SCNAME` (标准合约名称), `ANN_DATE` (日期)

## 中国期货月合约持仓限制

- **英文表名**: `CFuturesPositionLimit`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货品种月合约持仓数量限制的变化信息
- **业务主键**: `S_INFO_WINDCODE` (月合约Wind代码), `POSITION_LIMIT_TYPE` (限仓对象类型代码), `CHANGE_DT` (变动日期)

## 中国期货库存报告

- **英文表名**: `CFuturesWarehouseStocks`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货品种的入仓、出仓、注销仓单等情况
- **业务主键**: `S_INFO_CODE` (标准合约代码), `ANN_DATE` (日期), `WAREHOUSE_REGION` (地区), `WAREHOUSE_NAME` (仓库简称)

## 中国期货套保持仓

- **英文表名**: `CFuturesHedgingPositions`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录商品期货套期保值持仓数据
- **业务主键**: `FS_INFO_SCCODE` (标准合约代码), `FS_INFO_DATE` (日期)

## 中国期货交割数据

- **英文表名**: `CFuturesDelivery`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货交易所内品种的交割数据，包括交割类型、交割金额、交割结算价等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国期货交割意向申报

- **英文表名**: `CFuturesDeclarationOfDI`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货品种交割意向申报情况，包括会员公司ID、申报卖方交割量、申报买方交割量等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国期货交易所单边市状态

- **英文表名**: `CFuturesunilateralMakt`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货交易所期货品种单边市交易状态，包括期货wind代码、交易所、单边市状态、连续单边市天数等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国期货交割仓库基本资料

- **英文表名**: `CFuturesDeliveryWHInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货交易所公布的期货交割仓库基本资料，包括标准合约代码、办公地址、是否基准库等。
- **业务主键**: `S_INFO_SCCODE` (标准合约代码), `DESIGN_DELVY_WRHS` (指定交割仓库名称)

## 中国商品期货日行情

- **英文表名**: `CCommodityFuturesEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国商品期货的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国商品期货成交及持仓

- **英文表名**: `CCommodityFuturesPositions`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国商品期货的成交及持仓信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期), `FS_INFO_MEMBERNAME` (会员简称), `FS_INFO_TYPE` (类型)

## 中国股指期货日行情

- **英文表名**: `CIndexFuturesEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国股指期货的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国股指期货成交及持仓

- **英文表名**: `CIndexFuturesPositions`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国股指期货的成交及持仓信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `FS_INFO_TYPE` (类型), `FS_INFO_RANK` (名次), `S_INFO_COMPCODE` (会员ID)

## 中国国债期货标的券

- **英文表名**: `CbondFSubjectcvf`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国国债期货的标的券信息
- **业务主键**: `S_INFO_WINDCODE` (月合约Wind代码), `DLS_WINDCODE` (标的券Wind代码)

## 中国国债期货最便宜可交割券

- **英文表名**: `CbondFCTD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国国债期货的最便宜可交割券信息
- **业务主键**: `S_INFO_WINDCODE` (月合约Wind代码), `TRADE_DT` (日期)

## 中国国债期货交易日行情

- **英文表名**: `CBondFuturesEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国国债期货的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `S_DQ_CCCODE` (连续合约代码)

## 中国国债期货成交及持仓

- **英文表名**: `CBondFuturesPositions`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国国债期货的成交及持仓信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期), `FS_INFO_MEMBERNAME` (会员简称), `FS_INFO_TYPE` (类型)

## 中国国债期货可交割券衍生指标

- **英文表名**: `CbondFValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国国债期货的可交割券衍生指标，如交割利息、区间利息、基差等
- **业务主键**: `S_INFO_WINDCODE` (月合约Wind代码), `DLS_WINDCODE` (可交割券Wind代码), `TRADE_DT` (日期)

## 中国国债基准收益率

- **英文表名**: `CGBbenchmark`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国国债基准收益率信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国期权日行情

- **英文表名**: `ChinaOptionEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期权的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国期权月合约属性变动表

- **英文表名**: `COptionDescriptionchange`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期权月合约属性变动的信息
- **业务主键**: `OBJECT_ID` (对象ID), `S_INFO_WINDCODE` (期权月合约代码), `S_CHANGE_DATE` (调整日期)

## 中国权证基本资料

- **英文表名**: `CWarrantDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国权证的基本资料
- **业务主键**: `WINDCODE` (权证证券id), `UNDERLYINGWINDCODE` (标的证券id), `DURATION_DAYS` (存续期限(天))

## 中国期权衍生指标

- **英文表名**: `ChinaOptionValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期权涨跌停限制及分析指标
- **业务主键**: `S_INFO_WINDCODE` (月合约Wind代码), `TRADE_DT` (交易日期)

## 中国权证持有人

- **英文表名**: `CWarrantHolder`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国权证的持有人信息
- **业务主键**: `F_INFO_WINDCODE` (Wind代码), `END_DATE` (日期), `HOLDER` (持有人)

## 中国期权基本资料

- **英文表名**: `ChinaOptionDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国期权的基本资料
- **业务主键**: `S_INFO_WINDCODE` (月合约Wind代码), `S_INFO_CODE` (月合约交易所编码), `S_INFO_EXNAME` (月合约交易所简称)

## 中国期权指数日行情

- **英文表名**: `ChinaOptionIndexEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期权指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国期权标准合约属性

- **英文表名**: `ChinaOptionContpro`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国期权标准合约的相关属性
- **业务主键**: `S_INFO_WINDCODE` (标的Wind代码), `S_INFO_CODE` (期权Wind代码), `S_INFO_EXNAME` (交易所名称)

## 中国期权交易日历

- **英文表名**: `ChinaOptionCalendar`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国期权的交易日信息
- **业务主键**: `TRADE_DAYS` (交易日), `S_INFO_EXCHMARKET` (交易所英文简称)

## 外汇期权Delta计量参数

- **英文表名**: `ForexOptionDelta`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国货币网公布的外汇期权Delta计量参数
- **业务主键**: `CRNCY_CODE` (外汇品种代码), `TRADE_DT` (交易日期), `ANAL_CURVETERM` (标准期限), `SPOT_PRICE_TYPE_CODE` (即期价格类型代码), `RMB_RATE_TYPE_CODE` (人民币利率类型代码), `VOLATILITY_TYPE_CODE` (波动率类型代码)

## 中国期权标准合约属性变更

- **英文表名**: `COptionContProChange`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录期权标准合约属性变更情况
- **业务主键**: `CONTRACT_ID` (合约代码), `CHANGE_DT` (变更日期)

## 中国期权曾用名

- **英文表名**: `ChinaOptionPreviousName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录期权历次更名记录
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `BEGINDATE` (起始日期)

## 中国期权隐含波动率

- **英文表名**: `COptionImpliedVolatility`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期权隐含波动率的数据，包括标准合约代码、波动率类型、期限及隐含波动率等信息。
- **业务主键**: `S_INFO_SCCODE` (标准合约代码), `VOLATILITY_TYPE` (波动率类型), `TERM` (期限), `TRADE_DT` (日期)

## Wind中国期权衍生指标

- **英文表名**: `WindChinaOptionValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期权品种Wind盘后16:30计算的期权衍生指标，比如Delta、Theta、Gamma等。
- **业务主键**: `S_INFO_WINDCODE` (月合约Wind代码), `TRADE_DT` (交易日期)

## 中国期权日交易统计

- **英文表名**: `ChinaOptionDailyStatistics`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期权每日的交易情况信息
- **业务主键**: `S_INFO_CODE` (期权Wind代码), `TRADE_DT` (交易日期), `ITEM_CODE` (类型)

## 中国期权会员交易统计

- **英文表名**: `ChinaOptionMemberStatistics`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期权会员成交量与持仓量等数据，分认购与认沽
- **业务主键**: `S_INFO_CODE` (期权Wind代码), `TRADE_DT` (交易日期), `ITEM_CODE` (类型), `S_INFO_MEMBERNAME` (会员简称)

## 中国期货指数日行情

- **英文表名**: `CFutureIndexEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国期货指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国国债期货可交割券第三方估值

- **英文表名**: `CBondFThirdPartyValuation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中债、中证等第三方估值数据计算的国债期货IRR等衍生指标信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `DLS_WINDCODE` (Wind代码), `PRICETYPE_CODE` (价格类型代码), `TRADE_DT` (日期), `DL_COST` (交割成本)

## 其他第三方商品期货指数行情

- **英文表名**: `ThirdPartyIndexEOD`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录除交易所、发布过批量指数的第三方指数之外的其他第三方商品期货指数日行情信息
- **业务主键**: `S_INFO_WINDCODE` (WIND代码), `TRADE_DT` (交易日期)

## 中国黄金现货基本资料

- **英文表名**: `CGoldSpotDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录中国黄金现货的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_EXCHMARKET` (交易所)

## 中国黄金现货日行情

- **英文表名**: `CGoldSpotEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国黄金现货的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 中国B股日行情

- **英文表名**: `BShareEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录B股的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国B股停复牌信息

- **英文表名**: `BShareTradingSuspension`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录B股的停、复牌信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_DQ_SUSPENDDATE` (停牌日期)

## 香港股票公司名称变更

- **英文表名**: `HKChangeCompanyName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司名称的历次变更情况
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `CHANGE_DT` (变动日期)

## 香港股票上市公司基本资料

- **英文表名**: `HKCompanyInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的基本资料
- **业务主键**: `S_INFO_COMPCODE` (公司ID)

## 香港股票名称变更

- **英文表名**: `HKShareChangeName`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股名称的历次变更信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期)

## AH股关联证券

- **英文表名**: `SHSZRelatedsecurities`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股和A股代码的对应关系
- **业务主键**: `EXCHANGE_A` (交易所1), `S_INFO_WINDCODE` (WIND代码1), `EXCHANGE_B` (交易所2), `S_INFO_WINDCOD2` (WIND代码2)

## 香港股票基本资料

- **英文表名**: `HKShareDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 香港股票面值及交易单位

- **英文表名**: `HKShareParvalueLotsize`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的面值及交易单位信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (变动日期)

## 香港股票代码变更表

- **英文表名**: `HKStockChangecode`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录港股代码的历次变更信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_OLDWINDCODE` (变更前Wind代码), `S_INFO_NEWWINDCODE` (变更后Wind代码), `CHANGE_DATE` (Wind代码变更日期)

## 证券类型代码配置表

- **英文表名**: `SecuritiesTypecode`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 证券类型和代码的配置表
- **业务主键**: `TYPE_CODE` (证券类型代码)

## 香港股票终止上市

- **英文表名**: `HKShareEndlist`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录港股终止上市信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 香港股票概念板块

- **英文表名**: `HKConceptualplate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司所属的概念板块。
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMP_NAME` (公司名称)

## 香港股票中介机构

- **英文表名**: `HKShareAgency`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股发行的相关中介机构
- **业务主键**: `SEC_ID` (证券id), `AGENCYNAME` (机构名称), `TYPE_CODE` (关系类型代码), `SCP` (业务范围), `START_DT` (起使日期), `END_DT` (终止日期)

## 香港股票发行数据

- **英文表名**: `HKShareIssuance`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的发行信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ANN_DATE` (发行公告日), `S_ISSUE_TYPE` (发行方式)

## 香港港股通成分股

- **英文表名**: `HKSCMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股通的成分股明细数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `ENTRY_DT` (纳入日期), `S_INFO_SECTOR` (所属板块代码)

## 香港股票行业分类编码

- **英文表名**: `HKStockIndustriesCode`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录行业板块和代码间的映射关系，是配置表
- **业务主键**: `INDUSTRIESCLASS` (行业分类), `INDUSTRIESCODE` (行业代码)

## 香港股票Wind行业分类

- **英文表名**: `HKStockWindIndustriesMembers`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录港股的Wind行业分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `WIND_IND_CODE` (Wind行业代码), `ENTRY_DT` (纳入日期)

## 香港股票概念板块分类

- **英文表名**: `HKShareConseption`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的概念板块分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `HS_IND_CODE` (行业或类别代码), `ENTRY_DT` (起始日期)

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

## 香港股票日行情

- **英文表名**: `HKshareEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 香港股票卖空成交量

- **英文表名**: `HKShareShortSellingTurnover`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股卖空的成交量
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `S_INFO_DATATYPE` (数据类型)

## 香港股票可卖空证券明细

- **英文表名**: `HKStockShortSellingList`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股可卖空的证券明细
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `BEGINDATE` (起始日期), `ENDDATE` (终止日期)

## 香港股票停复牌信息

- **英文表名**: `HKTransactionStatus`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的停复牌信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SUSPENDDATE` (停牌日期), `SUSPENDTYPECODE` (停牌类型代码), `RESUMPDATE` (复牌日期)

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

## 香港股票证券未平仓卖空量

- **英文表名**: `HKShareUnsoldShortsale`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股未平仓卖空量
- **业务主键**: `S_INFO_WINDCODE` (WIND代码1), `TRADE_DT` (日期)

## 香港交易所交易日历

- **英文表名**: `HKEXCalendar`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港交易所的交易日信息
- **业务主键**: `TRADE_DAYS` (日期), `S_INFO_EXCHMARKET` (交易所英文简称)

## 港股市场中介持股统计

- **英文表名**: `HKShareAgencyHoldings`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股通、中资机构、国际机构、香港本地机构等媒介或中介持有的港股数量
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 香港股票日行情估值指标

- **英文表名**: `HKShareEODDerivativeIndex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的日估值和财务指标，如市值、市盈
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `FINANCIAL_TRADE_DT` (交易日期)

## 香港股票行情日收益率

- **英文表名**: `HKShareYield`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的周/月行情指标，如涨跌幅、成交量、成交额、换手率。记录全球股票的风险分析指标，如平均收益率、方差、标准差、BETA、ALPHA等，频率包括日、周、月等
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 香港股票存托凭证份额

- **英文表名**: `HDRInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证份额及每份凭证对应基础证券数量
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `END_DATE` (截止日期)

## 香港股票发行数量

- **英文表名**: `HKShareCapitalization`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的发行数量
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日)

## 香港证券回购信息

- **英文表名**: `HKStockRepo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港联交所的证券回购信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 香港股票股本结构

- **英文表名**: `HKEquityStruc`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的股本变动情况
- **业务主键**: `S_INFO_COMPCODE` (公司id), `CHANGE_DATE` (变动日期1(除权日或上市日))

## 香港股票自由流通股本

- **英文表名**: `HKShareFreeFloat`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录wind计算的港股自由流通股本
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DT` (变动日期(除权日))

## 香港股票权益事件

- **英文表名**: `HKshareEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司所有分红、配股、股份合并等可能导致股价变动的权益事项
- **业务主键**: `OBJECT_ID` (对象ID)

## 港股限售股流通日历

- **英文表名**: `HKShareFreeFloatCalendar`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股限售股流通日历数据，包括可流通日期、上市流通股份类型及冻结期限等信息。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_LISTDATE` (可流通日期), `S_SHARE_LSTTYPECODE` (上市股份类型代码)

## 香港股票财务指标

- **英文表名**: `HKFinancialIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的财务指标，依据财务报表计算
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_TYPE` (报告类型), `STATEMENT_TYPE` (报表类型), `BEGINDATE` (起始日期), `ENDDATE` (截止日期)

## 香港股票财报年结日变更

- **英文表名**: `CHGFinYearEndDT`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股财报年结日变更的情况
- **业务主键**: `S_INFO_COMPCODE` (品种ID), `ID_TYPECODE` (品种类别代码), `CHG_TYPECODE` (条款属性类型代码), `START_DT` (起始日期)

## 香港股票重大事件表

- **英文表名**: `HKShareMajorEvent`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的重大事件信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_EVENT_CATEGORYCODE` (事件类型代码), `S_EVENT_HAPDATE` (发生日期), `S_EVENT_EXPDATE` (失效日期)

## 香港股票诉讼事件

- **英文表名**: `HKShareProsecution`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司作为原告或被告的涉案情况和案件审理、判决、执行、上诉及二审判决情况
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DT` (公告日期), `COURT` (一审受理法院), `COURT2` (二审受理法院)

## 香港股票特别处理

- **英文表名**: `HKShareST`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股特别处理的实施和撤销、暂停/恢复上市，以及退市记录及原因
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_TYPE_ST` (特别处理类型), `ENTRY_DT` (实施日期)

## 香港股票股东大会通知

- **英文表名**: `HKShareholdersmeeting`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股股东大会的召开时间及审议事项
- **业务主键**: `S_INFO_COMPCODE` (品种ID), `ANN_DT` (公告日期), `MEETING_DT` (会议日期), `MEETING_TYPE` (会议类型)

## 香港股票股东大会议案网络投票表决明细

- **英文表名**: `HKShareInternetvoting`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股股东大会议案网络投票表决的明细信息
- **业务主键**: `S_EVENT_ID` (会议事件ID), `S_EVENT_NUM` (议案序号)

## 香港股票违规事件

- **英文表名**: `HKShareIllegality`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录各级主管部门公布的对港股公司违规行为的调查结果与处理决定
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DT` (公告日期), `SUBJECT_TYPE` (主体类别代码), `PROCESSOR` (处理人)

## 香港股票大股东增减持

- **英文表名**: `HKShareHolderTrade`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的大股东增减持信息
- **业务主键**: `SEC_ID` (证券ID), `END_DT` (事件日期), `HOLDER_NAME` (最终持有人名称), `SHRNUM` (增/减或涉及的股份数量), `SHROP` (持有权益类型), `AFTSHRNUM` (变动后股份总数(股))

## 香港股票大股东

- **英文表名**: `HKShareInsideHolder`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的大股东持股信息
- **业务主键**: `S_INFO_COMPCODE` (公司id), `END_DT` (截至日期), `HOLDERNAME` (股东名称), `SHARETYPE` (股份性质)

## 香港股票管理层信息

- **英文表名**: `HKShareManagement`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的管理层信息
- **业务主键**: `S_INFO_COMPCODE` (公司id), `S_INFO_MANAGER_NAME` (姓名), `S_INFO_MANAGER_ENNAME` (英文名), `S_INFO_MANAGER_STARTDATE` (任职日期), `S_INFO_MANAGER_LEAVEDATE` (离职日期)

## 香港股票管理层持股及报酬

- **英文表名**: `HKShareManagementHoldReward`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的管理层持股及报酬信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `END_DATE` (截止日期), `S_INFO_MANAGER_NAME` (姓名), `S_INFO_MANAGER_POST` (职务)

## 香港股票员工人数变更

- **英文表名**: `HKShareStaff`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的员工人数变更情况
- **业务主键**: `S_INFO_COMPCODE` (公司id), `END_DT` (截止日期)

## 香港股票控股参股

- **英文表名**: `HKShareCompanyHoldShares`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的控股参股信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ENDDATE` (截止日期), `S_CAPITALOPERATION_COMPANYNAME` (被参控公司名称)

## 香港股票实际控制人

- **英文表名**: `HKShareEquityRelationships`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股公司的股权关系、实际控制人信息
- **业务主键**: `S_INFO_COMPNAME` (公司名称), `S_INFO_COMPCODE` (公司ID), `ENDDATE` (截止日期), `S_HOLDER_NAME` (股东名称)

## 香港股票投资评级明细

- **英文表名**: `HKAnalystRating`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的投资评级明细数据
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `INSTITUTION` (机构), `EST_DATE` (评级日期)

## 香港股票盈利预测明细

- **英文表名**: `HKProfitForecast`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的盈利预测明细数据
- **业务主键**: `S_INFO_COMPCODE` (公司id), `INSTITUTION` (机构), `ANALYST` (分析师), `ENDDATE` (截止日期), `EST_DATE` (预测日期)

## 香港股票Wind一致预测个股指标

- **英文表名**: `HKStockConsensusindex`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港交所个股一致预测指标，不定期生成，依据wind一致预测数据生成。
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DT` (日期), `EST_REPORT_DT` (报告期)

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

## 香港股票指数基本资料

- **英文表名**: `HKIndexDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录香港股票指数的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 香港股票指数日行情

- **英文表名**: `HKIndexEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港股票指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 香港股票指数板块代码

- **英文表名**: `HKStockIndexCode`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录香港股票指数对应的板块信息
- **业务主键**: `S_INFO_INDEXWINDCODE` (指数万得代码), `S_INFO_INDUSTRYCODE` (板块代码)

## 香港股票指数成份股

- **英文表名**: `HKStockIndexMembers`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录香港股票指数对应成份股信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

## 香港期货标准合约属性

- **英文表名**: `HKFuturescontpro`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录香港期货标准合约的属性信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_CODE` (标准合约代码), `S_INFO_LISTDATE` (合约上市日期)

## 香港期货基本资料

- **英文表名**: `HKFuturesDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录香港期货的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_CODE` (交易代码), `FS_INFO_SCCODE` (标准合约代码), `S_INFO_LISTDATE` (上市日期), `S_INFO_DELISTDATE` (最后交易日期)

## 香港期货日行情

- **英文表名**: `HKFuturesEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港期货的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 香港期货保证金

- **英文表名**: `HKFuturesMargin`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港期货品种的保证金信息
- **业务主键**: `TRADE_DT` (变动日期), `S_INFO_WINDCODE` (标准合约Wind代码), `MARGIN_TYPE` (保证金类型)

## 香港期货标准合约属性变更

- **英文表名**: `HKFuturesContProChange`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港期货标准合约的属性信息变动情况
- **业务主键**: `CONTRACT_ID` (合约ID), `ITEM` (变更字段名称), `CHANGE_DT` (变更日期)

## 香港期权标准合约属性

- **英文表名**: `HKOptionContpro`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录香港期权标准合约的属性信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_CODE` (标准合约代码), `S_INFO_LISTEDDATE` (合约上市日期)

## 香港期权基本资料

- **英文表名**: `HKOptionDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港期权的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_CODE` (交易代码), `S_INFO_SCCODE` (标准合约代码), `S_INFO_LASTTRADINGDATE` (最后交易日)

## 香港期权日行情

- **英文表名**: `HKOptionEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录香港期权的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期), `S_INFO_STRIKEPRICE_TYPE` (期权行权价及类型)

## 香港期权交易日历

- **英文表名**: `HKOptionCalendar`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录香港期权品种的交易日信息
- **业务主键**: `TRADE_DAYS` (交易日), `S_INFO_EXCHMARKET` (交易所英文简称)

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

## 香港股票GICS行业成份(废弃)

- **英文表名**: `HKStockGICSIndustriesMembers`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股的GICS行业成份明细
- **业务主键**: `COMP_ID` (公司ID), `GICS_IND_CODE` (GICS行业代码), `ENTRY_DT` (起始日期)

## 港股通申万行业分类（一年更新一次）

- **英文表名**: `HKShareSWIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录港股通的申万行业分类
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `SW_IND_CODE` (申万行业代码), `ENTRY_DT` (纳入日期)

## 香港股票恒生行业分类

- **英文表名**: `HKStockHSIndustriesMembers`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录港股的恒生行业分类信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `HS_IND_CODE` (恒生行业代码), `ENTRY_DT` (纳入日期)

## 中国外汇交易行情

- **英文表名**: `FXEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录每天外汇交易行情数据
- **业务主键**: `TRADE_DT` (交易日期), `S_INFO_WINDCODE` (外汇交易代码)

## 股转系统股票基本资料

- **英文表名**: `NEEQSDescription`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录新三板股票的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 股转系统公司简介

- **英文表名**: `NEEQSIntroduction`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录新三板公司的基础信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID)

## 股转系统股票Wind行业分类

- **英文表名**: `NEEQSIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录新三板股票的Wind行业分类
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `WIND_IND_CODE` (Wind行业代码), `ENTRY_DT` (纳入日期)

## 股转系统股票证监会行业分类

- **英文表名**: `NEEQSSECIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录新三板股票的证监会行业分类
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `WIND_IND_CODE` (板块代码), `ENTRY_DT` (纳入日期)

## 股转系统股票分层分类

- **英文表名**: `NEEQGradation`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录新三板股票的分层分类信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `WIND_SEC_CODE` (板块代码), `ENTRY_DT` (纳入日期)

## 股转系统股票园区分类

- **英文表名**: `NEEQSPark`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录新三板股票的园区分类信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `WIND_SEC_CODE` (板块代码), `ENTRY_DT` (纳入日期)

## 股转系统股票日行情

- **英文表名**: `NEEQSEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录新三板股票的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

## 股转系统指数日行情

- **英文表名**: `NEEQIndexEODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录股转系统指数的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (交易日期)

## 中国券商集合理财分红

- **英文表名**: `ChinaInhouseFundDividend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录券商理财的分红信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `EX_DT` (除息日)

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

## 中国A股公司应付账款

- **英文表名**: `AshareAccountspayable`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的应付账款
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (上游公司ID), `REPORT_PERIOD` (报告期), `S_INFO_AMOUNT` (金额)

## 中国A股公司供应商

- **英文表名**: `AshareSupplier`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的供应商
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMP_NAME` (上游公司名称), `S_INFO_COMPCODE1` (上游公司ID), `REPORT_PERIOD` (报告期), `S_INFO_AMOUNT` (金额), `S_INFO_DISCLOSER` (披露公司ID)

## 中国A股公司客户

- **英文表名**: `AshareCustomer`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的客户
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_DIMENSION` (维度), `S_INFO_DIMENSION1` (子维度), `REPORT_PERIOD` (报告期)

## 中国A股应收账款

- **英文表名**: `AshareReceivables`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的应收账款
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_DIMENSION` (维度), `S_INFO_DIMENSION1` (子维度), `REPORT_PERIOD` (报告期)

## 中国A股公司高管成员

- **英文表名**: `AshareAdministration`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司的高管成员
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_MANID` (人物id)

## 中国A股公司董事成员

- **英文表名**: `AshareDirector`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司的董事成员
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_MANID` (人物id)

## 中国A股公司监事成员

- **英文表名**: `AshareSupervisor`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司的监事成员
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_MANID` (人物id)

## 中国A股被担保

- **英文表名**: `AshareBeguaranteed`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的被担保情况
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_DIMENSION1` (子维度), `S_INFO_COMPCODE1` (担保公司ID), `REPORT_PERIOD` (报告期)

## 中国A股关联方债权

- **英文表名**: `AshareCreditorrights`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的关联方债权信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_DIMENSION` (维度), `S_INFO_DIMENSION1` (子维度), `REPORT_PERIOD` (报告期)

## 中国A股担保

- **英文表名**: `Ashareguaranteerelationship`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的担保情况
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_DIMENSION` (维度), `S_INFO_DIMENSION1` (子维度), `S_INFO_COMPCODE1` (被担保公司ID), `REPORT_PERIOD` (报告期), `S_INFO_AMOUNT` (金额)

## 中国A股长期借款

- **英文表名**: `AshareLongLoan`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的长期借款
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (债务公司ID), `REPORT_PERIOD` (报告期)

## 中国A股关联方债务

- **英文表名**: `Asharerelatedpartydebt`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的关联方债务
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (债权公司ID), `REPORT_PERIOD` (报告期)

## 中国A股控参股

- **英文表名**: `AshareHolding`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的控股参股信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (投资公司ID), `S_HOLDER_ENDDATE` (报告期)

## 中国A股投资PEVC基金

- **英文表名**: `AshareInvestmentPEVC`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司投资PEVC基金的信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (投资公司ID), `S_HOLDER_DATE` (投资时间)

## 中国A股公司诉讼-被告

- **英文表名**: `AshareDefendant`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的涉诉信息（被告）
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DATE` (公告日期), `LITIGATION_EVENTS_ID` (诉讼事件ID)

## 中国A股公司诉讼-原告

- **英文表名**: `AsharePlaintiff`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的涉诉信息（原告）
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ANN_DATE` (公告日期), `LITIGATION_EVENTS_ID` (诉讼事件ID)

## 中国A股流通股东持股比例

- **英文表名**: `AshareCirculatingholders`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的流通股东持股比例
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (股东公司ID), `S_HOLDER_ENDDATE` (报告期)

## 中国A股股东

- **英文表名**: `Ashareholder`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的股东
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (股东公司ID), `S_HOLDER_ENDDATE` (报告期)

## 中国A股机构持股

- **英文表名**: `Asharemechanismownership`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的机构持股信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMP_NAME` (股东公司名称), `S_HOLDER_ENDDATE` (报告期)

## 中国A股PEVC投资机构

- **英文表名**: `AsharePEVCInvestment`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司PEVC投资机构
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (股东公司ID), `S_HOLDER_DATE` (融资时间)

## 中国A股并购标的

- **英文表名**: `AshareMergersubject`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司并购的标的信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_UPDATE_DATE` (最新披露日期), `S_MEETEVENT_ID` (事件ID)

## 中国A股并购出售标的

- **英文表名**: `AshareSellsubject`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的并购出售标的信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_MEETEVENT_ID` (事件ID)

## 中国A股公司产品

- **英文表名**: `Ashareproduct`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录A股公司的产品
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_ENDDATE` (截止日期), `S_PRODUCT_NAME` (产品名称)

## 中国A股公司概念板块

- **英文表名**: `AshareConceptualplate`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司所属概念板块
- **业务主键**: `S_INFO_COMPCODE` (公司ID)

## 中国A股公司集团信息

- **英文表名**: `AshareGroupinformation`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股公司集团信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_COMPCODE1` (集团子公司ID)

## 中国A股公司所属集团信息

- **英文表名**: `AshareGroup`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国A股公司所属集团信息，包括公司ID、集团公司名称、集团公司中文简称等。

## 中国存托凭证证监会新版行业分类

- **英文表名**: `CDRSECNIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的证监会行业分类
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `SEC_IND_CODE` (证监会行业代码), `ENTRY_DT` (纳入日期)

## 中国存托凭证基本资料

- **英文表名**: `CDRDescription`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证的基本资料
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国存托凭证公司简介

- **英文表名**: `CDRIntroduction`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的基本信息
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国存托凭证Wind行业分类

- **英文表名**: `CDRIndustriesClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的Wind行业分类
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `WIND_IND_CODE` (Wind行业代码), `ENTRY_DT` (纳入日期)

## 中国存托凭证IPO类型

- **英文表名**: `CDRIPOClass`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证的IPO类型信息，包括公司名称、分类代码、剔除和纳入日期等。
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `S_INFO_TYPECODE` (分类代码), `ENTRY_DT` (纳入日期)

## 中国存托凭证Wind概念板块

- **英文表名**: `CDRConseption`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证Wind概念板块信息，包括Wind概念板块代码、Wind概念板块名称、纳入剔除日期等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `WIND_SEC_CODE` (Wind概念板块代码), `ENTRY_DT` (纳入日期)

## 中国存托凭证询价基本资料

- **英文表名**: `CDRInquiryDetailsInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证询价基本资料，包括初步询价公告日、网下配售发行公告日、网下申购配售比例（%）等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国存托凭证分红条款

- **英文表名**: `CDRDividend`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证的分红条款
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TYPE_CODE` (品种类别代码), `CLAUSE_TYPE_CODE` (条款属性类型代码), `START_DT` (起始日期)

## 中国存托凭证发行中介机构

- **英文表名**: `CDRAgency`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行的相关中介机构
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_RELATION_TYPCODE` (关系类型代码), `S_BUSINESS_TYPCODE` (业务类型代码), `S_AGENCY_NAMEID` (机构名称ID), `BEGINDATE` (起始日期)

## 中国存托凭证发行审核一览

- **英文表名**: `CDRIssueCommAudit`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证的发行审核情况
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_IC_YEAR` (年度), `S_IC_SESSIONTIMES` (会议届次), `S_IC_AUDITTYPE` (审核类型), `S_IC_TYPE` (发审委类型), `S_IC_DATE` (会议日期)

## 中国存托凭证审核申报企业情况

- **英文表名**: `CDRCompRFA`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证注册审核申报的情况
- **业务主键**: `S_INFO_COMPANYID` (公司ID), `APP_CODE` (申请事项代码), `ST_DATE` (状态起始日期)

## 中国存托凭证首次公开发行数据

- **英文表名**: `CDRIPO`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证首次发行记录
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 中国存托凭证IPO初步询价明细

- **英文表名**: `CDRIPOInquiryDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证IPO初步询价明细，包括询价对象名称、投资者类别代码、配售对象名称等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `INQUIRER` (询价对象名称), `ISSUETARGET` (配售对象名称), `DEDAREDPRICE` (申报价格(元/股))

## 中国存托凭证网下配售机构获配明细

- **英文表名**: `CDRPlacementDetails`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证网下配售机构获配明细，包括股东名称、法人投资者类型、有效报价的申购数量等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_HOLDER_NAME` (股东名称), `TRADE_DT` (截止日期), `LOCKMONTH` (锁定期(月))

## 中国存托凭证网下配售机构获配统计

- **英文表名**: `CDRPlacementInfo`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证网下配售机构获配统计，包括Wind代码、投资者类型代码、网下中签率等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `PCT_CHANGE_1D` (投资者类型代码)

## 中国存托凭证发行主承销商

- **英文表名**: `CDRLeadUnderwriter`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证发行主承销商信息，包括发行类型、募集资金合计、参与主承销商个数等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_LU_ISSUEDATE` (发行日期), `S_LU_ISSUETYPE` (发行类型), `S_LU_NAME` (参与主承销商名称)

## 中国存托凭证股本

- **英文表名**: `CDRCapitalization`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证股本信息，包括总股本、流通股、限售A股(万股)等。

## 中国存托凭证限售股解禁公司明细

- **英文表名**: `CDRCompRestricted`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录中国存托凭证限售股解禁公司明细，包括wind代码、可流通日期、股份类型等。
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_LISTDATE` (可流通日期), `S_HOLDER_NAME` (股东名称), `S_SHARE_LSTTYPECODE` (股份类型代码), `S_SHARE_LST` (可流通数量(股)), `S_SHARE_PLACEMENT_ENDDT` (配售截止日期), `ANN_DT` (公告日期)

## 中国存托凭证管理层成员

- **英文表名**: `CDRManagement`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的管理层成员简历信息
- **业务主键**: `S_INFO_CODECODE` (公司ID), `S_INFO_MANAGER_POST` (职务), `MANID` (人物ID)

## 中国存托凭证员工人数变更

- **英文表名**: `CDRStaff`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的员工人数变更信息
- **业务主键**: `S_INFO_COMPCODE` (公司id), `END_DT` (截止日期)

## 中国存托凭证员工构成

- **英文表名**: `CDRStaffStructure`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的员工构成情况
- **业务主键**: `S_INFO_COMPCODE` (交易代码), `STAFF_TYPE_CODE` (人数类别代码), `END_DT` (截止日期), `ITEM_TYPE_CODE` (项目分类代码), `ITEM_NAME` (项目)

## 中国存托凭证主要控股参股公司经营情况

- **英文表名**: `CDRholdingoperate`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司主要控股参股公司经营情况
- **业务主键**: `S_INFO_COMPCODE` (公司id), `REPORT_PERIOD` (截止日期), `S_CAPITALOPERATION_COMPANYNAME` (被参控公司名称)

## 中国存托凭证控股参股

- **英文表名**: `CDRCompanyHoldShares`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的控股参股信息
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `ENDDATE` (截止日期), `S_CAPITALOPERATION_COMPANYNAME` (被参控公司名称)

## 中国存托凭证资产负债表

- **英文表名**: `CDRBalanceSheet`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的资产负债表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国存托凭证利润表

- **英文表名**: `CDRIncome`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的利润表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国存托凭证现金流量表

- **英文表名**: `CDRCashFlow`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证发行公司的现金流量表，根据2007年1月1日以后实施的会计准则编制
- **业务主键**: `S_INFO_COMPCODE` (公司ID), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型)

## 中国存托凭证财务指标

- **英文表名**: `CDRFinancialIndicator`
- **更新频率**: day
- **全量产品**: 否
- **说明**: "记录中国存托凭证财务指标，包括wind代码、息税前利润、毛利润、总资产净利率等。"
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `S_INFO_COMPCODE` (公司ID)

## 中国存托凭证审计意见

- **英文表名**: `CDRAuditOpinion`
- **更新频率**: day
- **全量产品**: 否
- **说明**: "记录中国存托凭证审计意见信息，包括审计结果类别、会计师事务所、签字会计师等。"

## 中国存托凭证日行情

- **英文表名**: `CDREODPrices`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录存托凭证的日收盘行情
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `TRADE_DT` (日期)

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

## 中国A股公司简介(回测)

- **英文表名**: `AShareIntroductionBT`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录用于回测的中国A股公司简介，包括历史数据，以满足回测策略的需求。

## 中国A股定期报告披露日期(回测)

- **英文表名**: `AShareIssuingDatePredictBT`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录用于回测的中国A股定期报告披露日期数据，包括修改时间、实际披露日期、更正公告披露日期等。

## 中国A股增发(回测)

- **英文表名**: `AShareSEOBT`
- **更新频率**: day
- **全量产品**: 否
- **说明**: 记录用于回测的中国A股增发信息，包含所有数据的历次修改都有记录，满足回测策略对于数据准确性要求。
- **业务主键**: `OBJECT_ID` (对象ID)

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

## 中国A股指数基本资料(增量)

- **英文表名**: `AIndexDescriptionZL`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

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

## 香港股票资产负债表（简表）

- **英文表名**: `HKBalanceSheetSimple`
- **更新频率**: day
- **全量产品**: 否

## 香港股票现金流量表（简表）

- **英文表名**: `HKCashFlowSimple`
- **更新频率**: day
- **全量产品**: 否

## 香港股票利润表（简表）

- **英文表名**: `HKIncomeSimple`
- **更新频率**: day
- **全量产品**: 否

## 期货市场

- **英文表名**: `FuturesNews`
- **更新频率**: nan
- **全量产品**: 否
- **说明**: 记录期货市场的相关新闻

## 中国A股公司公告(废弃)

- **英文表名**: `AShareCompanyfilings`
- **更新频率**: day
- **全量产品**: 否

## 中国A股财务科目与附注对应表(废弃)

- **英文表名**: `AshareFinancialaccounts`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `REPORT_PERIOD` (报告期), `STATEMENT_TYPE` (报表类型), `SUBJECT_CHINESE_NAME` (科目中文名), `CLASSIFICATION_NUMBER` (分类序号), `S_INFO_DATATYPE` (数据类型), `ANN_ITEM` (项目公布名称)

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

## 中国A股股权转让(恒指专用)

- **英文表名**: `AShareEquityTransfer`
- **更新频率**: day
- **全量产品**: 否

## 中国A股收购兼并（恒指专用）

- **英文表名**: `AShareMergersAcquisitions`
- **更新频率**: day
- **全量产品**: 否

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

## 中国期货Wind代码变更表

- **英文表名**: `CFuturesChangeWindcode`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码), `CHANGE_DATE` (代码变更日期)

## 中国期货行业代码

- **英文表名**: `CFuturesIndustriesCode`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `INDUSTRIESCODE` (板块代码)

## 中国期货公司简介

- **英文表名**: `CFuturesIntroduction`
- **更新频率**: day
- **全量产品**: 是
- **业务主键**: `S_INFO_COMPCODE` (公司ID)

## 中国期货类型编码表

- **英文表名**: `CFuturesTypeCode`
- **更新频率**: day
- **全量产品**: 否

## 中国期货Wind兼容代码

- **英文表名**: `CFuturesWindCustomCode`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

## 全球行业板块(废弃)

- **英文表名**: `GICSCode`
- **更新频率**: day
- **全量产品**: 是

## 股转系统Wind兼容代码

- **英文表名**: `NEEQSWindCustomCode`
- **更新频率**: day
- **全量产品**: 否
- **业务主键**: `S_INFO_WINDCODE` (Wind代码)

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

## AB股周收益率

- **英文表名**: `TB_OBJECT_5005`
- **更新频率**: nan
- **全量产品**: 否

## AB股月收益率

- **英文表名**: `TB_OBJECT_5006`
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

## 期货合约基本资料

- **英文表名**: `TB_OBJECT_3511`
- **更新频率**: nan
- **全量产品**: 否

## 国债期货可交割券转换因子

- **英文表名**: `TB_OBJECT_3591`
- **更新频率**: nan
- **全量产品**: 否

## 人民币中间价及中国银行外汇牌价

- **英文表名**: `TB_OBJECT_1233`
- **更新频率**: nan
- **全量产品**: 否

## 基金基本资料和发行

- **英文表名**: `TB_OBJECT_1099`
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

## 基金申购与赎回情况

- **英文表名**: `TB_OBJECT_1495`
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

## 申万指数成份明细

- **英文表名**: `SWIndexMembers`
- **更新频率**: day
- **全量产品**: 是
- **说明**: 记录A股申万指数成份明细信息
- **业务主键**: `S_INFO_WINDCODE` (指数Wind代码), `S_CON_WINDCODE` (成份股Wind代码), `S_CON_INDATE` (纳入日期)

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
