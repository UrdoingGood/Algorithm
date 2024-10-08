SELECT 
    COUNT(id) AS fish_count
FROM fish_info
WHERE time BETWEEN '2021-01-01' AND '2021-12-31';