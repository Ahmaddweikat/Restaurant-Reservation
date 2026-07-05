<img width="4491" height="2469" alt="ERD" src="https://github.com/user-attachments/assets/a34655d7-3c99-44ab-8e2f-d88a80347633" /># Restaurant Reservation Management System

A relational database built in MS SQL Server to support restaurant operations including reservations, orders, menu management, and employee tracking.

---

## Background

A group of restaurants wishes to transition from their traditional ordering and reservation system to a more robust digital platform. This database supports their core operations: managing tables, reservations, customers, employees, menu items, and orders.

---

## Objective

Design and implement a relational database using MS SQL that supports the restaurant's operations and offers extensive querying capabilities.

---

## ERD Diagram

Designed using ERDPlus.

<img width="4491" height="2469" alt="ERD" src="https://github.com/user-attachments/assets/d24e40d8-9db9-4a78-b0d7-b565a8c4c631" />

### Relationships Summary

| Relationship | Cardinality | Notes |
|---|---|---|
| Restaurants – Table | 1..1 to 1..N | A restaurant has one or many tables |
| Restaurants – MenuItems | 1..1 to 0..N | A restaurant has zero or many menu items |
| Restaurants – Employee | 1..1 to 1..N | A restaurant has one or many employees |
| Restaurants – Reservation | 1..1 to 0..N | A restaurant has zero or many reservations |
| Customer – Reservation | 1..1 to 0..N | A customer makes zero or many reservations |
| Reservation – Order | 0..1 to 0..1 | An order may optionally link to a reservation (walk-ins allowed) |
| Employee – Order | 1..1 to 1..N | An employee handles one or many orders |
| Order – OrderItems | 1..1 to 1..N | An order contains one or many order items (mandatory) |
| MenuItems – OrderItems | 1..1 to 0..N | A menu item appears in zero or many order items |

---

## Repository Structure

| File | Description |
|---|---|
| `schema.sql` | DDL — creates the database and all 8 tables with PK/FK constraints |
| `seed_data.sql` | DML — fictional, internally consistent seed data |
| `generate_seed.py` | Python script used to generate the seed data |
| `01_list_of_reservations.sql` | Query 1 — reservations for a specific customer |
| `02_list_of_managers.sql` | Query 2 — employees holding Manager position |
| `03_orders_and_menu_items.sql` | Query 3 — orders and menu items for a reservation |
| `04_ordered_menu_items.sql` | Query 4 — menu items ordered by a reservation |
| `05_average_order_amount.sql` | Query 5 — average order amount per employee |
| `06_view_reservations_report.sql` | Query 6 — view: reservations with restaurant and customer info |
| `07_view_employees_details.sql` | Query 7 — view: employees with restaurant details |
| `08_cte_reservation_orders.sql` | Query 8 — CTE: reservations with 2 or more orders |
| `09_restaurant_popularity.sql` | Query 9 — restaurants ranked by reservation frequency |
| `10_popular_menu_items.sql` | Query 10 — most popular menu item per restaurant per month |
| `11_fn_CalculateRevenue.sql` | Function — compute total revenue for a restaurant |
| `12_fn_CalculateEmployeeSalary.sql` | Function — compute salary for an employee |
| `13_sp_ReservedTablesReport.sql` | Procedure — reserved tables report by date range |
| `14_sp_AddNewOrder.sql` | Procedure — add a new order with validation |
| `15_sp_FutureReservations.sql` | Procedure — future reserved tables using temp table |
| `16_trigger_AuditLog.sql` | Trigger — log reservation inserts to AuditLog |
| `17_query_plans_part1.md` | Screenshots and notes on query plans before indexing |
| `18_indexes.sql` | Indexes created to improve query performance |
| `19_query_plans_part2.md` | Screenshots and notes on query plans after indexing |

---

## Setup

```bash
# Run in order against your SQL Server instance
sqlcmd -S your_server -i schema.sql
sqlcmd -S your_server -i seed_data.sql
```

Or open each file in SSMS, make sure RestaurantDB is selected in the database dropdown, then execute.

---

## Schema

### Restaurants
Stores core restaurant information.
| Column | Type | Key |
|---|---|---|
| RestaurantId | INT | PK |
| Name | NVARCHAR(100) | |
| Address | NVARCHAR(255) | |
| PhoneNumber | NVARCHAR(20) | |
| OpeningHours | NVARCHAR(100) | |

### Tables
Physical tables within a restaurant.
| Column | Type | Key |
|---|---|---|
| TableId | INT | PK |
| RestaurantId | INT | FK → Restaurants |
| Capacity | INT | |

