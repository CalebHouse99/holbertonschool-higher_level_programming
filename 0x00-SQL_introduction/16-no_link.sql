-- no link
SELECT score, name FROM second_table 
WHERE EXISTS (SELECT name from second_table)
ORDER BY score DESC;
