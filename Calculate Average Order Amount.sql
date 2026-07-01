-- Calculate Average Order Amount: Calculate the average order amount made through a specific employee.

select emp.EmployeeId, avg(ord.TotalAmount) as [Average Order Amount] from Orders as ord
join Employees as emp
on ord.EmployeeId = emp.EmployeeId
WHERE emp.EmployeeId = 50
group by emp.EmployeeId