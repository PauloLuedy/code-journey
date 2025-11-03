# SQL Practice Environment

## Quick Start

1. **Start the database:**
   ```bash
   docker-compose up -d
   ```

2. **Connect to MySQL:**
   ```bash
   docker exec -it sql_practice mysql -u student -pstudent123 practice_db
   ```

3. **Stop the database:**
   ```bash
   docker-compose down
   ```

## Database Schema

- **departments**: id, department_name, budget
- **employees**: id, name, salary, department_id, manager_id, hire_date
- **projects**: id, project_name, employee_id, status, start_date

## Connection Details

- **Host**: localhost
  - **Port**: 3306
- **Database**: practice_db
- **Username**: student
- **Password**: student123

## Exercise Files

- `beginner_exercises.sql` - Basic SQL queries
- `intermediate_exercises.sql` - JOINs and aggregations
- `advanced_exercises.sql` - Window functions and CTEs
