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
    suni = 0
    how = 0
    for average in students:
        if average.get("class") == class_name:
            suni += float(average.get("grade"))
            how += 1
            
    if how == 0:
        return 0
    return suni / how

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

def ptint_all(students, filename):
    all_name = []
    for name in students:
        all_name.append(name.get("name"))
    print(all_name)
    
    while True:
        nenu = int(input("to see all enter 1: \nto add enter 2:\nto find enter 3:\nto class average enter 4:\nto top student enter 5: \nto save and exit enter 6 \nto delete a student enter 7: "))
        if nenu > 7 or nenu < 1:
            print("the number is error try agein😒")
        if nenu == 1:
            for s in students:
                print(s)
                
        elif nenu == 2:
            name = input("Enter the name: ")
            while True:
                grade = int(input("Enter the grade: "))
                if grade <= 100 and grade >= 0:
                    break
                print("the grade is error try agein")
            class_name = input("Enter the class: ")
            add_student(students, name, grade, class_name)
            save_students(filename, students)
            print("Student added and saved successfully!😊")
            
        elif nenu == 3:
            name_to_find = input("enter the name: ")
            print(find_student(students, name_to_find))
            
        elif nenu == 4:
            class_to_find = input("enter name op the class: ")
            print(class_average(students, class_to_find))
            
        elif nenu == 5:
            print(top_student(students))

        elif nenu == 7:
            name_of_delete = input("Enter the name of the student to delete: ")
            students = delete_student(students, name_of_delete)
            save_students(filename, students)
            print("Student deleted and saved successfully!🗑️")

        elif nenu == 6:
                    save_students(filename, students)
                    return "Saved and exiting👌"

def delete_student(students,name):
    new=[i for i in students if i.get("name") != name]
    return new
            

file_name = "students.csv"
a = load_students(file_name)
b = ptint_all(a, file_name)
print(b)