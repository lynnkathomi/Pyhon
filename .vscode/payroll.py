#creating a parent class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        pass

#inheriting the employee class
class HourlyEmployee(Employee):
    HOURLY_RATE =1000

    def __init__(self, emp_id, name, salary, hours_worked):
        #the function inherited in the parent class
        super().__init__(emp_id, name, salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hours_worked * HourlyEmployee.HOURLY_RATE
#inheriting the employee class functions
class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, monthly_salary)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, monthly_salary, commission):
        super().__init__(emp_id, name, monthly_salary)
        self.commission = commission

    def calculate_salary(self):
        return self.monthly_salary + (self.monthly_salary * self.commission / 100)

# Set the constant salary for SalaryEmployee
SALARY_AMOUNT = 30,000

# Prompting the user to enter employee details
emp_name = input("Enter your official names: ")
emp_id = input("Enter employee ID: ")
salary_type = input("Enter type of employee (Hourly/Salary/Commission): ")
#calculating the hourly/salary/commision
if salary_type.lower() == "hourly":
    hours_worked = float(input("Enter hours worked: "))
    emp = HourlyEmployee(emp_id, emp_name, 0, hours_worked)
elif salary_type.lower() == "salary":
    emp = SalaryEmployee(emp_id, emp_name, SALARY_AMOUNT)
elif salary_type.lower() == "commission":
    commission = float(input("Enter commission percentage: "))
    emp = CommissionEmployee(emp_id, emp_name, SALARY_AMOUNT, commission)
#the final display when all data is aquired
print(f"The total salary for {emp.name} with ID {emp.emp_id} is: {emp.calculate_salary()}")