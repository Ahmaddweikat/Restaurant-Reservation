	-- Database Function - Calculate Employees Salary:
	-- Function Name: `fn_CalculateEmployeeSalary`
	-- Purpose: Compute the salary for a given employee.
	-- Parameter: `EmployeeId`
	-- Implementation: Salary is defined as: # number of orders made by specific employee * employee rank.
	-- Employee’s rank based on position: Position = `Manager` = 5, `Waiter` = 4, `Waitress`  = 3.
	-- Return: salary for the `EmployeeId`.

	go

	create function fn_CalculateEmployeeSalary(@EmployeeId int)
	returns int
	as
	begin

	declare @Salary int
	declare @Position nvarchar(50)

	set @Position = (select Position from Employees 
	where EmployeeId = @EmployeeId)

	if(@Position = 'Manager') begin
	set @Salary = (select count(ord.OrderId) * 5
	from Orders as ord
	where ord.EmployeeId = @EmployeeId)
	return @Salary;
	end

	else if(@Position = 'Waiter') begin
	set @Salary = (select count(ord.OrderId) * 4
	from Orders as ord
	where ord.EmployeeId = @EmployeeId)
	return @Salary;
	end

	else if(@Position = 'Waitress') begin
	set @Salary = (select count(ord.OrderId) * 3
	from Orders as ord
	where ord.EmployeeId = @EmployeeId)
	return @Salary;
	end

	return 0
	end;

	go

	select dbo.fn_CalculateEmployeeSalary(14) as Salary;