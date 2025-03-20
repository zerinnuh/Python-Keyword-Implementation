# Importing required modules
from datetime import datetime  # Importing datetime module to handle attendance timestamps

# Class Definition for Student
class Student:
    def __init__(self, name, student_id):  # Constructor to initialize student attributes
        self.name = name
        self.student_id = student_id
        self.attendance = []  # List to store attendance records

    def mark_attendance(self):
        """Marks attendance for the student with the current timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Gets current date and time
        self.attendance.append(timestamp)
        print(f"Attendance marked for {self.name} at {timestamp}")

    def display_attendance(self):
        """Displays the attendance record of the student"""
        print(f"Attendance record for {self.name}:")
        for record in self.attendance:
            print(record)

# Class Definition for Attendance System
class AttendanceSystem:
    def __init__(self):
        self.students = []  # List to store students

    def add_student(self, student):
        """Adds a student to the system"""
        self.students.append(student)
        print(f"Student {student.name} added successfully!")

    def mark_attendance(self, student_id):
        """Marks attendance for a student by student ID"""
        for student in self.students:
            if student.student_id == student_id:
                student.mark_attendance()
                return
        print("Student not found!")

    def display_all_attendance(self):
        """Displays attendance records of all students"""
        for student in self.students:
            student.display_attendance()

# Main function demonstrating Python keywords
def main():
    print("Student Attendance System")  # Prints system title

    # Creating Attendance System Object
    attendance_system = AttendanceSystem()

    # Adding students to the system
    student1 = Student("Rizzy", 101)
    student2 = Student("Annie", 102)
    attendance_system.add_student(student1)
    attendance_system.add_student(student2)

    # Marking attendance
    attendance_system.mark_attendance(101)
    attendance_system.mark_attendance(102)
    attendance_system.mark_attendance(103)  # Non-existent student

    # Display all attendance records
    attendance_system.display_all_attendance()

    # Exception Handling
    try:
        result = 10 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
    finally:
        print("Exception handling  has been completed.")

    # Using lambda function
    square = lambda x: x ** 2  # Lambda function to calculate square
    print("Square of 4:", square(4))

    # Using with statement for file handling
    with open("attendance_log.txt", "w") as file:  # Opens a file in write mode
        file.write("Attendance records logged.")

    # Global and Nonlocal example
    global_var = "Attendance Ongoing"

    def outer_function():
        outer_status = "Attendance has Closed"

        def inner_function():
            nonlocal outer_status
            outer_status = "Attendance is Ongoing"
            print("Inner Function Status:", outer_status)

        inner_function()
        print("Outer Function Status:", outer_status)

    outer_function()

    # None, True, False Keywords
    student_present = None  # Assigns None
    print("Student present?", student_present is None)
    print("Logical Examples:", True and False, True or False, not True)

    # Del Keyword
    temp_data = "Temporary Data"
    del temp_data  # Deletes temp_data variable

    # Yield Keyword
    def attendance_generator():
        yield "Rizzy Present"
        yield "Annie Present"
        yield "Alayie Absent"

    gen = attendance_generator()
    print("Generated Attendance Records:", next(gen), next(gen), next(gen))

    # Raise Keyword
    def raise_example():
        raise ValueError("Simulated error in Attendance System")

    try:
        raise_example()
    except ValueError as e:
        print("Caught Raised Exception:", e)

    print("End of Student Attendance System")

# Calling main function
if __name__ == "__main__":
    main()
