# LOOPING
# FOR LOOP --> LISTS and SETS
namesList = ["Abc", "Def", "Ghi", "Jkl"]
for name in namesList:
    print(name)
# FOR LOOP --> DICTIONARY
person = {
    "name": "Random Name",
    "age": 20,
    "address": 'USA'
}
for key in person:
    print(f"Key::{key}  Value::{person[key]}")
print(person.items())  # ARRAY OF KEY VALUE PAIRS
for key, value in person.items():
    print(f"Key::{key}  Value::{value}")

exerciseList = [1, 3, 5, 6, 7, 9]
sumOfNumbers = 0
for num in exerciseList:
    sumOfNumbers += num
print(f"Sum of numbers = {sumOfNumbers}")

# WHILE LOOP
number = 0
while number < 10:
    print(number)
    number += 1
else:
    print("While Loop Ended")

# BREAK
num = 0
while num < 10:
    if num == 5:
        print("Breaking out of loop")
        break
    num += 1
    print(num)

# CONTINUE
num = 0
while num < 10:
    num += 1
    if num < 5:
        print("Continue to loop start")
        continue
    print(num)
