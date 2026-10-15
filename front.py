import json

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


students = load_students()

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
#===================================================================
def add_student():

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Roll Number Already Exists!")
            return

    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")
    branch = input("Enter Branch: ")
    age = input("Enter Age: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "branch": branch,
        "age": age
    }

    students.append(student)

    save_students()

    print("Student Added Successfully!")

#==============================================================


def view_student():

    if len(students) == 0:
        print("No Students Found!")

    else:
        for student in students:

            print("\n-------------------------")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            print("Branch:", student["branch"])
            print("Age:", student["age"])
            print("-------------------------")

#================================================================


def search_student():

    roll_no = input("Enter Roll Number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nStudent Found!")

            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            print("Branch:", student["branch"])
            print("Age:", student["age"])

            return

    print("Student Not Found!")

#===================================================================


def delete_student():

    roll_no = input("Enter Roll Number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            students.remove(student)

            save_students()

            print("Student Deleted Successfully!")

            return

    print("Student Not Found!")


#=============================================================

def update_student():

    roll_no = input("Enter Roll Number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("Student Found!")

            student["name"] = input("Enter New Name: ")
            student["marks"] = input("Enter New Marks: ")
            student["branch"] = input("Enter New Branch: ")
            student["age"] = input("Enter New Age: ")

            save_students()

            print("Student Updated Successfully!")

            return

    print("Student Not Found!")


#=================================================================

def main():

    while True:

        print("\n=================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("=================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            update_student()

        elif choice == "6":
            print("Thank You For Using Student Management System!")
            break

        else:
            print("Invalid Choice! Please Try Again.")


main()