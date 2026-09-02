# Inheritance allows one class (child / sub class) to reuse and extend another class (parent class).
# Child classes can inherit the functions of the parent class e.g both child classes can access display_info from Employee
# PARENT CLASS
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    def work(self):
        print(f"{self.name} is working")

    def get_bonus(self):
        return self.salary * 0.05

    def totalSalary(self):
        total = self.salary + self.get_bonus()
        print(f"Total Salary is: {total}")

# CHILD / SUB CLASS
class SoftwareEngineer(Employee):
    def __init__(self, name, salary, department, programmingLanguage):
        # super() means Go to the parent class and use its constructor. so this line calls Employee.__init__(...) from Employee parent class
        super().__init__(name, salary, department)

        self.programmingLanguage = programmingLanguage

    def write_code(self):
        print(f"{self.name} is writing {self.programmingLanguage}")

    # METHOD OVERRIDING
    # Overriding is the process of a child class making it's version of a method/function from the parent class e.g
    # def work from Employee should print Rutherford is working. But now it will print Rutherford is developing software
    
    # This is the main mechanism behind inheritance-based polymorphism.
    # The parent class defines: def work(self):  
    # Then the child defines another method with the same name: def work(self): 
    # The child's version replaces the parent's version for objects of that child class.
    # Example:
    # class Employee:
    #     def work(self):
    #         print("Employee is working")
    # class SoftwareEngineer(Employee):
    
    #     def work(self):
    #         print("Software engineer is coding")
    
    # Then:
    # employee = Employee()
    # engineer = SoftwareEngineer()

    # employee.work()
    # engineer.work()
    
    # Output:
    
    # Employee is working
    # Software engineer is coding
    # 

    def work(self):
        print(f"{self.name} is developing software")

    def get_bonus(self):
        return self.salary * 0.15

# CHILD / SUB CLASS
class ProductManager(Employee):
    def __init__(self, name, salary, department, product):
        super().__init__(name, salary, department)

        self.product = product

    def plan_product(self):
        print(f"{self.name} is planning {self.product}")

    # METHOD OVERRIDING
    def work(self):
        print(f"{self.name} is planning product features")

    def get_bonus(self):
        return self.salary * 0.10

# POLYMORPHSIM WITH A FUNCTION
def start_work(employee):
    employee.work()
    
engineer = SoftwareEngineer("Greatman", 500000, "Engineering", "Python")
pm = ProductManager("Rutherford", 600000, "Product", "Mobile App")

engineer.totalSalary()
# employees = [
#     engineer,
#     pm
# ]

# for employee in employees:
#     employee.work()
#     print(f"Bonus: {employee.get_bonus()}")
    
# engineer.display_info()
# engineer.write_code()
# engineer.work()

# pm.display_info()
# pm.plan_product()
# pm.work()

# Polymorphism With a Function. You can also pass different objects into the same function.
# start_work(engineer)