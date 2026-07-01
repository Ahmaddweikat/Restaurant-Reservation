-- Retrieve Reservations Report with Views: Use a view to list all reservations information including restaurants and customers information.

create view Reservations_Report as 
select res.ReservationId, cust.CustomerId, cust.FirstName, cust.LastName, cust.Email, cust.PhoneNumber as [Customer Phone], rest.RestaurantId, rest.Name, rest.Address,
	   rest.PhoneNumber as [Restaurant Phone], rest.OpeningHours
from Reservations as res
join Restaurants as rest
on res.RestaurantId = rest.RestaurantId
join Customers as cust
on res.CustomerId = cust.CustomerId;