mysql> use stocks;
Database changed
mysql> show tables;
+------------------+
| Tables_in_stocks |
+------------------+
| location         |
| product          |
| productmovement  |
+------------------+
3 rows in set (0.01 sec)

mysql> select * from location;
+-------------+
| location_id |
+-------------+
| chennai     |
| trichy      |
| salem       |
| madurai     |
+-------------+
4 rows in set (0.00 sec)

mysql> select * from product;
+------------+
| product_id |
+------------+
| IMWA 1     |
| IMWA 2     |
| IMWA 3     |
| IMWA 4     |
+------------+
4 rows in set (0.00 sec)

mysql> select * from productmovement;
+-------------+---------------------+---------------+-------------+------------+------+
| movement_id | timestamp           | from_location | to_location | product_id | qty  |
+-------------+---------------------+---------------+-------------+------------+------+
|         101 | 2023-01-30 15:01:27 | chennai       | -------     | IMWA1      |  100 |
|         102 | 2023-01-30 15:02:52 | chennai       | trichy      | IMWA1      |  100 |
|         103 | 2023-01-30 15:03:30 | trichy        | salem       | IMWA1      |   50 |
|         104 | 2023-01-30 15:04:25 | chennai       | -------     | IMWA2      |   40 |
+-------------+---------------------+---------------+-------------+------------+------+
4 rows in set (0.00 sec)
