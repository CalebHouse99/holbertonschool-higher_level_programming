-- group it up
SELECT DISTINCT score, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