### MenuItems
Food and drink items offered by a restaurant.
| Column | Type | Key |
|---|---|---|
| ItemId | INT | PK |
| RestaurantId | INT | FK → Restaurants |
| Name | NVARCHAR(100) | |
| Description | NVARCHAR(255) | |
| Price | DECIMAL(10,2) | |

### Employees
Staff members belonging to a restaurant.
| Column | Type | Key |
|---|---|---|
| EmployeeId | INT | PK |
| RestaurantId | INT | FK → Restaurants |
| FirstName | NVARCHAR(50) | |
| LastName | NVARCHAR(50) | |
| Position | NVARCHAR(50) | |

### Customers
Registered customers who make reservations.
| Column | Type | Key |
|---|---|---|
| CustomerId | INT | PK |
| FirstName | NVARCHAR(50) | |
| LastName | NVARCHAR(50) | |
| Email | NVARCHAR(100) | |
| PhoneNumber | NVARCHAR(20) | |

### Reservations
Table bookings made by customers at restaurants.
| Column | Type | Key |
|---|---|---|
| ReservationId | INT | PK |
| CustomerId | INT | FK → Customers |
| RestaurantId | INT | FK → Restaurants |
| TableId | INT | FK → Tables |
| ReservationDate | DATETIME | |
| PartySize | INT | |

### Orders
Orders placed during a visit, optionally linked to a reservation.
| Column | Type | Key |
|---|---|---|
| OrderId | INT | PK |
| ReservationId | INT | FK → Reservations (nullable — walk-ins allowed) |
| EmployeeId | INT | FK → Employees |
| OrderDate | DATETIME | |
| TotalAmount | DECIMAL(10,2) | |

### OrderItems
Individual line items within an order.
| Column | Type | Key |
|---|---|---|
| OrderItemId | INT | PK |
| OrderId | INT | FK → Orders (mandatory) |
| ItemId | INT | FK → MenuItems |
| Quantity | INT | |

---

## Seed Data

| Table | Rows |
|---|---|
| Restaurants | 50 |
| Tables | 100 |
| MenuItems | 1000 |
| Employees | 100 |
| Customers | 400 |
| Reservations | 500 |
| Orders | 500 |
| OrderItems | 1500 |

Generated using `generate_seed.py` (Python standard library, fixed seed for reproducibility). Data is internally consistent:
- Every restaurant has at least one table and one employee
- Menu items are categorized (Starters, Mains, Desserts, Beverages) with realistic price ranges per category
- Reservation party sizes never exceed the assigned table's capacity
- ~70% of orders are linked to a reservation; ~30% are walk-in orders (ReservationId = NULL)
- Every order is handled by an employee from that same restaurant
- Every OrderItem references a menu item from that order's restaurant only
- TotalAmount on each order is computed from the sum of Quantity × Price across its OrderItems

---

## Queries & Procedures — Rationale

### 1. List of Reservations
Retrieves all reservations for a specific customer using a WHERE filter on CustomerId. Useful for customer-facing reservation history.

```sql
SELECT * FROM Reservations WHERE CustomerId = @CustomerId;
```

### 2. List of Managers
Filters the Employees table by `Position = 'Manager'`. Useful for management reporting and contact lookups.

```sql
SELECT * FROM Employees WHERE Position = 'Manager';
```

### 3. Orders and Menu Items for a Reservation
Joins Orders → OrderItems → MenuItems filtered by a given ReservationId. Shows the full order context for a reservation. Useful for front-of-house staff reviewing what was ordered.

### 4. Ordered Menu Items for a Reservation
Similar to Query 3 but focused purely on menu items (name, description, quantity, price) without order-level metadata. Useful for kitchen or billing summaries.

### 5. Average Order Amount per Employee
Uses AVG(TotalAmount) grouped by EmployeeId with a WHERE filter on the specific employee. Useful for performance tracking.

```sql
SELECT emp.EmployeeId, AVG(ord.TotalAmount) AS [Average Order Amount]
FROM Orders AS ord
JOIN Employees AS emp ON ord.EmployeeId = emp.EmployeeId
WHERE emp.EmployeeId = @EmployeeId
GROUP BY emp.EmployeeId;
```

### 6. View — Reservations Report
A view (`Reservations_Report`) joining Reservations, Customers, and Restaurants into a reusable result set. Both PhoneNumber columns aliased as `[Customer Phone]` and `[Restaurant Phone]` to avoid column name conflicts.

### 7. View — Employees Details
A view joining Employees with Restaurants to show each employee alongside their restaurant's details. Useful for HR and scheduling reports.

### 8. CTE — Reservations with 2+ Orders
Uses a CTE to count orders per reservation, then filters where count >= 2. CTEs make the two-step logic (aggregate then filter) readable and maintainable.

