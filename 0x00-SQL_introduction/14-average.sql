-- average sql comment
ALTER TABLE second_table
ADD average FLOAT;
INSERT INTO second_table (average)
VALUES (AVG(score));
SELECT average FROM second_table;
