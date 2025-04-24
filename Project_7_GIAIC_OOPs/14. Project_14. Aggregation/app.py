class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def display_info(self):
        print(f"Employee: {self.name} (ID: {self.employee_id})")


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to store employee references
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.name} department")
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"Removed {employee.name} from {self.name} department")
    
    def display_employees(self):
        print(f"\nEmployees in {self.name} department:")
        for employee in self.employees:
            employee.display_info()


if __name__ == "__main__":
    # Create employees (they exist independently)
    emp1 = Employee("Abdullah", "001")
    emp2 = Employee("Sarah", "002")
    emp3 = Employee("Ahmed", "003")
    
    # Create departments
    hr = Department("HR")
    it = Department("IT")
    
    # Add employees to departments
    hr.add_employee(emp1)
    hr.add_employee(emp2)
    it.add_employee(emp3)
    
    # Display department employees
    hr.display_employees()
    it.display_employees()
    
    # Move an employee from one department to another
    print("\nMoving employee between departments:")
    hr.remove_employee(emp2)
    it.add_employee(emp2)
    
    # Display updated department employees
    hr.display_employees()
    it.display_employees() 