-- updates Bob's score to 10; cannot use Bob's id value, only 'name' field
UPDATE second_table SET `score` = 10 WHERE second_table.`name` ='Bob';
