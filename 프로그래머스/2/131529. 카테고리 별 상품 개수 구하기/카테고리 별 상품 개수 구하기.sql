SELECT p.category, COUNT(p.product_id) AS 'product'
FROM (
    SELECT *, SUBSTRING(product_code,1 ,2) AS 'category'
    FROM product 
) AS p
GROUP BY p.category
ORDER BY p.product_code;