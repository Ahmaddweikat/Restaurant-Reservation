-- Restaurant Popularity using Aggregation: Rank restaurants by the reservation frequency.

select rest.RestaurantId, rest.Name, count(res.ReservationId) as Popularity,
rank() over(order by count(res.ReservationId) desc) as RestaurantPopularity
from Restaurants as rest
join Reservations as res
on rest.RestaurantId = res.RestaurantId
group by rest.RestaurantId, rest.Name