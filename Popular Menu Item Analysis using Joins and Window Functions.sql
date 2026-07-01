-- Popular Menu Item Analysis using Joins and Window Functions: Identify the most popular menu item for each restaurant for a given month.

select rest.Name as [Restaurant Name], menu.Name as [Item Name], count(menu.ItemId) as Popularity,
rank() over(PARTITION BY rest.Name order by count(menu.ItemId) desc) as Rank
from Restaurants as rest
join Reservations as res
on rest.RestaurantId = res.RestaurantId
join Orders as ord
on ord.ReservationId = res.ReservationId
join OrderItems as item
on ord.OrderId = item.OrderId
join MenuItems as menu
on item.ItemId = menu.ItemId
where ord.OrderDate between '2026-01-01' and '2026-01-31'
group by rest.Name, menu.Name