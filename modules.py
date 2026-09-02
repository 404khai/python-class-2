# import math

# print(math.sqrt(25))

# USING AN ALIAS
# import math as m

# print(m.sqrt(36))

# from math import sqrt, factorial, cbrt

# print(sqrt(25))
# print(factorial(5))
# print(cbrt(125))
# 
import os
from pathlib import Path
import json

student = {
    "name": "Greatman",
    "age": 156,
    "course": "Python"
}

# state = input("eNTER State")


print(student["name"])
data = json.dumps(student)
print(data)
# path = Path.cwd()
# print(path)

# # CHECK IF A FILE EXISTS
# file = Path("students.txt")
# print(file.exists())

# print(os.getcwdb())
# print(os.listdir())

# os.mkdir("PythonDir")
# print("Directory created successfully")