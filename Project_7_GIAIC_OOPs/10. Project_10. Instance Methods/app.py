class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"Dog {self.name} is a {self.breed} and says: Woof! Woof!")


if __name__ == "__main__":
    # Create a dog object
    my_dog = Dog("Buddy", "Husky")
    
    # Call the instance method
    my_dog.bark()
    
    # Create another dog
    neighbor_dog = Dog("Max", "German Shepherd")
    neighbor_dog.bark() 