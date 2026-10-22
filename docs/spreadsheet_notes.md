
# Spreadsheet Cleaning Notes

## 1. Source Data
The source file was `DATA/orders_enriched.csv`, containing 90 order records and 10 columns.

## 2. Data Cleaning Steps
- Removed leading and trailing spaces from customer first and last names.
- Standardized customer name capitalization using title case.
- Converted missing amounts represented as `null` into blank CSV fields.
- Preserved all 90 order records and the original column structure.

## 3. Output File
The cleaned data was saved as `DATA/orders_clean.csv`.

## 4. Validation
- Total records processed: 90
- Expected columns: 10
- Missing amounts were left blank, not replaced with zero.
- Order IDs, order months, regions, sales representatives, products, quantities, and statuses were preserved.

## 5. Limitation
Only customer name formatting and missing amount representation were changed. No order records were removed.
