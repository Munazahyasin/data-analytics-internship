# Student Management System

students = []


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print("ID:", student["ID"])
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Course:", student["Course"])
        print("Marks:", student["Marks"])
        print("-----------------------")


def search_student():
    search = input("Enter student ID or name to search: ")

    found = False

    for student in students:
        if student["ID"] == search or student["Name"].lower() == search.lower():
            print("\nStudent Found:")
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])
            found = True

    if not found:
        print("Student not found.")


def update_student():
    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["ID"] == student_id:
            student["Name"] = input("Enter new name: ")
            student["Age"] = int(input("Enter new age: "))
            student["Course"] = input("Enter new course: ")
            student["Marks"] = float(input("Enter new marks: "))

            print("Student details updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")