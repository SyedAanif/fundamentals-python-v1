# LISTS --> ORDERED
numbers = [1, 4, 2, 3]  # ANY DATA TYPE HELD
numbersOfDifferentTypes = [1, 2, 3, 4, "A", [-1, 0]]  # ANY DATA TYPE HELD
print(numbers)
print(numbers[3])
print(numbersOfDifferentTypes[5][0])  # MATRIX ACCESS
"""print(numbers[7])  # INDEX OUT OF BOUNDS
print(numbers[3])  # NOT ACCESSIBLE AFTER EXCEPTION"""
print(len(numbers))
numbers.sort()  # SORT ASCENDING
print(numbers)
numbers.reverse()  # DESCENDING ORDER
print(numbers)
numbers.append(1000)  # ADD TO LAST
print(numbers)
print(4 in numbers)  # CHECK ELEMENT IS PRESENT OR NOT
numbers.remove(1)  # NUMBER TO BE REMOVED --> FIRST INSTANCE
# numbers.remove(11)  # ERROR --> NUMBER NOT IN LIST
print(numbers)
numbers.pop()  # REMOVES LAST MEMBER
print(numbers)
del numbers[0]  # INDEX BASED REMOVING [inclusiveIndex:exclusiveIndex]
del numbers[9:1000]  # ANY INDEX
print(numbers)
numbers.clear()  # DELETE ALL ELEMENTS
print(numbers)

# SETS --> DUPLICATES NOT ALLOWED --> UNORDERED
numbersSet = {1, 1}
print(numbersSet)  # ALMOST SAME METHODS AS LIST
lettersSet = {"a", "A", "B", "C", "A"}
print(lettersSet)
# INTERSECTION AND UNION
firstSet = {"A", "B", "D", "F"}
secondSet = {"C", "A", "E"}
print(firstSet | secondSet)  # UNION --> COMBINES BOTH REMOVING DUPLICATES
print(firstSet & secondSet)  # INTERSECTION --> COMMON BETWEEN THE TWO --> if none common empty set() returned
print(firstSet - secondSet)  # DIFFERENCE --> ELEMENTS IN FIRST BUT NOT IN SECOND

# DICTIONARIES --> KEY VALUE PAIRS
person = {
    "name": "Random Name",
    "age": 20,
    "address": 'USA'
}
print(person)
print(person["name"])  # ACCESSING THE VALUE USING THE KEY
print(person.get("age"))  # ACCESSING THE VALUE USING get(THE KEY)
"""print(person["randomAccess"])  # CAN'T ACCESS"""
print(person.keys())  # GET ALL KEYS
print(person.values())  # GET ALL VALUES
person["age"] = 100  # UPDATING VALUE
print(person)