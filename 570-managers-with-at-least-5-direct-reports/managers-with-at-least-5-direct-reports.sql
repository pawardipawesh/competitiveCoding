# Write your MySQL query statement below

with cte as 
(
    select
        managerId, 
        count(*) as nr
    from
        Employee
    group by 
        managerId
    having
        nr >= 5
)

select
    e.name as name
from
    cte c
inner join
    Employee e
on
    c.managerId = e.id
