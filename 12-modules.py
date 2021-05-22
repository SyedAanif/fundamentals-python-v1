# FIRST CREATE YOUR OWN MODULE --> e.g; calculator.py
# FIRST WAY OF IMPORTING OUR OWN MODULE
import calculator

print(calculator.add(2, 2))
print(calculator.sub(2, 2))
print(calculator.divide(2, 2))
print(calculator.multiply(2, 2))

# SECOND WAY OF IMPORTING WITH JUST BRINGING SPECIFIC METHODS
from calculator import add

print(add(2, 4))
