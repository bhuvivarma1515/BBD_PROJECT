
-- Business question: What are the completed-order revenue and customer counts by region and month?
-- INNER JOIN is used to include orders with matching customers.
-- COUNT(DISTINCT ...) prevents repeat orders by one customer from being counted multiple times.
SELECT
    c.region,
    o.order_month,
    COUNT(o.order_id) AS number_of_orders,
    COUNT(DISTINCT o.customer_id) AS number_of_customers,
    SUM(o.amount) AS total_revenue,
    AVG(o.amount) AS average_revenue
FROM orders AS o
JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE o.status = 'completed'
GROUP BY c.region, o.order_month
ORDER BY c.region ASC, o.order_month ASC;

