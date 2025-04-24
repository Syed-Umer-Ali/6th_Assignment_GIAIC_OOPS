class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn         # Private variable
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


if __name__ == "__main__":
    # employee object
    emp = Employee("Umer", 50000, "123-45-6789")
    
    # Accessing public variable (works)
    print("Accessing public variable:")
    print(f"Name: {emp.name}")
    
    # Accessing protected variable (works but not recommended)
    print("\nAccessing protected variable:")
    print(f"Salary: {emp._salary}")
    
    # Accessing private variable (will cause error)
    print("\nTrying to access private variable directly:")
    try:
        print(f"SSN: {emp.__ssn}")  # This will raise an AttributeError
    except AttributeError as e:
        print(f"Error: You cannot access private variable directly")
    
    # The proper way to access all information
    print("\nAccessing information through class method:")
    emp.display_info() 