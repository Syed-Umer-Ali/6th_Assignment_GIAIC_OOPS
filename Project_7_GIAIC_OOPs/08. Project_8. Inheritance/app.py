class Person:
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f"Name inherited from parent class: {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the parent class constructor
        self.subject = subject
    
    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"Subject: {self.subject}")


if __name__ == "__main__":
    # Create a Person object
    person = Person("Ali")
    print("Person Information:")
    person.display_info()
    
    # Create a Teacher object
    teacher = Teacher("Umer", "Mathematics")
    print("\nTeacher Information:")
    teacher.display_info() 