# Write your MySQL query statement below

select
    TS.request_at as Day,
    round(sum(TS.status_int)/count(TS.id), 2) as `Cancellation Rate`           
from
    (select 
        *,
        CASE
            WHEN status = 'cancelled_by_driver' THEN 1
            WHEN status = 'cancelled_by_client' THEN 1
            ELSE 0
        END as status_int
    from Trips
    where 
        request_at 
        between 
            str_to_date("2013-10-01", '%Y-%m-%d') and 
            str_to_date("2013-10-03", '%Y-%m-%d')) TS
    INNER JOIN
        (select
            *
        from Users
        where
        banned = 'No' and
        (role = 'client' or role = 'driver')
        ) US_client
    on
        US_client.users_id = TS.client_id
    INNER JOIN
        (select
            *
        from Users
        where
        banned = 'No' and
        (role = 'client' or role = 'driver')
        ) US_driver
    on
        US_driver.users_id = TS.driver_id
group by
    TS.request_at
