
class Student:    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My course is {self.course}")

    
students = []

# ADD STUDENT FUNCTION
def add_student():
    name = input("Enter student name: ")

    try:
        age = int(input("Enter student age: "))
        if age <= 1:
            print("Age must be greater than 1")
            return
    except ValueError:
        print("Age must be a number")
        return

    course = input("Enter student course: ")
    
    student = Student(name, age, course) 

    students.append(student)
    print("Student added successfully")

# VIEWING STUDENTS
def view_students():
    if len(students) == 0:
        print("No students found")
        return

    for index, student in enumerate(students, start=1):
        print(f"\n Student {index}")
        student.display()
        
# SEARCH STUDENTS
def search_student():
    name = input("Enter student name: ")

    for student in students:
        if student.name.lower() == name.lower():
            student.display()
            return
    print("Student not found")

# MENU
def show_menu():
    print("\n========================================")
    print("STUDENT MANAGEMENT SYSTEM")
    print("===========================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice")



