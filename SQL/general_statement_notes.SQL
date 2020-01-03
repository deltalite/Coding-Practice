/* 
General SQL format 
*/
SELECT column_name(s)
FROM table_name AS alias
WHERE column_name = "Desired value"
GROUP BY column_name(s)
-- Essentially the same as "WHERE", except the condition
--   can have aggregation functions such as "COUNT"
HAVING COUNT("column_name") = "Desired agg value"
ORDER BY column_name(s)
-- MySQL 
LIMIT X OFFSET Y;
-- alternate syntax:
-- LIMIT Y, X



-- SQL Server
-- Use "TOP" in SELECT line
-- Use OFFSET Y ROWS as last row

