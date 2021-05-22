# WORKING WITH DATES
import datetime  # IMPORT THE MODULE

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().time())

# FORMATTING DATES
now = datetime.datetime.now()
print(f"Un formatted Date = {now}")

print(f"Formatted Date = {now.strftime('%d-%m-%Y %H:%M:%S')}")
print(f"Formatted Date = {now.strftime('%d-%B-%Y %H:%M:%S')}")
print(f"Formatted Date = {now.strftime('%d-%b-%Y %H:%M:%S')}")
