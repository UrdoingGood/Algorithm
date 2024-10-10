SELECT *
FROM animal_outs;

SELECT *, HOUR(datetime) AS "HOUR"
FROM animal_outs;

SELECT HOUR, COUNT(*) AS "COUNT"
FROM (
    SELECT *, HOUR(datetime) AS "HOUR"
    FROM animal_outs
) AS ao
WHERE HOUR BETWEEN 9 AND 19
GROUP BY HOUR
ORDER BY HOUR;