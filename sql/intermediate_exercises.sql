-- INTERMEDIATE SQL EXERCISES
-- JOINs, GROUP BY, HAVING, subqueries, and aggregate functions

-- Exercise 1: INNER JOIN
-- Join employees and departments tables to show employee names with their department names
Solution: SELECT e.name, d.department_name FROM employees e INNER JOIN departments d ON e.department_id = d.id;

-- Exercise 2: GROUP BY with COUNT
-- Count employees by department
 SELECT department, COUNT(*) as employee_count FROM employees GROUP BY department;

-- Exercise 3: GROUP BY with HAVING
-- Find departments with more than 1 employees
select 
d.department_name AS departamento,
COUNT(e.id) as total_funcionarios
from departments d 
left join employees e 
on e.department_id = d.id
group by d.department_name 
HAVING count(e.id) > 1


-- Exercise 4: LEFT JOIN
-- Show all departments and their employees (including departments with no employees)
SELECT d.department_name, e.name
FROM departments d 
LEFT JOIN employees e
on e.department_id  = d.id\
-- Exercise 5: Subquery in WHERE
-- Find employees earning more than the average salary
-- Solution: SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- Exercise 6: Multiple JOINs
-- Join employees, departments, and projects tables to show employee name, department, and project
-- Solution: SELECT e.name, d.department_name, p.project_name FROM employees e JOIN departments d ON e.department_id = d.id JOIN projects p ON e.project_id = p.id;

-- Exercise 7: CASE statement
-- Categorize employees as 'High', 'Medium', or 'Low' earners based on salary
-- Solution: SELECT name, salary, CASE WHEN salary > 70000 THEN 'High' WHEN salary > 50000 THEN 'Medium' ELSE 'Low' END as salary_category FROM employees;

-- Exercise 8: Date functions
-- Find employees hired in the last 2 years
-- Solution: SELECT * FROM employees WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR);

-- Exercise 9: Correlated subquery
-- Find employees earning more than the average in their department
-- Solution: SELECT * FROM employees e1 WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department = e1.department);

-- Exercise 10: UPDATE with JOIN
-- Increase salary by 10% for employees in the 'IT' department
-- Solution: UPDATE employees SET salary = salary * 1.1 WHERE department = 'IT';
