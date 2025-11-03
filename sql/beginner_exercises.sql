-- BEGINNER SQL EXERCISES
-- Basic SELECT, WHERE, ORDER BY, and simple functions
select * from departments d 

select * from departments d 
where budget > 200000.00

select * from departments d 
where budget > 200000.00
order by budget asc

-- Exercise 1: Basic SELECT
-- Write a query to select all columns from a table called 'employees'
 SELECT * FROM employees;

-- Exercise 2: SELECT specific columns
-- Select only 'name' and 'salary' from the 'employees' table
SELECT name, salary FROM employees;

-- Exercise 3: WHERE clause
-- Find all employees with salary greater than 50000
 SELECT * FROM employees WHERE salary > 50000;

-- Exercise 4: ORDER BY
-- List all employees ordered by salary in descending order
SELECT * FROM employees ORDER BY salary DESC;

-- Exercise 5: LIKE operator
-- Find employees whose name starts with 'J'
SELECT * FROM employees WHERE name LIKE 'J%';

-- Exercise 6: COUNT function
-- Count the total number of employees
SELECT COUNT(*) FROM employees;

-- Exercise 7: MAX function
-- Find the highest salary
SELECT MAX(salary) FROM employees;

-- Exercise 8: WHERE with multiple conditions
-- Find employees with salary between 40000 and 60000
SELECT * FROM employees WHERE salary >= 40000 AND salary <= 60000;

-- Exercise 9: DISTINCT
-- Get unique department names from employees table
 SELECT DISTINCT department FROM employees;

-- Exercise 10: Basic INSERT
-- Insert a new employee: John Doe, salary 55000, department IT
 INSERT INTO employees (name, salary, department) VALUES ('John Doe', 55000, 'IT');
