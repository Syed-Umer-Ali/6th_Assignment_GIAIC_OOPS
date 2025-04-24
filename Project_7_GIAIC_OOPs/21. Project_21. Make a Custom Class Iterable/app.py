class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            current_value = self.current
            self.current -= 1
            return current_value


if __name__ == "__main__":
    # Create a countdown from 5
    print("Countdown from 5:")
    for number in Countdown(5):
        print(number)
    
    # Create a countdown from 3
    print("\nCountdown from 3:")
    for number in Countdown(3):
        print(number)
    
    # Create a countdown from 10
    print("\nCountdown from 10:")
    for number in Countdown(10):
        print(number)
    
    # Test with zero
    print("\nCountdown from 0:")
    for number in Countdown(0):
        print(number)
    
    # Test with negative number
    print("\nCountdown from -1:")
    for number in Countdown(-1):
        print(number) 