-- SQL Stored Procedure with Temp Table:
-- Design a stored procedure that retrieves all tables which have future reservations. 
-- Store these tables in a temporary table, 
-- then join this temp table with the Restaurants table to list out the specific information about the associated restaurants.

GO

CREATE PROCEDURE sp_FutureReservation
AS
BEGIN
    SELECT DISTINCT tbl.TableId, tbl.RestaurantId, tbl.Capacity
    INTO #FutureTables
    FROM Tables AS tbl
    JOIN Reservations AS res ON tbl.TableId = res.TableId
    WHERE res.ReservationDate > GETDATE();

    SELECT ft.TableId, ft.Capacity, rest.RestaurantId, rest.Name,
           rest.Address, rest.PhoneNumber, rest.OpeningHours
    FROM #FutureTables AS ft
    JOIN Restaurants AS rest ON ft.RestaurantId = rest.RestaurantId;

    DROP TABLE #FutureTables;
END;

GO

exec sp_futureReservation;