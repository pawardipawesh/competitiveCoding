# Write your MySQL query statement below
select distinct
    p.firstName,
    p.lastName,
    a.city,
    a.state
from
    Person p
left join
    Address a
on
   p.personId = a.personId