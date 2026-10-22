# Release validation / 发布核验

Version 1.0 · 2026-10-22

- Frozen WDI inputs: 5 economies × 25 years × 7 indicators = 875 observation slots; missing values retained, no duplicate country-year-indicator keys.
- All 30 displayed main-table values agree with the source snapshot to two decimals.
- Household/government consumption and domestic-saving identities reconcile within the stated numerical tolerance; national saving-investment-current-account residuals are disclosed rather than overwritten.
- Chinese and US sector calculations are derived from separately identified source entries; source-rounding differences are retained.
- The income-share/saving-propensity decomposition reconciles exactly in the script. Its values are not asserted as estimated policy effects.
- Main-paper reference numbers resolve to 27 numbered source entries; local manuscript links resolve to existing files.
- Chinese and English PDFs contain 14 and 18 pages, respectively, including the bibliography. Font subsets are embedded in the release PDFs.
- Every PDF page was rendered in a contact sheet. Title pages, tables, charts, and bibliography pages were additionally inspected at higher resolution. Text bounding-box checks detected no horizontal overflow or replacement characters.
- Markdown, data, scripts, charts, and PDFs are included in the release package; cached full third-party reports and temporary font/build files are excluded.

以上检查验证本次发布的数值一致性、文件完整性及排版，不等于独立复现所引用研究的因果估计，也不等于同行评审。日本和韩国的完全统一部门面板仍是研究缺口；新加坡补充部门数据的全文访问限制在正文与数据说明中保留。
