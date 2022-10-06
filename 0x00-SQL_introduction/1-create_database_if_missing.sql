-- The CREATE command creates something, go figure
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hbtn_0c_0')
BEGIN
  CREATE DATABASE hbtn_0c_0;
END;
GO