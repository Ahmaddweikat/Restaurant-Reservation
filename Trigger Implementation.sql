-- Trigger Implementation
-- Design a trigger to log an entry into a separate AuditLog table whenever a table get reserved. 
-- The AuditLog should capture ResturantId, TableId, ReservationDate and ChangeDate.

go

CREATE TABLE AuditLog (
    AuditLogId      INT IDENTITY(1,1) PRIMARY KEY,
    RestaurantId    INT             NOT NULL,
    TableId         INT             NOT NULL,
    ReservationDate DATETIME        NOT NULL,
    ChangeDate      DATETIME        NOT NULL DEFAULT GETDATE()
);
go

go

CREATE TRIGGER trg_ReservationAudit
ON Reservations
AFTER INSERT
AS
BEGIN
    INSERT INTO AuditLog (RestaurantId, TableId, ReservationDate, ChangeDate)
    SELECT RestaurantId, TableId, ReservationDate, GETDATE()
    FROM inserted;
END;

go 

INSERT INTO Reservations (CustomerId, RestaurantId, TableId, ReservationDate, PartySize)
VALUES (1, 1, 1, '2026-12-01 19:00', 4);

SELECT * FROM AuditLog;