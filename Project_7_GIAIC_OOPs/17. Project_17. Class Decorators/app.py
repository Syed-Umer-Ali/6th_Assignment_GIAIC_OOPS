def add_greeting(cls):
    # Add a new method to the class
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the method to the class
    cls.greet = greet
    return cls


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f"Name: {self.name}")


if __name__ == "__main__":
    # Create a Person object
    person = Person("ALi")
    
    # Use the original method
    person.display_info()
    
    # Use the decorated method
    print(person.greet())
    
    # Create another person
    person2 = Person("Sarah")
    person2.display_info()
    print(person2.greet()) 