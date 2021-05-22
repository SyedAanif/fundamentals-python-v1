# DATA TYPES - DYNAMICALLY TYPED
brand = "Some Brand"
num = 2
numbers = [1, 2, 3, 4]
PI = 3.14
isAdult = True

print(type(brand))  # str
print(type(num))  # int
print(type(numbers))  # list
print(type(PI))  # float
print(type(isAdult))  # bool

# TO SPECIFY DATA TYPES
string: str = "Some String"
isUnderAge: bool = True
# NOTE:: HARD DATA TYPE CHECK IS STILL NOT THERE, JUST TO SEE THE TYPE IT IS MENTIONED
# isUnderAge: str = True  -- VALID --> RESOLVED TO bool AT RUNTIME -- Only Syntax Error


# IN METHODS WE CAN SPECIFY RETURN TYPES
def hello() -> str:
    return "hello"
