class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name} got {self.marks} marks.")
       


if __name__ == "__main__":
    student1 = Student("Ahmed", 98)
    
student1.display()
