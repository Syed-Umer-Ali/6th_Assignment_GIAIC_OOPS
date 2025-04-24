class Bank:
    bank_name = "GIAIC Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def display_info(self):
        print(f"Bank Name: {Bank.bank_name}")


if __name__ == "__main__":
    bank1 = Bank()
    
    print("Initial Bank Information:")
    bank1.display_info()
    
    print("\nAfter changing bank name:")
    Bank.change_bank_name("GIAIC International Bank")
    
    bank1.display_info()
   