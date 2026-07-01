-- Stored Procedure - Add New Order:
-- Procedure Name: `sp_AddNewOrder`
-- Purpose: Streamline the process of adding a new order.
-- Parameters: `ReservationId`, `EmployeeId`, `OrderDate`, and `TotalAmount`.
-- Implementation: Check if the specified reservation and employee exist, if not, return an error message, if existing, add new order.
-- Return: The new `BorrowerID` or an error message.

go

create procedure sp_AddNewOrder(@ReservationId int, @EmployeeId int, @OrderDate date, @TotalAmount Decimal(10,2))
as
begin
if not exists (select 1 from Reservations where ReservationId = @ReservationId)
or not exists (select 1 from Employees where EmployeeId = @EmployeeId)
print 'Error !'
else 
insert into Orders (ReservationId, EmployeeId, OrderDate, TotalAmount) values(@ReservationId, @EmployeeId, @OrderDate, @TotalAmount);
end;

go

exec dbo.sp_AddNewOrder 10, 2, '2026-01-02', 100.15