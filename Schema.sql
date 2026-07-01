-- =========================================================
-- Restaurant Management System - MS SQL Server Schema
-- =========================================================

CREATE DATABASE RestaurantDB;
GO

USE RestaurantDB;
GO

-- =========================================================
-- 1. Restaurants
-- =========================================================
CREATE TABLE Restaurants (
    RestaurantId    INT IDENTITY(1,1) PRIMARY KEY,
    Name            NVARCHAR(100)   NOT NULL,
    Address         NVARCHAR(255)   NOT NULL,
    PhoneNumber     NVARCHAR(20)    NULL,
    OpeningHours    NVARCHAR(100)   NULL
);
GO

-- =========================================================
-- 2. Tables (within a restaurant)
-- =========================================================
CREATE TABLE Tables (
    TableId         INT IDENTITY(1,1) PRIMARY KEY,
    RestaurantId    INT             NOT NULL,
    Capacity        INT             NOT NULL,
    CONSTRAINT FK_Tables_Restaurants
        FOREIGN KEY (RestaurantId) REFERENCES Restaurants(RestaurantId)
        ON DELETE CASCADE
);
GO

-- =========================================================
-- 3. MenuItems
-- =========================================================
CREATE TABLE MenuItems (
    ItemId          INT IDENTITY(1,1) PRIMARY KEY,
    RestaurantId    INT             NOT NULL,
    Name            NVARCHAR(100)   NOT NULL,
    Description     NVARCHAR(255)   NULL,
    Price           DECIMAL(10,2)   NOT NULL,
    CONSTRAINT FK_MenuItems_Restaurants
        FOREIGN KEY (RestaurantId) REFERENCES Restaurants(RestaurantId)
        ON DELETE CASCADE
);
GO

-- =========================================================
-- 4. Employees
-- =========================================================
CREATE TABLE Employees (
    EmployeeId      INT IDENTITY(1,1) PRIMARY KEY,
    RestaurantId    INT             NOT NULL,
    FirstName       NVARCHAR(50)    NOT NULL,
    LastName        NVARCHAR(50)    NOT NULL,
    Position        NVARCHAR(50)    NULL,
    CONSTRAINT FK_Employees_Restaurants
        FOREIGN KEY (RestaurantId) REFERENCES Restaurants(RestaurantId)
        ON DELETE CASCADE
);
GO

-- =========================================================
-- 5. Customers
-- =========================================================
CREATE TABLE Customers (
    CustomerId      INT IDENTITY(1,1) PRIMARY KEY,
    FirstName       NVARCHAR(50)    NOT NULL,
    LastName        NVARCHAR(50)    NOT NULL,
    Email           NVARCHAR(100)   NULL,
    PhoneNumber     NVARCHAR(20)    NULL
);
GO

-- =========================================================
-- 6. Reservations
-- =========================================================
CREATE TABLE Reservations (
    ReservationId   INT IDENTITY(1,1) PRIMARY KEY,
    CustomerId      INT             NOT NULL,
    RestaurantId    INT             NOT NULL,
    TableId         INT             NOT NULL,
    ReservationDate DATETIME        NOT NULL,
    PartySize       INT             NOT NULL,
    CONSTRAINT FK_Reservations_Customers
        FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
    CONSTRAINT FK_Reservations_Restaurants
        FOREIGN KEY (RestaurantId) REFERENCES Restaurants(RestaurantId),
    CONSTRAINT FK_Reservations_Tables
        FOREIGN KEY (TableId) REFERENCES Tables(TableId)
);
GO

-- =========================================================
-- 7. Orders
-- ReservationId is optional (NULL allowed) - an order can
-- exist without a reservation (e.g. walk-ins/takeout)
-- =========================================================
CREATE TABLE Orders (
    OrderId         INT IDENTITY(1,1) PRIMARY KEY,
    ReservationId   INT             NULL,
    EmployeeId      INT             NOT NULL,
    OrderDate       DATETIME        NOT NULL DEFAULT GETDATE(),
    TotalAmount     DECIMAL(10,2)   NOT NULL DEFAULT 0,
    CONSTRAINT FK_Orders_Reservations
        FOREIGN KEY (ReservationId) REFERENCES Reservations(ReservationId)
        ON DELETE SET NULL,
    CONSTRAINT FK_Orders_Employees
        FOREIGN KEY (EmployeeId) REFERENCES Employees(EmployeeId)
);
GO

-- =========================================================
-- 8. OrderItems
-- Every OrderItem must belong to an Order (mandatory)
-- =========================================================
CREATE TABLE OrderItems (
    OrderItemId     INT IDENTITY(1,1) PRIMARY KEY,
    OrderId         INT             NOT NULL,
    ItemId          INT             NOT NULL,
    Quantity        INT             NOT NULL DEFAULT 1,
    CONSTRAINT FK_OrderItems_Orders
        FOREIGN KEY (OrderId) REFERENCES Orders(OrderId)
        ON DELETE CASCADE,
    CONSTRAINT FK_OrderItems_MenuItems
        FOREIGN KEY (ItemId) REFERENCES MenuItems(ItemId)
);
GO