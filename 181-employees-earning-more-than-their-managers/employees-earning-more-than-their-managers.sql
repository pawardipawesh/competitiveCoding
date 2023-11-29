# Write your MySQL query statement below
select 
    E.name as Employee
from
    Employee E
INNER JOIN
    Employee L
On
    E.managerId = L.id
where 
    E.salary > L.salary