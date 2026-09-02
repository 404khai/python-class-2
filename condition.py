# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

day = "Monday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
else:
    print("Weekday, go to school")


age = int(input("Enter your age: "))
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Access denied")
else:
    print("You're underage")