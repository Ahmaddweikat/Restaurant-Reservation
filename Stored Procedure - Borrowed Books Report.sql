-- Stored Procedure - Borrowed Books Report:
-- Procedure Name: `sp_ResrvedTablesReport`
-- Purpose: Generate a report of tables reserved within a specified date range.
-- Parameters: `StartDate`, `EndDate`
-- Implementation: Retrieve all tables reserved within the given range, with details like reservation date, party size and restaurant details.
-- Return: Tabulated report of reserved tables.

go

create procedure sp_ResrvedTablesReport(@StartDate date, @EndDate date)
as
begin
select rest.RestaurantId, rest.Name, rest.Address, rest.PhoneNumber, rest.OpeningHours, tbl.TableId, tbl.Capacity, res.ReservationDate, res.PartySize
from Restaurants as rest
join Tables as tbl
on rest.RestaurantId = tbl.RestaurantId
join Reservations as res
on res.TableId = tbl.TableId
where res.ReservationDate between @StartDate and @EndDate
order by res.ReservationDate
end;

go

exec dbo.sp_ResrvedTablesReport '2026-01-01', '2026-01-31'