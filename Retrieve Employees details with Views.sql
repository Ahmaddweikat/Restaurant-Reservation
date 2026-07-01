-- Retrieve Employees details with Views: Use a view to list all employees information including their restaurants details

create view Employee_Details as
select emp.EmployeeId, emp.FirstName, emp.LastName, emp.Position, rest.RestaurantId, rest.Name, rest.Address,
	   rest.PhoneNumber as [Restaurant Phone], rest.OpeningHours
from Employees as emp
join Restaurants as rest
on emp.RestaurantId = rest.RestaurantId;