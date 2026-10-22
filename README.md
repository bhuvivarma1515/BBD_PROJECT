# Big Billion Days Regional Performance Review

## Project Overview

This project analyzes regional sales performance during a three-month Big Billion Days sales period, from September to November 2026. It uses SQL queries, CSV data cleaning, and dashboard planning to examine order statuses, product revenue, regional trends, customer profiles, and sales representative performance.

## Objectives

- Analyze completed orders and calculate headline sales KPIs.
- Identify high-performing products and customer segments.
- Compare monthly revenue across regions.
- Evaluate sales representative performance against monthly targets.
- Clean and prepare order data for spreadsheet analysis.
- Document query results and propose a business dashboard.

## Project Structure

```text
BBD_PROJECT/
├── README.md
├── sql/
│   ├── 00_schema_and_seed.sql
│   ├── q01.sql
│   ├── q02.sql
│   ├── q03.sql
│   ├── q04.sql
│   ├── q05.sql
│   ├── q06.sql
│   ├── q07.sql
│   ├── q08.sql
│   ├── q09.sql
│   ├── q10.sql
│   ├── q11.sql
│   ├── q12.sql
│   ├── q13.sql
│   └── d1_corrected.sql
├── data/
│   ├── orders_enriched.csv
│   └── orders_clean.csv
├── results/
│   └── query_results.md
└── docs/
    ├── spreadsheet_notes.md
    ├── dashboard_spec.md
    └── ai_log.md
```

## Tools Used

- SQLite for relational data queries.
- Visual Studio Code for editing project files.
- Python for CSV data cleaning.
- CSV and Markdown for data exchange and documentation.
- GitHub for version control and project submission.

## Data Description

The enriched order dataset contains 90 order records and 10 columns:

- `order_id`
- `order_month`
- `first_name`
- `last_name`
- `region`
- `rep_name`
- `item`
- `quantity`
- `amount`
- `status`

The data covers September, October, and November 2026.

## SQL Analysis

Thirteen SQL queries address questions about pending orders, missing amounts, largest completed orders, customer segments, headline KPIs, order status distribution, product performance, customer profiles, enriched order data, customer order counts, regional monthly performance, product revenue tiers, and sales representative targets.

Detailed query outputs are documented in `results/query_results.md`.

## Data Cleaning

The Python script `clean_order.py` creates the cleaned dataset from the enriched CSV file. It:

- Trims leading and trailing spaces from customer names.
- Standardizes customer name capitalization.
- Converts textual `null` amounts into blank CSV fields.
- Preserves all 90 order records and the original 10-column structure.

The cleaned output is saved as `data/orders_clean.csv`.

## Revenue Definition

Revenue is calculated using completed orders only. Pending and disputed orders are excluded from completed revenue calculations. Missing amounts are kept blank rather than being treated as zero.

## Key Results

- Completed orders: 63
- Completed revenue: 346,200
- Average completed order value: approximately 5,495.24
- Highest-revenue product: Air Fryer, with revenue of 104,000
- Revenue analysis covers four regions: East, North, South, and West.

These figures are based on the recorded SQL query outputs and should be reconciled against the final query results before submission.

## Dashboard Plan

The proposed dashboard includes KPI cards, monthly revenue trends by region, product revenue rankings, order status distribution, and sales representative performance against targets. The specifications are documented in `docs/dashboard_spec.md`.

## AI Usage and Validation

AI assistance was used during query development, result documentation, Python data cleaning, and dashboard planning. The project includes `docs/ai_log.md` to document this assistance.

Generated code and analytical results should be reviewed and validated before final submission.

## Project Status

This repository documents the SQL analysis, data cleaning, query results, and proposed dashboard design. The final repository structure, required SQL files, and submission setup must be verified before submission.
