# Worksheet 3
# Q1
def diff_from_17(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return 17 - n

print(diff_from_17(22)) 

# Q2
def in_range(n):
    return (100 <= n <= 1000) or n == 2000

print(in_range(150))

# Q3
def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello"))

# Q4
def count_case(s):
    upper_case = sum(1 for c in s if c.isupper())
    lower_case = sum(1 for c in s if c.islower())
    return upper_case, lower_case

print(count_case("Hello World!"))

# Q5
def distinct_elements(lst):
    return list(set(lst))

print(distinct_elements([1, 2, 2, 3, 4, 4]))

# Q6
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])) 

# Q7
def outer_func():
    def inner_func():
        print("Inner function")
    return inner_func()

outer_func() 

# Q8
def student(*args):
    return args

print(student('John', 'Maths', 'A+'))

# Q9
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None
    
    def set_class(self, student_class):
        self.student_class = student_class
    
    def display(self):
        print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")

student = Student(1, "John")
student.set_class("10th")
student.display() 

# Q10
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(1, "John")
student2 = Student(2, "Jane")

print(f"Student 1 - ID: {student1.student_id}, Name: {student1.student_name}")
print(f"Student 2 - ID: {student2.student_id}, Name: {student2.student_name}")

# Q11
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")

# Q12
class StringManipulator:
    def __init__(self):
        self.string = ""
    
    def get_String(self):
        self.string = input("Enter a string: ")
    
    def print_String(self):
        print(self.string.upper())

string_manipulator = StringManipulator()
string_manipulator.get_String()
string_manipulator.print_String()