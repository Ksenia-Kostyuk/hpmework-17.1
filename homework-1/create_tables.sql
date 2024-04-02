-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employe_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	post varchar(150),
	birth_date date
)

CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	name_company varchar(100),
	contact_employe varchar(100)
)

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(10) UNIQUE REFERENCES customers(customer_id),
	empploye_id int UNIQUE REFERENCES employees(employe_id),
	order_date date,
	city varchar(50)
)