# STRINGS
brand = "some dummy brand"
print(brand.upper())
print(len(brand))
print(brand.replace("s", "11"))
print(brand == "some dummy brand")  # == CHECKS EQUALITY OF CONTENT.
print(brand != "some dummy brand")
print("some" in brand)

# FORMATTING STRINGS
paragraphWrongFormat = "I want " \
                       "my sentence to be " \
                       "formatted like this, with each " \
                       "sentence in new line."
print(paragraphWrongFormat)
paragraphRightFormat = """
The correct way to
write a sentence in your format
is writing it like
a multiline comment.
"""
print(paragraphRightFormat)

# PLACEHOLDERS
emailExampleForPlaceHolder1 = """
Hi {},
This is testing place holders using curly braces
and string.format method.
"""
name = "Dummy Name"
print(emailExampleForPlaceHolder1.format(name))

emailExampleForPlaceHolder2 = f"""
Hi {name},
This is testing place holders using curly braces
, 'f' at the beginning and variable inside.
With also expression evaluation 4 + 4 = {4 + 4}
"""
print(emailExampleForPlaceHolder2)
