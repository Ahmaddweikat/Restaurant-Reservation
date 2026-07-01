-- List of Orders and Menu Items: Lists the orders placed on a specific given reservation along with the associated menu items.

select res.ReservationId, ord.OrderId, ordItem.ItemId, menu.Name, menu.Description from Orders as ord
join Reservations as res
on ord.ReservationId = res.ReservationId
join OrderItems as ordItem
on ord.OrderId = ordItem.OrderId
join MenuItems as menu
on ordItem.ItemId = menu.ItemId
where res.ReservationId = 222;