# From Capital Accumulation to Household Welfare
# 从资本积累到居民福利

**A bilingual research working paper on sectoral saving, fiscal institutions, and China's consumption transition.**  
**关于部门储蓄、财政制度与中国消费转型的中英文研究工作论文。**

Version 1.0 · 22 October 2026 / 2026年10月22日

| Language / 语言 | Full paper / 正文 | Download / 下载 |
| --- | --- | --- |
| 简体中文 | [中文论文](paper.zh-CN.md) | [中文PDF](output/pdf/saving-consumption.zh-CN.pdf) |
| English | [English paper](paper.en.md) | [English PDF](output/pdf/saving-consumption.en.pdf) |

The paper compares **China, Japan, Korea, Singapore, and the United States**, starting with a common 2024 World Bank baseline and explicitly qualified national sector accounts. It examines who receives income, who bears risk, how saving is invested, and how returns reach households. The aim is sustainable household welfare, rather than maximizing or minimizing one saving or consumption ratio.

论文比较**中国、日本、韩国、新加坡与美国**，以2024年世界银行同一数据快照为总量基准，对国家部门账户逐项标明口径。核心问题是：收入归谁、风险由谁承担、储蓄如何投资、收益如何回到居民。最终评价标准是长期居民福利，而非单一储蓄率或消费率。

## Research materials / 研究材料

- [References and evidence map / 27项参考文献与证据索引](REFERENCES.md)
- [Data definitions, corrections, and limitations / 口径修正与局限](DATA_NOTES.md)
- [Development of the argument / 核心知识轨迹](RESEARCH_TRAJECTORY.md)
- [Common 2024 baseline / 统一总量基准](data/baseline_2024.csv)
- [2000-2024 WDI observations / 历史序列](data/wdi_long.csv)
- [Chinese 2023 source transcription / 中国部门原始数据录入](data/china_2023_source.csv)
- [US 2024 source transcription / 美国部门原始数据录入](data/us_2024_source.csv)
- [Accounting reconciliation / 核算残差](data/reconciliation_2024.csv)
- [Illustrative scenarios / 核算情景](data/accounting_scenarios.csv)

## Reproduce / 复核

From this directory, with Python 3 and the packages in `requirements.txt`:

```bash
# Reproduce calculations and figures from the frozen source data.
python scripts/analyze.py

# Rebuild both PDFs. For fully embedded Chinese glyphs, provide a local
# Noto Sans SC variable TrueType font as CJK_FONT.
CJK_FONT=/absolute/path/NotoSansSC-VF.ttf python scripts/build_pdf.py

# OPTIONAL: download live WDI data. This overwrites the frozen WDI snapshot.
# Keep the published snapshot for exact replication of this release.
python scripts/fetch_wdi.py
```

`fetch_wdi.py` uses the Python standard library. The PDF builder can use ReportLab's CID fallback if an embedded CJK font is unavailable; final release PDFs use embedded font subsets. Font source: [Google Fonts, Noto Sans SC](https://github.com/google/fonts/tree/main/ofl/notosanssc). Font redistribution terms remain with its source.

公开版本冻结875个国家-年份-指标槽位（缺失值保留为空），并保留原始API响应、查询地址和数据库更新时间。重新获取在线数据可能得到修订值；它不等于精确重现当前版本。日本、韩国与其他国家尚未形成完整同年同口径部门面板，论文明确保留这一限制。

## Status and attribution / 文稿状态与归属

Research initiated and published by **deepbule0**, with ChatGPT assistance in research organization, source checking, drafting, translation, and document production. It is a **public working paper, not a peer-reviewed journal publication**. The paper does not claim new causal estimates or official endorsement. Policy suggestions and numerical scenarios are clearly distinguished from observations and government announcements.

研究由**deepbule0**发起并发布，ChatGPT辅助完成资料整理、来源核对、写作、翻译和文稿制作。本文为**公开研究工作论文，尚非通过期刊同行评审的论文**。事实、核算推导、机制假说、政策建议与示意情景分别标示。
