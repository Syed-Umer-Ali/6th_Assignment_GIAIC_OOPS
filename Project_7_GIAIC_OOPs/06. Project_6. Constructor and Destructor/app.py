class Logger:
    def __init__(self):
        print("Logger object created!")
    
    def __del__(self):
        print("Logger object destroyed!")


if __name__ == "__main__":
    print("Creating first logger...")
    logger1 = Logger()
    
    print("\nCreating second logger...")
    logger2 = Logger()
    
    print("\nProgram ending...")
    # Objects will be destroyed when the program ends 