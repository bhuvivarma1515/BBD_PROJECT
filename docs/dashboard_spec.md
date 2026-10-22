
# Big Billion Days Regional Performance Dashboard

## 1. Objective
Build a dashboard to evaluate regional sales performance, identify strong products, track monthly revenue, and assess sales representative performance against targets.

## 2. Data Source
- File: `DATA/orders_clean.csv`
- Records: 90 orders
- Time period: September–November 2026
- Revenue is calculated using completed orders only.
- Pending and disputed orders are excluded from revenue calculations.

## 3. KPI Cards
Display these KPI cards at the top of the dashboard:

1. Total completed orders: 63
2. Total completed revenue: 346,200
3. Average order value: 5,495.24
4. Number of regions: 4

## 4. Recommended Charts

### Chart 1: Monthly Revenue by Region
- Type: Line chart
- X-axis: Order month
- Y-axis: Revenue
- Color: Region
- Purpose: Compare monthly revenue trends across regions.

### Chart 2: Revenue by Product
- Type: Horizontal bar chart
- Y-axis: Product
- X-axis: Revenue
- Sort: Highest to lowest
- Purpose: Identify top- and low-revenue products.

### Chart 3: Orders by Status
- Type: Donut chart
- Categories: Completed, Pending, Disputed
- Values: Number of orders
- Purpose: Show the distribution of order statuses.

### Chart 4: Sales Representative Performance
- Type: Grouped bar chart
- Categories: Sales representative
- Values: Monthly revenue and monthly target
- Purpose: Compare actual revenue against targets.

## 5. Filters
Provide filters for:
- Order month
- Region
- Product
- Sales representative
- Order status

## 6. Dashboard Layout
1. Title and filters at the top.
2. KPI cards directly below the title.
3. Monthly revenue trend in the main section.
4. Product revenue and order status charts in the middle section.
5. Sales representative performance at the bottom.

## 7. Key Business Questions
- Which region generated the most revenue?
- Which products contributed the most revenue?
- How did regional revenue change month to month?
- Which sales representatives met or exceeded their targets?
- What proportion of orders are pending or disputed?

## 8. Data Rules
- Revenue = SUM(amount) for completed orders only.
- Missing amounts must not be treated as zero-value sales.
- Pending and disputed orders must not be counted as completed revenue.
- Dashboard figures should reconcile with the SQL query results.
