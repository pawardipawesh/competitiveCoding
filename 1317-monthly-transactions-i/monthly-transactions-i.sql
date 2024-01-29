# Write your MySQL query statement below

with cte as (
select
    id,
    SUBSTR(trans_date, 1, 7) as mnth,
    country,
    case
        when state = 'approved' then 1
        else 0
    end as state,
    amount,
    case
        when state = 'approved' then amount
        else 0
    end as approved_amount
from
    Transactions
)

select
    mnth as month,
    country,
    sum(state) as approved_count,
    count(*) as trans_count,
    sum(amount) as trans_total_amount,
    sum(approved_amount) as approved_total_amount
from
    cte
group by
    mnth,
    country