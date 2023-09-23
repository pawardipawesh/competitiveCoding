# Write your MySQL query statement below

select
    dept.name as Department,
    emp_der.Employee as Employee,
    emp_der.salary as Salary
from
    (select 
        emp.name as Employee,
        emp.salary,
        emp.departmentId
    from 
        Employee emp
    INNER JOIN
        (select
            departmentId,
            max(salary) as salary
        from Employee
        group by
            departmentId) dept_max_salary
    On
        emp.departmentId = dept_max_salary.departmentId AND
        emp.salary = dept_max_salary.salary) emp_der
    inner join
        Department dept
    on
        dept.id = emp_der.departmentId



