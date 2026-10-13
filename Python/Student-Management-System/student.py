                                                    #Student Management System

students = []

def add_student():
    st_id = int(input("enter student id: "))
    st_name = input("enter the name: ")
    maths_marks = int(input("enter the maths marks: "))
    python_marks = int(input("enter the python marks: "))
    java_marks = int(input("enter the java marks: "))

    student = {
        "id" : st_id,
        "name" : st_name,
        "maths" : maths_marks,
        "python" : python_marks,
        "java" : java_marks,
    }
    students.append(student)
    print("student added successfully.")

def view_student():
    if len(students) == 0:
        print("no record found")
        return
    print("\n****** Students list ******")
    for student in students:
        print(
            "ID:",student["id"],
            "| NAME:",student["name"],
            "| MATHS:",student["maths"],
            "| PYTHON:",student["python"],
            "| JAVA:",student["java"]
        )

def search_student():
    search_id = int(input("enter the student id to search his data: "))
    for student in students:
        if student["id"] == search_id:
            print("\n*****student found******")
            print("ID:",student["id"])
            print("name:",student["name"])
            print("maths marks:",student["maths"])
            print("python marks:",student["python"])
            print("java marks:",student["java"])
            return
    print("student not found")

def calculate_average():
    search_id = int(input("Enter Student ID to get the average of all subjects: "))

    for student in students:
        if student["id"] == search_id:
            total = student["maths"] + student["python"] + student["java"]
            average = total / 3
            print("student found")
            print("\n===== STUDENT RESULT =====")
            print("Name:", student["name"])
            print("Total Marks:", total)
            print("Average Marks:", round(average,2))
            return

    print("Student not found.")

# add_student()
# view_student()
# search_student()
# calculate_average()
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
