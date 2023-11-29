# Write your MySQL query statement below

with cte as
(select 
    *
from
    (select 
        *,
        DENSE_RANK() over (PARTITION BY departmentId order by salary desc) as rn
    from
        Employee
    ) as dt 
)

select 
    d.name as Department,
    c.name as Employee,
    c.salary as Salary
from 
    cte c
left join
    Department d
on
    c.departmentId = d.id
where c.rn < 4