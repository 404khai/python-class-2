# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("Enter a valid number")

# try:
#     number = int(input("Enter a number: "))
#     # name = input("Enter a name")
#     print(number)
# except ValueError:
#     print("Enter a valid name")

# age = int("hello3")
# 
# try:
#     number1 = int(input("Enter first number: "))
#     number2 = input("Enter second number: ")

#     result = number1 / number2

#     print(result)

# except ValueError:
#     print("Please enter numbers only")
# except ZeroDivisionError:
#     print("you can't divide by zero")


# age = 20
# name = "Great"

# print(age + name)

# myAge = input("Enter age: ")
# 
try: #block of code likely to throw error
    num = int(input("Enter a number: "))
except ValueError: #handle error
    print("Invalid number")
else: #if try succeeds, do else
    print("You entered: ", num)
finally: #run whether exception occurs or not
    print("Program finished")