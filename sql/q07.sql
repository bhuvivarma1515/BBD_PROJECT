
-- Business question: Which products generated more than 20000 in completed-order revenue?
SELECT
    item,
    COUNT(*) AS number_of_orders,
    SUM(amount) AS revenue
FROM orders
WHERE status = 'completed'
GROUP BY item
HAVING SUM(amount) > 20000
ORDER BY revenue DESC;

