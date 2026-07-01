-- Database Function - Calculate Restaurant Revenue:
-- FunctionName:`fn_CalculateRevenue`
-- Purpose:Compute revenue made by a specific restaurant.
-- Parameter:`RestaurantId`
-- Return:total revenue amount for the `RestaurantId`.

go

create function fn_CalculateRevenue(@RestaurantId int)
returns decimal(10,2)
as
begin
declare @Total Decimal(10,2)
select @Total = cast(sum(ord.TotalAmount) as decimal(10,2))
from Restaurants as rest
join Reservations as res
on rest.RestaurantId = res.RestaurantId
join Orders as ord
on res.ReservationId = ord.ReservationId
where rest.RestaurantId = @RestaurantId
return @Total
end;

go

select dbo.fn_CalculateRevenue(7) AS [Total Revenue];