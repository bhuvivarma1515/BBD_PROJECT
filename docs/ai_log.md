
# AI Usage Log

## 1. Purpose
AI assistance was used to support SQL query development, result formatting, data cleaning, and dashboard planning for the Big Billion Days Regional Performance Review.

## 2. Tasks Supported by AI
- Reviewed SQL query requirements and helped structure queries.
- Helped format query outputs in Markdown for documentation.
- Assisted in writing a Python script to clean customer names and handle missing amount values.
- Helped prepare spreadsheet cleaning notes.
- Helped design the dashboard specification, including KPI cards, charts, filters, and layout.

## 3. Data Cleaning
A Python script was used to:
- Trim leading and trailing spaces from customer names.
- Standardize customer name capitalization.
- Convert textual `null` amounts into blank CSV fields.
- Preserve all 90 order records and the original columns.

## 4. Validation
- Confirmed that the cleaning script processed 90 orders.
- Checked the generated CSV output.
- Compared documented KPI values against SQL query results.

## 5. Human Review
AI-generated suggestions and code were reviewed by the project author. Query outputs and data-cleaning results were checked before inclusion in the project.

## 6. Limitations
- AI suggestions may contain errors and require verification.
- Missing amounts were left blank rather than assumed to be zero.
- Dashboard recommendations describe a proposed design; the dashboard itself must be built and validated separately.
