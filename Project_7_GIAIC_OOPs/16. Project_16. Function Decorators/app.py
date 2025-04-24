def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("\nFunction is being called")
        return func(*args, **kwargs)
    return wrapper


@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    # Call the decorated function
    say_hello("Abdullah")
    
    # Call it again with a different name
    say_hello("Sarah")
    
    # The decorator will print the message each time the function is called 