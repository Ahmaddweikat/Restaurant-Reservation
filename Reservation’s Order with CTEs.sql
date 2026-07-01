-- Reservation’s Order with CTEs: Identify reservations which have 2 or more orders using CTEs.


with Reservation_Order as (
select res.ReservationId, count(ord.OrderId) as OrderCount
from Reservations as res
join Orders as ord
on res.ReservationId = ord.ReservationId
group by res.ReservationId
)

select * from Reservation_Order
where OrderCount >= 2