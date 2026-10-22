# Data notes and corrections / 数据口径、复核与修正

## 1. Aggregate baseline / 总量基准

`data/baseline_2024.csv` contains seven WDI indicators for CHN, JPN, KOR, SGP, and USA. `data/wdi_long.csv` retains 2000-2024 observations, including blanks for missing data. Raw responses and `wdi_manifest.json` preserve precision and source-update metadata. Each country-indicator-year observation is unique. A blank is not zero.

统一基准为2024日历年、当前价格、GDP百分比。消费、资本形成和储蓄保留各自定义；国民储蓄不是可以与消费、投资相加的GDP支出项。总量表使用同一WDI数据快照，部门表使用明确标注的国家来源，不假装已完全统一。

## 2. Chinese sector accounts / 中国部门账户

Source: NBS Statistical Yearbook 2025, table 3-15, 2023 nonfinancial transactions. Units below are **RMB100 million / 亿元**. These are visually verified transcriptions of the original image table, not OCR-only readings.

| Item / 项目 | Amount / 金额 |
| --- | ---: |
| GDP / 国内生产总值 | 1,294,271.7 |
| Household disposable income / 住户可支配总收入 | 786,890.6 |
| Household adjusted disposable income / 调整后可支配总收入 | 877,478.2 |
| Household actual final consumption / 住户实际最终消费 | 602,708.2 |
| Household gross saving / 住户总储蓄 | 274,770.1 |
| Nonfinancial enterprise gross saving / 非金融企业总储蓄 | 246,213.7 |
| Financial institution gross saving / 金融机构总储蓄 | 41,341.9 |
| General government gross saving / 广义政府总储蓄 | -11,332.7 |
| Total gross saving / 国内机构部门总储蓄合计 | 550,992.9 |

Calculated results / 本文计算：

- Household saving/GDP = 21.2297078%; corporate total = 22.2175607%; government = -0.8756044%; reported total = 42.5716563%; component sum = 42.5716640% (a 0.1-unit source-rounding difference).
- Household gross saving/disposable income = 34.9184626%.
- Household disposable income/GDP = 60.7979453%.
- Household final consumption expenditure reconstructed as disposable income minus saving = 512,120.5; consumption/GDP = 39.5682375%.
- Actual final consumption minus social transfers in kind gives a value differing by RMB10 million at the displayed precision because original entries are rounded. It is not a substantive discrepancy.

The table reports actual final consumption after transfers in kind. Subtracting that consumption from unadjusted disposable income would mix concepts. Corporate saving combines financial and nonfinancial institutions; it does not identify SOE saving. / 住户实际消费与未调整收入不可直接相减；企业总量不能分离国企。

Table 3-18 household shares of total sectoral disposable income: 68.9% (1992), 56.7% (2010), 61.2% (2023). These are not GDP shares. A narrative of uninterrupted decline is inconsistent with this series. / 该份额先降后升，分母不是GDP。

The World Bank December 2025 report separately states a 2023 household saving rate of 31.3%. Its exact bridge to the NBS entries above has not been established here. It is neither silently relabeled as net saving nor forced to reconcile with 34.92%. / 未查明桥接差异，不猜测差额全部来自折旧、调查误差或某一个制度项目。

## 3. United States / 美国

Frozen vintage: Fed Z.1, 19 March 2026; F.2 and F.4. **USD billions / 十亿美元**:

| 2024 item / 项目 | Value |
| --- | ---: |
| GDP | 29,298.0 |
| Household/institution net saving, F.4 line 7 | 1,193.2 |
| Household/institution depreciation, line 17 | 878.3 |
| Nonfinancial corporate net saving, line 5 | 651.3 |
| Nonfinancial corporate depreciation, line 14 | 2,274.4 |
| Financial business net saving, line 6 | 244.4 |
| Financial business depreciation, line 16 | 344.8 |
| Broad domestic business net saving, line 4 | 895.7 |
| Broad domestic business depreciation, line 13 | 3,114.6 |
| Government net saving, line 8 | -2,053.2 |
| Government depreciation, line 18 | 803.8 |

