class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.course = ""
        self.roll_number = ""
        self.address = ""

    def set_details(self):
        self.name = input("Enter Student Name: ")1
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")
        self.course = input("Enter Course: ")
        self.roll_number = input("Enter Roll Number: ")
        self.address = input("Enter Address: ")

    def display_details(self):
        print("\nStudent Admission Form Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Course:", self.course)
        print("Roll Number:", self.roll_number)
        print("Address:", self.address)


class AdmissionSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student = Student()
        student.set_details()
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\nStudent Admission Form Details:")
        for i, student in enumerate(self.students, 1):
            print(f"\nStudent {i}:")
            student.display_details()

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student found:")
                student.display_details()
                return
        print("Student not found with the given Roll Number.")

    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found with the given Roll Number.")


if __name__ == "__main__":
    print("Welcome to Student Admission Form")
    admission_system = AdmissionSystem()

    while True:
        print("\n*** Admission Form Menu ***")
        print("1. Add Student Details")
        print("2. Display All Students")
        print("3. Search Student by Roll Number")
        print("4. Delete Student by Roll Number")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admission_system.add_student()

        elif choice == "2":
            admission_system.display_students()

        elif choice == "3":
            roll_number = input("Enter Roll Number to search: ")
            admission_system.search_student(roll_number)

        elif choice == "4":
            roll_number = input("Enter Roll Number to delete: ")
            admission_system.delete_student(roll_number)

        elif choice == "0":
            print("Exiting the Admission Form.")
            break

        else:
            print("Invalid choice. Please try again.")
