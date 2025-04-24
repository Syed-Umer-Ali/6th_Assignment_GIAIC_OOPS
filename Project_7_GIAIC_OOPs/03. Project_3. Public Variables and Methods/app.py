class Car:
    brand = "Toyota Corolla"
    
    def start(self):
        print(f"The {self.brand} has started!")


if __name__ == "__main__":
    my_car = Car()
    
print(f"Car brand: {my_car.brand}")
my_car.start()
    

my_car.brand = "Honda Civic"
print(f"New car brand: {my_car.brand}")
my_car.start() 