-- ADVANCED SQL EXERCISES
-- Window functions, CTEs, complex queries, performance optimization

-- Exercise 1: Window function - ROW_NUMBER
-- Rank employees by salary within each department
-- Solution: SELECT name, department, salary, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank FROM employees;

-- Exercise 2: CTE (Common Table Expression)
-- Find the top 3 highest paid employees using CTE
-- Solution: WITH top_earners AS (SELECT name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn FROM employees) SELECT name, salary FROM top_earners WHERE rn <= 3;

-- Exercise 3: Recursive CTE
-- Create an organizational hierarchy showing employee and their managers
-- Solution: WITH RECURSIVE hierarchy AS (SELECT id, name, manager_id, 1 as level FROM employees WHERE manager_id IS NULL UNION ALL SELECT e.id, e.name, e.manager_id, h.level + 1 FROM employees e JOIN hierarchy h ON e.manager_id = h.id) SELECT * FROM hierarchy;

-- Exercise 4: PIVOT operation (using CASE)
-- Show employee count by department and year
-- Solution: SELECT YEAR(hire_date) as year, SUM(CASE WHEN department = 'IT' THEN 1 ELSE 0 END) as IT, SUM(CASE WHEN department = 'HR' THEN 1 ELSE 0 END) as HR, SUM(CASE WHEN department = 'Finance' THEN 1 ELSE 0 END) as Finance FROM employees GROUP BY YEAR(hire_date);

-- Exercise 5: LAG and LEAD functions
-- Calculate salary difference between current and previous employee (ordered by hire date)
-- Solution: SELECT name, salary, LAG(salary) OVER (ORDER BY hire_date) as prev_salary, salary - LAG(salary) OVER (ORDER BY hire_date) as salary_diff FROM employees;

-- Exercise 6: Complex aggregation with multiple CTEs
-- Find departments where average salary increased compared to previous year
-- Solution: WITH yearly_avg AS (SELECT department, YEAR(hire_date) as year, AVG(salary) as avg_salary FROM employees GROUP BY department, YEAR(hire_date)), salary_comparison AS (SELECT department, year, avg_salary, LAG(avg_salary) OVER (PARTITION BY department ORDER BY year) as prev_avg FROM yearly_avg) SELECT department, year FROM salary_comparison WHERE avg_salary > prev_avg;

-- Exercise 7: EXISTS vs IN performance
-- Find employees who work on active projects (compare EXISTS vs IN)
-- Solution with EXISTS: SELECT * FROM employees e WHERE EXISTS (SELECT 1 FROM projects p WHERE p.employee_id = e.id AND p.status = 'active');
-- Solution with IN: SELECT * FROM employees WHERE id IN (SELECT employee_id FROM projects WHERE status = 'active');

-- Exercise 8: Dense ranking with ties
-- Rank employees by salary, handling ties properly
-- Solution: SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank, RANK() OVER (ORDER BY salary DESC) as rank FROM employees;

-- Exercise 9: Running totals
-- Calculate running total of salaries ordered by hire date
-- Solution: SELECT name, hire_date, salary, SUM(salary) OVER (ORDER BY hire_date ROWS UNBOUNDED PRECEDING) as running_total FROM employees;

-- Exercise 10: Complex data analysis
-- Find employees whose salary is in the top 20% of their department and have been with company for more than 3 years
-- Solution: WITH dept_percentiles AS (SELECT id, name, department, salary, hire_date, PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary) as salary_percentile FROM employees) SELECT * FROM dept_percentiles WHERE salary_percentile >= 0.8 AND DATEDIFF(CURDATE(), hire_date) > 1095;
