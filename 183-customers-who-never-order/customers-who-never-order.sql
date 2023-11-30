# Write your MySQL query statement below
with cte as
(select distinct 
   c.id,
   name as Customers
from 
    Customers c
left join
    Orders o
on
    c.id = o.customerId
where 
    o.id is Null)

select Customers from cte
