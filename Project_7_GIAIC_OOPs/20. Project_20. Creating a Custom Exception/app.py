class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Age {age} is invalid. Age must be 18 or older."
        super().__init__(self.message)


def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    return f"Age {age} is valid. Access granted."


if __name__ == "__main__":
    # Test with valid age
    try:
        result = check_age(20)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test with invalid age
    try:
        result = check_age(15)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test with another invalid age
    try:
        result = check_age(16)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test with edge case
    try:
        result = check_age(18)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}") 