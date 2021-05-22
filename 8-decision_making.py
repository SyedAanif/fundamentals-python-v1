# DECISION MAKING
# IF - ELIF -ELSE
randomNum = 15
if randomNum > 0:
    print(f"Number {randomNum} is positive")
elif randomNum < 0:
    print(f"Number {randomNum} is negative")
elif randomNum == 0:
    print("Number {} is neither positive nor negative".format(randomNum))
else:
    print("Learn number system...")

# TERNARY IF
message = "positive" if randomNum > 0 else "0 or negative"
print(message)
