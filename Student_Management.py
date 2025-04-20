class StudentDatabase:

    __student_list = []
    @classmethod
    def add_student(cls,student):
        cls.__student_list.append(student)
    @classmethod
    def view_all_student_list(cls):
        return cls.__student_list
    @classmethod
    def find_student_id(cls,student_id):
        for student in cls.__student_list:
            if student.get_student_id() == student_id:
                return student
        return None

class Student:
    def __init__(self,student_id,name,dept):
        self.__student_id = student_id
        self.__name = name
        self.__dept = dept
        self.__is_enrolled = False
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print("Student is already enrolled!")
        else:
            self.__is_enrolled = True
            print("Student enrolled succesfully!")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Student is not currently enrolled!")
        else:
            self.__is_enrolled = False
            print("Student has been droped successfully.")

    def view_student_info(self):
        status = "Enrolled!" if self.__is_enrolled else "Not Enrolled!"
        print(f"\nStudent ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__dept}")
        print(f"Status: {status}\n")
    def get_student_id(self):
        return self.__student_id


Student(101, "Mirajul Islam", "CSE")
Student(102, "Monira Jahan", "EEE")
Student(103, "Nadia Khan", "BBA")

def menu():
    while True:
        print("\n--- Student Database Menu ---")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice(1-4): "))
            if choice == 1:
                students = StudentDatabase.view_all_student_list()
                for stu in students:
                    stu.view_student_info()
            elif choice == 2:
                stu_id = int(input("Enter student Enrolled id: "))
                student = StudentDatabase.find_student_id(stu_id)
                if student:
                    student.enroll_student()
                else:
                    print("Student Not Found!")
            elif choice == 3:
                stu_id = int(input("Enter student Enrolled id: "))
                student = StudentDatabase.find_student_id(stu_id)
                if student:
                    student.drop_student()
                else:
                    print("Student Not Found!")
            elif choice == 4:
                print("Exiting the program.Good Bye!")
                break
            else :
                print("Invalid oftion.Choose between 1-4")
        
        except ValueError:
            print("Please Enter a valid Number.")

menu()
