class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    # Convert temperatures using static methods
    celsius_temp = 25
    fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C in Fahrenheit is equal to {fahrenheit_temp:.2f}°F")
    
    # Convert back to Celsius
    converted_back = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp:.2f}°F in Celsius is equal to {converted_back:.2f}°C")
    
    # You can also call static methods from an instance (though not necessary)
    converter = TemperatureConverter()
    temp = converter.celsius_to_fahrenheit(0)
    print(f"0°C in Fahrenheit is equal to {temp:.2f}°F") 