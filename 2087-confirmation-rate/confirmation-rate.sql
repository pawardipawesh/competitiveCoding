# Write your MySQL query statement below

with cte as
(
select
    user_id,
    sum(case
            when action = 'confirmed' then 1.0
            when action = 'timeout' then 0.0
            else 0
        end
    ) as int_action,
    count(*) as total
from
    Confirmations
group by
    user_id
)

select
    s.user_id as user_id,
    case
        when c.total is Null then 0
        when c.total = 0 then 0
        else round(c.int_action/c.total, 2)
    end as confirmation_rate
from 
    Signups s
left join
    cte c
on
    s.user_id = c.user_id




    