```sql
WITH Reservation_Order AS (
    SELECT res.ReservationId, COUNT(ord.OrderId) AS OrderCount
    FROM Reservations AS res
    JOIN Orders AS ord ON res.ReservationId = ord.ReservationId
    GROUP BY res.ReservationId
)
SELECT ReservationId, OrderCount
FROM Reservation_Order
WHERE OrderCount >= 2;
```

### 9. Restaurant Popularity Ranking
Uses COUNT(ReservationId) with RANK() OVER(ORDER BY COUNT DESC) to rank restaurants by reservation frequency. Useful for business performance comparisons.

```sql
SELECT rest.RestaurantId, rest.Name, COUNT(res.ReservationId) AS Popularity,
RANK() OVER(ORDER BY COUNT(res.ReservationId) DESC) AS RestaurantPopularity
FROM Restaurants AS rest
JOIN Reservations AS res ON rest.RestaurantId = res.RestaurantId
GROUP BY rest.RestaurantId, rest.Name;
```

### 10. Popular Menu Item per Restaurant per Month
Uses COUNT(ItemId) with RANK() OVER(PARTITION BY restaurant ORDER BY count DESC) filtered by a date range. PARTITION BY ensures ranking resets per restaurant so each gets its own #1 item independently.

### 11. fn_CalculateRevenue
Scalar function that takes a RestaurantId and returns total revenue by summing TotalAmount across all orders linked to that restaurant's reservations. Returns 0 if no orders exist.

```sql
SELECT dbo.fn_CalculateRevenue(1) AS [Total Revenue];
```

### 12. fn_CalculateEmployeeSalary
Scalar function computing an employee's salary as: number of orders handled × position rank.
- Manager = 5
- Waiter = 4
- Waitress = 3
- All other positions = 0

```sql
SELECT dbo.fn_CalculateEmployeeSalary(1) AS Salary;
```

### 13. sp_ReservedTablesReport
Stored procedure accepting a date range and returning all tables reserved within it, joined with restaurant details. Useful for capacity planning.

```sql
EXEC sp_ResrvedTablesReport '2025-01-01', '2025-12-31';
```

### 14. sp_AddNewOrder
Stored procedure that validates both ReservationId and EmployeeId exist in their respective tables before inserting a new order. Returns an error message if either is missing, preventing orphaned records.

```sql
EXEC sp_AddNewOrder 1, 5, '2026-01-15', 85.50;
```

### 15. sp_FutureReservation (Temp Table)
Stored procedure that queries future reservations, stores matching tables in a temp table (`#FutureTables`), then joins with Restaurants to return restaurant-level details. Demonstrates temp table usage for multi-step processing.

### 16. Trigger — AuditLog
An AFTER INSERT trigger on the Reservations table that logs every new reservation into AuditLog, capturing RestaurantId, TableId, ReservationDate, and ChangeDate (GETDATE()). Uses the special `inserted` table available inside triggers to handle both single and bulk inserts correctly.

### 17. Query Plans Part 1
The following 5 queries were selected for query plan analysis before indexing:
- Query 9: Restaurant Popularity (RANK + GROUP BY)
- Query 10: Popular Menu Item Analysis (PARTITION BY + JOIN chain)
- Query 8: CTE Reservation Orders
- Query 11: fn_CalculateRevenue
- Query 13: sp_ReservedTablesReport

Screenshots are in the `/query-plans` folder. Common findings before indexing: Table Scans on Reservations, Orders, and OrderItems due to missing indexes on FK columns.

### 18. Indexes
Indexes created on the most frequently filtered and joined columns:

```sql
CREATE INDEX IX_Reservations_CustomerId ON Reservations(CustomerId);
CREATE INDEX IX_Reservations_RestaurantId ON Reservations(RestaurantId);
CREATE INDEX IX_Reservations_TableId ON Reservations(TableId);
CREATE INDEX IX_Reservations_ReservationDate ON Reservations(ReservationDate);
CREATE INDEX IX_Orders_ReservationId ON Orders(ReservationId);
CREATE INDEX IX_Orders_EmployeeId ON Orders(EmployeeId);
CREATE INDEX IX_OrderItems_OrderId ON OrderItems(OrderId);
CREATE INDEX IX_OrderItems_ItemId ON OrderItems(ItemId);
CREATE INDEX IX_MenuItems_RestaurantId ON MenuItems(RestaurantId);
```

### 19. Query Plans Part 2
After adding indexes, the same 5 queries were re-examined. Table Scans were replaced by Index Seeks, significantly reducing query cost. Screenshots are in the `/query-plans` folder with `_after` suffix for comparison.
