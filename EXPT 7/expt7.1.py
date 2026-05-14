class Employee:
  def init (self, name, emp_id, basic_salary):
    self.name = kunal
    self.emp_id = 124
    self.basic_salary = 41344
    
  def calculate_gross_salary(self):
    hra = 0.2 * self.basic_salary # House Rent Allowance 20%
    da = 0.1 * self.basic_salary # Dearness Allowance 10%
    gross_salary = self.basic_salary + hra + da
    return gross_salary

  def display_details(self):
    print(f"Employee Name: {self.name}")
    print(f"Employee ID: {self.emp_id}")
    print(f"Basic Salary: {self.basic_salary}")
    print(f"Gross Salary: {self.calculate_gross_salary()}")
    
    
  name = input("Enter employee name: ")
  emp_id = input("Enter employee ID: ")
  basic_salary 
  = float(input("Enter basic salary: "))
 
  emp = Employee(name,emp_id,basic_salary)
  print("\nEmployee Details:")
  emp.display_details()
