-- Initialize database with sample data for SQL practice

USE practice_db;

-- Create departments table
CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(50) NOT NULL,
    budget DECIMAL(12,2)
);

-- Create employees table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    department_id INT,
    manager_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

-- Create projects table
CREATE TABLE projects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(100) NOT NULL,
    employee_id INT,
    status VARCHAR(20) DEFAULT 'active',
    start_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Insert sample departments
INSERT INTO departments (department_name, budget) VALUES
('IT', 500000.00),
('HR', 200000.00),
('Finance', 300000.00),
('Marketing', 250000.00),
('Sales', 400000.00);

-- Insert sample employees
INSERT INTO employees (name, salary, department_id, manager_id, hire_date) VALUES
('John Smith', 75000.00, 1, NULL, '2020-01-15'),
('Jane Doe', 65000.00, 1, 1, '2021-03-10'),
('Mike Johnson', 55000.00, 1, 1, '2022-06-20'),
('Sarah Wilson', 70000.00, 2, NULL, '2019-08-05'),
('Tom Brown', 45000.00, 2, 4, '2023-01-12'),
('Lisa Davis', 80000.00, 3, NULL, '2018-11-30'),
('Chris Miller', 60000.00, 3, 6, '2021-09-15'),
('Amy Taylor', 52000.00, 4, NULL, '2022-02-28'),
('David Lee', 48000.00, 4, 8, '2023-05-10'),
('Emma Garcia', 85000.00, 5, NULL, '2017-12-01'),
('Ryan Martinez', 58000.00, 5, 10, '2020-07-22'),
('Kelly Anderson', 62000.00, 1, 1, '2021-11-08');

-- Insert sample projects
INSERT INTO projects (project_name, employee_id, status, start_date) VALUES
('Website Redesign', 2, 'active', '2024-01-15'),
('Mobile App', 3, 'active', '2024-02-01'),
('HR System', 5, 'completed', '2023-06-01'),
('Financial Dashboard', 7, 'active', '2024-03-10'),
('Marketing Campaign', 9, 'active', '2024-01-20'),
('Sales Portal', 11, 'active', '2023-12-15'),
('Database Migration', 12, 'completed', '2023-09-01');
