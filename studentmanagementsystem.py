class Student:
    def __init__(self, roll_number, name, age, grade):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_student(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print("-------------")

class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_student(self, roll_number, name, age, grade):
        student = Student(roll_number, name, age, grade)
        self.students.append(student)
    
    def display_all_students(self):
        for student in self.students:
            student.display_student()
    
    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

# Sample usage:
if __name__ == "__main__":
    sms = StudentManagementSystem()
    
    # Adding students
    sms.add_student(101, "Iyyappan", 18, "A")
    sms.add_student(102, "Shiva", 17, "B")
    sms.add_student(103, "Ramya", 18, "A+")
    
    # Displaying all students
    sms.display_all_students()
    
    # Searching for a student
    roll_number_to_search = 102
    found_student = sms.search_student(roll_number_to_search)
    if found_student:
        print(f"Student with Roll Number {roll_number_to_search} found:")
        found_student.display_student()
    else:
        print(f"Student with Roll Number {roll_number_to_search} not found.")
