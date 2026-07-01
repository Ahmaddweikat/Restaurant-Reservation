-- List of Ordered Menu Items: Lists the menu items ordered by a specific reservation.

select res.ReservationId, menu.Name, menu.Description,ordItem.Quantity, menu.Price from Reservations as res
join Orders as ord
on res.ReservationId = ord.ReservationId
join OrderItems as ordItem
on ord.OrderId = ordItem.OrderId
join MenuItems as menu
on ordItem.ItemId = menu.ItemId
where res.ReservationId = 411;