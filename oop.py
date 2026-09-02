class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        # print("My name is", {self.name})
        print(f"My name is {self.name}")
        print(f"I am studying {self.course}")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")

student = Student(name, age, course)

student.introduce()
# student1 = Student("Greatman", 35, "Python")
# student2 = Student("Kelly", 20, "Java")

# print(student1.age)
# print(student2.course)

# student1.introduce()
