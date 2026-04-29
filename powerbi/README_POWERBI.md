Power BI assets for AI Data with Copilot and Pencil

Files:
- Student_Placement_Skills_2025_cleaned.csv  -- cleaned CSV to use as data source
- power_query_transform.m                      -- Power Query (M) script to load and transform the CSV

How to open in Power BI Desktop:
1. Open Power BI Desktop.
2. Get Data -> Text/CSV and select Student_Placement_Skills_2025_cleaned.csv. Click Transform Data.
3. In Power Query Editor, Advanced Editor -> replace contents with the M script from power_query_transform.m (or use 'Run New Source' and point to the CSV). This will create a table with typed columns and a 'Placed' column (0/1).
4. Close & Apply.

Suggested model & measures (DAX):
- Placement Rate = DIVIDE(SUM(Table[Placed]), COUNT(Table[Student_ID]))
- Avg CGPA = AVERAGE(Table[CGPA])
- Avg Salary (Placed) = CALCULATE(AVERAGE(Table[Salary_Offered_USD]), FILTER(Table, Table[Placed] = 1))

Suggested visuals:
- KPI tiles for Placement Rate, Avg CGPA, Avg Salary (Placed)
- Stacked/clustered bar: Placement Rate by Degree (use measure with percentage)
- Box plot or violin (custom visual) for Salary distribution by Degree (filter to placed)
- Heatmap / correlation matrix: use Python/R visual or matrix with conditional formatting
- Slicers: Degree, Gender, Age range, Certifications range
- Drillthrough: Student details page showing individual record
- Bookmarks & buttons for storytelling (Before vs After filters)

Interactivity tips:
- Use bookmarks to create narrative states
- Use drillthrough on Degree -> Student detail
- Add report-level filters for cohort selection (e.g., Age group)

Automating updates:
- Save PBIX locally; set data source to the CSV in the repo and use Refresh to regenerate visuals after CSV changes.
- For cloud automation use Power BI Service with scheduled refresh and a gateway (if CSV is on-prem).

