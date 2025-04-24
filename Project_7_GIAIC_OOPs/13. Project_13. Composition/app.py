class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        print(f"{self.engine_type} engine started!")
    
    def stop(self):
        print(f"{self.engine_type} engine stopped!")


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  
    
    def start_car(self):
        print(f"\nStarting {self.brand} car...")
        self.engine.start()  # Accessing Engine's method of Engine class
    
    def stop_car(self):
        print(f"Stopping {self.brand} car...")
        self.engine.stop()  # Accessing Engine's method of Engine class


if __name__ == "__main__":
    # Create an engine
    v8_engine = Engine("V8")
    my_car = Car("Bugatti", v8_engine)
    
    # Use the car's methods which access the engine's methods
    my_car.start_car()
    my_car.stop_car()
    
    # Create another car with a different engine
    electric_engine = Engine("Electric")
    electric_car = Car("Tesla", electric_engine)
    
    electric_car.start_car()
    electric_car.stop_car() 