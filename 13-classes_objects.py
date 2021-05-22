# CREATING CLASSES
class Phone:
    # CONSTRUCTOR BY PASSING CURRENT INSTANCE --> self and OTHER ATTRIBUTES
    def __init__(self, brand, price):
        # ATTRIBUTES
        self.brand = brand
        self.price = price

    # BEHAVIOUR OF THE OBJECT FROM CLASS
    def call(self, phone_number):
        return f"{self.brand} is calling {phone_number}"

    # OVERRIDE TO STRING OF OBJECT
    def __str__(self) -> str:
        return f"Price = {self.price}, Brand = {self.brand}"


# CREATING OBJECTS FROM CLASS
iphone = Phone("Iphone 12", 300)
samsung = Phone("Samsung s21", 1400)

# ACCESSING METHODS/BEHAVIOURS
print(iphone)
print(iphone.call(12345))

print()

print(samsung)
print(samsung.call(12345))
