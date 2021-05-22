# FUNCTIONS -- NOTE:: NO FORWARD CARRYING AVAILABLE i.e; CAN'T USE BEFORE DECLARATION
# FUNCTION DEFINITION WITHOUT ARGUMENTS
def greet_someone():
    print("Hello,How are you?")


# CALL TO FUNCTION
greet_someone()


# FUNCTION WITH ARGUMENTS
def greet_someone_with_parameters(name, age):
    print(f"Hello {name}, how are you?")
    print(f"Your age is {age}")


# CALL FUNCTION
greet_someone_with_parameters("Foo", 15)


# FUNCTION WITH DEFAULT VALUES
def greet_with_default_parameters(name="Default name", age=-1):
    print(f"Hello {name}")
    if age >= 0:
        print(f"Your age is {age}")


# CALL FUNCTION
greet_with_default_parameters()


# FUNCTION WITH RETURN VALUES
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


# CALL FUNCTION
if is_adult(16):
    print("You are an adult :(")
else:
    print("Not yet an adult :)")
