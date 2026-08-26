import csv
import os

def load_students(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8", newline="") as f:
        a = csv.DictReader(f)
        return list(a)

def save_students(filename, students):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["name", "grade", "class"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def add_student(students, name, grade, class_name):
    students.append({"name": name, "grade": grade, "class": class_name})

def find_student(students, name):
    for name1 in students:
        if name1.get("name") == name:
            return name1
    return None

def class_average(students, class_name):
    total = 0
    count = 0
    for average in students:
        if average.get("class") == class_name:
            total += float(average.get("grade"))
            count += 1

    if count == 0:
        return 0
    return total / count

def top_student(students):
    if not students:
        return None
    topist = ""
    nom_top = -1
    for top in students:
        grade = int(top.get("grade", 0))
        if grade > nom_top:
            nom_top = grade
            topist = top.get("name")
    return topist

def print_all(students):
    for student in students:
        print(student["name"], "|", student["grade"], "|", student["class"])

def delete_student(students, name):
    new = [i for i in students if i.get("name") != name]
    return new

def report_to_txt(students):
    if not students:
        return
    count = len(students)
    avg = sum(int(s["grade"]) for s in students) / count
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(f"\n the top studen is {top_student(students)}")
        f.write(f"\n the average form the student is {avg}")
        f.write(f"\n how match student {count}")
    return "the text file was created successfully"

def run_menu(students, filename):
    all_name = []
    for name in students:
        all_name.append(name.get("name"))
    print(all_name)

    while True:
        choice = int(input("to see all enter 1: \nto add enter 2:\nto find enter 3:\nto class average enter 4:\nto top student enter 5: \nto save and exit enter 6 \nto delete a student enter 7 \nto save file txt enter 8: "))
        if choice > 8 or choice < 1:
            print("the number is error try agein😒")
        if choice == 1:
            print_all(students)

        elif choice == 2:
            name = input("Enter the name: ")
            while True:
                try:
                    grade = int(input("Enter the grade: "))
                    if grade <= 100 and grade >= 0:
                        break
                    print("the grade is error try agein")
                except ValueError:
                    print("the grade is error try agein")
            class_name = input("Enter the class: ")
            add_student(students, name, str(grade), class_name)
            save_students(filename, students)
            print("Student added and saved successfully!😊")

        elif choice == 3:
            name_to_find = input("enter the name: ")
            print(find_student(students, name_to_find))

        elif choice == 4:
            class_to_find = input("enter name op the class: ")
            print(class_average(students, class_to_find))

        elif choice == 5:
            print(top_student(students))

        elif choice == 7:
            name_of_delete = input("Enter the name of the student to delete: ")
            students = delete_student(students, name_of_delete)
            save_students(filename, students)
            print("Student deleted and saved successfully!🗑️")

        elif choice == 8:
            report_to_txt(students)
            print("the text file was created successfully")
        elif choice == 6:
            save_students(filename, students)
            return "Saved and exiting👌"

file_name = "students.csv"
a = load_students(file_name)
b = run_menu(a, file_name)
print(b)