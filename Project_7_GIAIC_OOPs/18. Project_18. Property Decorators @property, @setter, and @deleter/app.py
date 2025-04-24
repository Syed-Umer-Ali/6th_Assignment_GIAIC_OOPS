class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute
    
    @property
    def price(self):
        print("Getting price...")
        return self._price
    
    @price.setter
    def price(self, value):
        print(f"Setting {self.name}'s price... to ${value}")
        try:
            # Try to convert value to float
            price_value = float(value)
            
            # Check if the value is negative
            if price_value < 0:
                raise ValueError("Price cannot be negative")
            
            # Check if the value is a string that can't be converted to number
            if isinstance(value, str) and not value.replace('.', '', 1).isdigit():
                raise ValueError("Price must be a number")
            
            self._price = price_value
        except ValueError as e:
            if "Price cannot be negative" in str(e):
                raise ValueError("Price cannot be negative")
            else:
                raise ValueError("Price must be a number, not a string or alphabet")
    
    @price.deleter
    def price(self):
        print("Deleting price...")
        self._price = 0


if __name__ == "__main__":
    # Create a product
    product = Product("Laptop", 1000)
    
    # Get price using property
    print(f"{product.name}'s Initial price: ${product.price}")
    
    # Set price using setter
    product.price = 1200
    print(f"{product.name}'s Updated price: ${product.price}")
    
    # Try setting negative price
    try:
        product.price = -100
    except ValueError as e:
        print(f"Error: {e}")
    
    # Try setting string price
    try:
        product.price = "abc"
    except ValueError as e:
        print(f"Error: {e}")
    
    # Try setting numeric string price
    try:
        product.price = "500"
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{product.name}'s Price after setting string number: ${product.price}")
    
    # Delete price using deleter
    del product.price
    print(f"{product.name}'s Price after deletion: ${product.price}")
    
    # Create another product
    product2 = Product("Phone", 500)
    print(f"\n{product2.name}'s Price: ${product2.price}") 