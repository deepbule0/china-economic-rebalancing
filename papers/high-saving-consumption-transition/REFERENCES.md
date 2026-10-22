# References and evidence map / 参考文献与证据索引

Research cutoff / 检索截止：2026-10-22。References are numbered consistently in both papers. Official statistics and original research are distinguished from the paper's own inferences. / 两种语言使用相同编号；官方统计、原始研究与本文推论分别标明。

## [1] World Bank: World Development Indicators

- [Household and NPISH final consumption/GDP](https://data.worldbank.org/indicator/NE.CON.PRVT.ZS)
- [Government final consumption/GDP](https://data.worldbank.org/indicator/NE.CON.GOVT.ZS)
- [Total final consumption/GDP](https://data.worldbank.org/indicator/NE.CON.TOTL.ZS)
- [Gross capital formation/GDP](https://data.worldbank.org/indicator/NE.GDI.TOTL.ZS)
- [Gross national saving/GDP](https://data.worldbank.org/indicator/NY.GNS.ICTR.ZS)
- [Gross domestic saving/GDP](https://data.worldbank.org/indicator/NY.GDS.TOTL.ZS)
- [Current account/GDP](https://data.worldbank.org/indicator/BN.CAB.XOKA.GD.ZS)

**Use / 用途：** 2024 common aggregate table, 2000-2024 time series, and reconciliation residuals. Raw JSON and API URLs are frozen in `data/raw/` and `data/wdi_manifest.json`. API database date: 2026-10-08. WDI source attribution and applicable data terms remain in force; the data pages identify CC BY 4.0, subject to provider exceptions. / 统一总量比较与历史序列；保留完整原始响应及查询地址。核算残差是本文计算结果。

## [2] National Bureau of Statistics of China (2025), China Statistical Yearbook 2025

- [Yearbook index](https://www.stats.gov.cn/sj/ndsj/2025/indexch.htm)
- [Table 3-15, flow of funds, nonfinancial transactions, 2023](https://www.stats.gov.cn/sj/ndsj/2025/html/C03-15.jpg)
- [Table 3-18, gross disposable income by sector](https://www.stats.gov.cn/sj/ndsj/2025/html/C03-18.jpg)
- [Table 3-1, GDP and GNI](https://www.stats.gov.cn/sj/ndsj/2025/html/C03-01.jpg)

**Use / 用途：** Chinese sectoral amounts, same-table GDP, household saving-rate calculation, and the 1992-2010-2023 household income-share trajectory. Image tables were visually read, with relevant entries transcribed into the accompanying CSV; the official images are linked rather than republished. / 中国部门原始金额、同表GDP、住户储蓄率与收入份额轨迹。不是从居民调查的收入和消费相减所得。

## [3] OECD, Household savings: indicator definition

[Definition](https://www.oecd.org/en/data/indicators/household-savings.html)

**Use / 用途：** Net saving, pension entitlement adjustment, household and NPISH perimeter. This definition page alone does not establish a five-country same-vintage saving-rate table. / 解释净储蓄、养老金权益调整及住户和非营利机构口径；定义页不能代替数值数据集。

## [4] European Commission, IMF, OECD, United Nations and World Bank (2009), System of National Accounts 2008

[Full manual](https://unstats.un.org/unsd/nationalaccount/docs/SNA2008.pdf)

**Relevant chapters / 相关章节：** 3-4, 8-11, 16, 22, 24, 26. **Use / 用途：** Historical accounting conventions for sector boundaries, saving, social transfers in kind, capital accounts, and external accounts. A newer SNA edition exists, but its publication does not imply that historical country series have all been recompiled. / 本文历史序列所用核算概念；新标准发布不等于各国既往序列已经同步重编。

## [5] World Bank (2025), China Economic Update, December 2025: Advancing Reforms, Enhancing Prospects

[Report](https://thedocs.worldbank.org/en/doc/600cd53e2bb24d516b8c3489e5d2c187-0070012025/original/CEU-December-2025-EN.pdf)

**Locator / 位置：** Special Focus III, printed pp.20-27. **Use / 用途：** Household saving, financial intermediation, risk, and portfolio discussion. The report's 31.3% figure is retained as its own reported series, not silently relabeled as the NBS flow-of-funds gross saving rate. / 31.3%仅作为该报告的系列，未冒充本文同表计算的34.92%。

## [6] World Bank (2026), China Economic Update, July 2026

[Report](https://thedocs.worldbank.org/en/doc/0cb2fc6dd88d4db3816dc0433b5cb49b-0070012026/original/CEU-July-2026-EN.pdf)

**Locator / 位置：** Recent developments, printed pp.5-6. **Use / 用途：** Q1 real household consumption growth of 2.6%, a reported saving rate of 32.4% on a four-quarter moving average, and household caution. These are report-specific measures. / 季度诊断，不与年度部门口径作直接排名。

## [7] IMF (2026), People's Republic of China: 2025 Article IV Consultation, Country Report 26/044

[Staff report](https://www.imf.org/-/media/files/publications/cr/2026/english/1chnea2026001-source-pdf.pdf)

**Locator / 位置：** Sections on fiscal policy, property adjustment, and reducing household savings; especially paragraphs 48-53. **Use / 用途：** Contemporary macroeconomic diagnosis and policy tradeoffs, with authorities' views distinguishable from staff recommendations. The paper does not treat staff forecasts as outcomes. / 区分工作人员建议、中方观点与预测值。

## [8] Chamon, Marcos, and Eswar Prasad (2010), Why Are Saving Rates of Urban Households in China Rising?

American Economic Journal: Macroeconomics, 2(1), 93-130. [DOI](https://doi.org/10.1257/mac.2.1.93). Earlier research version: [NBER Working Paper 14546](https://www.nber.org/papers/w14546), 2008.

**Use / 用途：** Historical evidence and mechanisms relating saving to housing, health, and education responsibilities. Historical sample findings are not asserted as current causal coefficients. / 历史机制证据，未将历史系数直接外推至2026年。

## [9] Chamon, Marcos, Kai Liu, and Eswar S. Prasad (2010), Income Uncertainty and Household Savings in China

IMF Working Paper 10/289. [Paper page](https://www.imf.org/en/publications/wp/issues/2016/12/31/income-uncertainty-and-household-savings-in-china-24497)

**Use / 用途：** Income uncertainty, pension reform, and a buffer-stock saving mechanism. Model calibration does not independently identify the entire macroeconomic effect of a present-day reform. / 收入风险、养老金及缓冲储蓄机制。

## [10] Xu, Yizhi, Fan Zhang, Rongyu Cui, and Ding Hua (2025), Reforms to Reduce China's High Household Savings

IMF Working Paper 25/259. [Paper page](https://www.imf.org/en/publications/wp/issues/2025/12/12/reforms-to-reduce-chinas-high-household-savings-572507). [PDF](https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025259-source-pdf.pdf). [DOI](https://doi.org/10.5089/9798229033367.001).

**Use / 用途：** Rural social spending, Hukou, and housing wealth/downpayment mechanisms. Working papers reflect authors' analysis rather than automatically being the IMF's institutional policy. / 农村保障、户籍与住房机制；研究论文不等于机构正式政策。

## [11] Chen, Peter, Loukas Karabarbounis, and Brent Neiman (2017), The Global Rise of Corporate Saving

Journal of Monetary Economics, 89, 1-19. [NBER Working Paper 23133](https://www.nber.org/papers/w23133). [Original working paper PDF](https://www.nber.org/system/files/working_papers/w23133/w23133.pdf).

**Use / 用途：** Global corporate-saving context and the distinction between household and corporate income accumulation. Does not prove that one country's retained earnings are all inefficient. / 企业储蓄的全球背景，不支持将全部留存收益视为浪费。

## [12] OECD (2026), OECD Economic Surveys: Japan 2026

[Report](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/05/oecd-economic-surveys-japan-2026_9457bba4/54cc833d-en.pdf)

**Locator / 位置：** Table 1.1, printed p.23; corporate saving-investment discussion, printed p.81. **Use / 用途：** Calendar-year 2024 net household saving rate of 0.7% in this vintage and a persistent corporate saving-investment surplus. Cash holdings discussed by OECD are stocks and are not treated as annual saving. / 0.7%为该版本日历年净储蓄率；公司现金存量不等于年度储蓄。

## [13] Economic and Social Research Institute, Cabinet Office of Japan (2025), Annual Report on National Accounts for 2024: Flow Accounts

[Official summary, 23 December 2025](https://www.esri.cao.go.jp/en/sna/data/kakuhou/files/2024/pdf/point_flow_en20251223.pdf)

**Locator / 位置：** Household disposable income and saving, PDF pp.8-9. **Use / 用途：** FY2024 household net saving of JPY2.6 trillion and saving ratio of 0.8%. Fiscal-year and calendar-year values are not interchangeable. / 财政年0.8%与OECD日历年0.7%不可混写。

## [14] OECD (2024), OECD Economic Surveys: Korea 2024

[Report](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/07/oecd-economic-surveys-korea-2024_9343c046/c243e16a-en.pdf)

**Locator / 位置：** Printed p.53, Figure 3.3 and surrounding text. **Use / 用途：** High corporate saving, business investment, and diminishing scope for capital-deepening-led catch-up. Report language and figure dates are not converted into an exact 2024 departmental observation. / 不用图形目测值构造精确年度排名。

## [15] OECD (2026), OECD Economic Surveys: Korea 2026

[Report](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/07/oecd-economic-surveys-korea-2026_17d6bf02/6b87f585-en.pdf)

**Locator / 位置：** Housing and household debt, printed p.28; broader discussions of aging and productivity. **Use / 用途：** Household vulnerabilities and fiscal/service reform tradeoffs. / 家庭债务、住房压力与老龄化背景。

## [16] IMF (2026), Singapore: 2026 Article IV Consultation, Country Report 26/185

[Official indexed report text](https://www.elibrary.imf.org/view/journals/002/2026/185/article-A001-en.xml). [Board assessment](https://www.imf.org/en/news/articles/2026/07/20/pr26253-singapore-imf-executive-board-concludes-2026-article-iv-consultation).

**Use / 用途：** Indexed official report text identifies 2025 private household saving/GDP of 17.0% and estimated private corporate saving/GDP of 16.8%. Full-report access returned an access restriction during preparation; these supplementary figures are not used for exact harmonization or sectoral reconciliation. / 全文访问受限；数值仅作补充说明，不进入统一加总。

## [17] Central Provident Fund Board, Contribution rate tables from 1 January 2026

[Official tables](https://www.cpf.gov.sg/content/dam/web/employer/employer-obligations/documents/CPFcontributionratesfrom1Jan2026.pdf). [Current contribution guide](https://www.cpf.gov.sg/employer/employer-obligations/how-much-cpf-contributions-to-pay).

**Use / 用途：** Full-rate employer/employee contributions of 17%/20% for qualifying employees aged 55 and below, subject to wage and residency conditions. Not a national saving-rate estimate. / 完整费率及其适用限制，不是全国储蓄率。

## [18] Ministry of Finance, Singapore, Net Investment Returns Contribution

[Framework](https://www.mof.gov.sg/policies/reserves/net-investment-returns-contribution/)

**Use / 用途：** NIR/NII rules, relevant assets net of government liabilities, and permitted budget use of part of expected long-term real returns. The framework is not described as spending half the principal or half each year's market gain. / 不是支用一半本金，也不是逐年市值涨幅的一半。

## [19] Board of Governors of the Federal Reserve System (2026), Financial Accounts of the United States, 19 March 2026

[Statistical release](https://www.federalreserve.gov/releases/z1/20260319/z1.pdf)

**Locator / 位置：** F.2, printed p.26; F.4, printed p.28. **Use / 用途：** 2024 GDP and sectoral net saving/depreciation to reconstruct gross saving. The broader business aggregate includes noncorporate depreciation; it is not silently equated with S11+S12. / 详细公式和原始条目见数据说明。

## [20] Bureau of Economic Analysis, NIPA Handbook, Chapter 5: Personal Consumption Expenditures

[Chapter](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-05.pdf). [Consumer spending definition](https://www.bea.gov/data/consumer-spending/main).

**Use / 用途：** Expenditure by or on behalf of households and interpretation of PCE. Does not establish that medical spending translates one-for-one into welfare. / 第三方支付与PCE口径；支出金额不等于福利。

## [21] Social Security Administration (2026), Monthly Statistical Snapshot, September 2026

[Official statistics](https://www.ssa.gov/policy/docs/quickfacts/stat_snapshot/)

**Use / 用途：** Evidence that substantial public retirement/disability/survivor income support exists in the United States. The live page can roll forward after the research cutoff. / 证明公共保障制度确实存在；页面会随时间更新。

## [22] Congressional Budget Office (2026), The Budget and Economic Outlook: 2026 to 2036

[Report, February 2026](https://www.cbo.gov/publication/62105)

**Use / 用途：** Conditional current-law projections of federal debt held by the public and fiscal pressures. This measure differs from general government gross debt. / 公众持有联邦债务口径，不与广义政府总债务混同。

## [23] Ministry of Finance, China (2026), Report on the Execution of the Central and Local Budgets for 2025 and Draft Budgets for 2026

[Official report, 16 March 2026](https://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/202603/t20260316_3985331.htm)

**Use / 用途：** 2025 government-managed fund revenue, its decline, and the role of land-conveyance receipts. Government-managed funds are not identical to all local recurrent revenue. / 基金预算不等于全部地方经常性收入。

## [24] Ministry of Finance, China (2026), Fiscal Revenue and Expenditure, January-August 2026

[Official release, 18 September 2026](https://gks.mof.gov.cn/tongjishuju/202609/t20260918_3997709.htm)

**Use / 用途：** Continued land-revenue pressure as reported in this release, without claiming this was the latest release available on every subsequent date. / 只支持该期财政诊断，不声称永远是最新数据。

## [25] IMF (2026), External Sector Report

[Report](https://www.imf.org/-/media/files/publications/esr/2026/english/text.pdf). [Economy assessments](https://www.imf.org/-/media/files/publications/esr/2026/english/ch2.pdf).

**Use / 用途：** Global external-balance context and structural interpretation. Normative recommendations and the coordinated-adjustment framework in the paper are the paper's own synthesis. / 全球背景；本文的协调改革方案是独立综合判断。

## [26] SASAC, published account of central enterprise objectives for 2025

[Official-hosted discussion](https://wap.sasac.gov.cn/n4470048/n29955503/n32392302/n32392320/c32441870/content.html)

**Use / 用途：** Published performance targets include return on equity, refuting the blanket premise that state enterprises have no return-related assessment. Existence of a target does not establish effective implementation or an appropriate marginal social return. / 考核指标的存在不等于实际执行充分，更不等于所有投资有效。

## [27] OECD (2025), Economic Outlook 118, Statistical Annex, Table 28

[Official December 2025 annex](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/economic-outlook/eo-dec-2025/EO118_Annexes_E.pdf). Earlier comparison: [June 2025 EO117 annex](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/economic-outlook/eo117-june-2025/EO117_Annexes_E.pdf).

**Locator / 位置：** EO118 printed p.37, net saving section. **Use / 用途：** Same-vintage 2024 household net saving rates: Korea 9.6%, Japan 2.0%, United States 5.7%. Values retain this release vintage and are not substituted for newer Japan data or compared directly to gross household saving in China. / 固定版本的居民净储蓄率，不与总储蓄率混比；版本变动的原因未在本文识别。

## Evidence hierarchy / 证据层级

- **Accounting / 核算：** identities and arithmetic, which hold only with matching definitions.
- **Description / 描述：** source-specific observed data, with year and vintage retained.
- **Mechanism / 机制：** original literature and institutional evidence, with limits to external validity.
- **Synthesis / 综合判断：** the paper's argument about institutions transmitting productive gains into welfare.
- **Scenario / 情景：** assumed parameter changes and a budget stress test, not an estimated forecast.

No unpublished causal estimates, fabricated confidence intervals, journal acceptance, or official endorsement are claimed. / 未声称拥有新的因果估计、虚构置信区间、期刊录用或官方背书。