Calculations / 公式：

- Household gross saving = 1,193.2 + 878.3 = 2,071.5; / GDP = 7.0704485%.
- Corporate proxy = 651.3 + 2,274.4 + 244.4 + 344.8 = 3,514.9; / GDP = 11.9970646%.
- Broad business = 895.7 + 3,114.6 = 4,010.3; / GDP = 13.6879650%.
- Government gross saving = -2,053.2 + 803.8 = -1,249.4; / GDP = -4.2644549%.

The corporate proxy uses the source labels “nonfinancial corporate business” and “financial business.” It is closer to a company comparison than broad business, but it is not claimed to be a full SNA-recompiled S11+S12 series. Broad business depreciation includes noncorporate enterprises, while their income/saving is treated differently across accounting frameworks. / 12.00%亦保留原部门标签，并非宣布完成SNA统一重编。

The resulting national total is about 16.49% of GDP in this Fed vintage, versus WDI's 16.59%. The difference is retained, not hidden. / 不将不同修订版本硬拼成精确加总。

## 4. Japan, Korea, Singapore / 日本、韩国与新加坡

Japan's 0.7% OECD calendar-year net household saving rate and 0.8% ESRI fiscal-year rate are separate observations. Neither is gross saving/GDP. A separately frozen EO118 table reports 2024 net rates of 9.6% (Korea), 5.7% (United States), and 2.0% (Japan). EO117 reports a different 2024 Korean value of 3.5%; both releases have been checked, but the reason for the vintage change is not identified here. They must not be mixed. Figure readings for Korean/Japanese corporate saving are not used as exact observations.

日本0.7%与0.8%的年度和口径已分开。另固定EO118的日韩美2024年净储蓄率为9.6%、2.0%、5.7%；已核对EO117的韩国2024年列为3.5%，但不声称查明其版本差异的具体原因。关于日韩企业储蓄的图形读数被正式报告的可核对叙述取代。

Singapore's 17.0% household and 16.8% estimated private corporate saving/GDP refer to 2025 and private-sector definitions in indexed IMF text. Full report access was restricted. No government residual is inferred by subtracting them from a 2024 national total. CPF contribution rates are not saving rates and must not be added to those ratios.

## 5. Reconciliation / 核算残差

`data/reconciliation_2024.csv` reports:

- `consumption_residual = total C - household C - government C`;
- `domestic_saving_residual = domestic S + total C - 100`;
- `saving_investment_current_account_residual = national S - I - CA`.

The first two are essentially rounding/source noise. The third can be materially nonzero across independently compiled series. For 2024 it is approximately -0.23 (China), -0.24 (Japan), -0.27 (Korea), +1.40 (Singapore), and -0.85 (United States), in GDP percentage points. It is not assigned a causal interpretation.

## 6. Scenario assumptions / 情景假设

The household scenario uses the same-table Chinese 2023 baseline. Income share rises by 0.03 and the saving propensity falls by 0.05. Exact decomposition:

`change in consumption share = (1 - s0) × change in h - h0 × change in s - change in h × change in s`

The approximate effects are +1.95, +3.04, and +0.15 GDP percentage points, totaling +5.14. This is an identity-based counterfactual, not a forecast or a fiscal multiplier. The separate 1.5% GDP budget stress test is not linked to these changes by an estimated behavioral model.

## 7. What is not established / 未被证明的事项

This release does not estimate culture's contribution, the share of precautionary saving in Chinese household saving, a causal effect of SOE ownership, a universal optimal consumption share, or the probability/timing of future reform. It does not provide a complete harmonized sectoral panel for all five countries. It does not infer fiscal space from gross public assets or from the size of bank deposits.

本文的贡献是可复核的描述、口径澄清与机制综合，而不是伪装成完成了新的因果识别。后续需要统计口径统一、家庭和企业微观资料，以及透明可重复的识别设计。
