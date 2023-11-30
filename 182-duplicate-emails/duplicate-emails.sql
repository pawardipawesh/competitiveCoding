# Write your MySQL query statement below
with cte as 
(select 
    email, 
    count(*) as cnt
from Person
group by email
having cnt > 1)

select 
    email 
from cte