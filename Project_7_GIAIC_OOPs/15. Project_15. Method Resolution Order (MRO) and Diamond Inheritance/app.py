class A:
    def show(self):
        print("This is class A")


class B(A):
    def show(self):
        print("This is class B")


class C(A):
    def show(self):
        print("This is class C")


class D(B, C):
    print("this is class D")


if __name__ == "__main__":
    # Create an object of D
    d = D()
    
    # Call show() to see which version is executed
    print("Calling show() on D object:")
    d.show()
    
    # Display the Method Resolution Order
    print("\nMethod Resolution Order (MRO) for class D:")
    print(D.mro())
    
    # Demonstrate inheritance chain
    print("\nInheritance chain:")
    print(f"D inherits from: {D.__bases__}")
    print(f"B inherits from: {B.__bases__}")
    print(f"C inherits from: {C.__bases__}") 