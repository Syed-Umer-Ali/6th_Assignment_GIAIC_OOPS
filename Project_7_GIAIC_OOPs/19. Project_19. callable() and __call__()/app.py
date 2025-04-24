class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, number):
        return number * self.factor


if __name__ == "__main__":
    # Create a multiplier object
    multiply_by_5 = Multiplier(5)
    
    # Check if the object is callable
    print(f"Is multiply_by_5 callable? {callable(multiply_by_5)}")
    
    # Call the object like a function
    result = multiply_by_5(10)
    print(f"10 multiplied by 5: {result}")
    
    # Create another multiplier
    multiply_by_3 = Multiplier(3)
    print(f"\nIs multiply_by_3 callable? {callable(multiply_by_3)}")
    print(f"7 multiplied by 3: {multiply_by_3(7)}")
    
    # Try with different numbers
    print("\nTry with different numbers")
    print(f"15 multiplied by 5: {multiply_by_5(15)}")
    print(f"20 multiplied by 3: {multiply_by_3(20)}") 