# file = open("students.txt", "r")

# content = file.read()

# print(content)

# file.close()
# 
# with open("students.txt", "r") as folder:
#     content = folder.read()
#     print(content)

# READ LINE BY LINE
# with open("students.txt", "r") as file:
#     for line in file:
#         # print(line)
#         # REMOVE WHITESPACE
#         print(line.strip())

#WRITE INTO A FILE
# with open("students.txt", "w") as file:
#     file.write("John \n")
#     file.write("Richard \n")
#     print("Filws have been written")

# APPEND TO FILE
# with open("students.txt", "a") as file:
#    file.write("Johnson \n")

# COLLECT INPUT AND APPEND TO FILE
name = input("Enter your name: ")
with open("students.txt", "a") as file:
    file.write(name + "\n")
    print("Student added successfully")