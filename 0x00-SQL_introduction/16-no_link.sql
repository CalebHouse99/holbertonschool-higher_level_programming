-- List all records of table
SELECT score, name FROM second_table 
WHERE EXISTS (SELECT name FROM second_table)
ORDER BY score DESC;
