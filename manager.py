import csv
import os 

def load_students(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8", newline="") as f:
        a = csv.DictReader(f)
        return list(a)

def add_student(filename, name, grade, class_name):
    with open(filename, "a", encoding="utf-8", newline="") as f:
        c = csv.writer(f)
        c.writerow([name, grade, class_name])

def find_student(students, name):
    for name1 in students:
        if name1.get("name") == name:
            return name1
    else:
        return None  

def class_average(students, class_name):
    suni=0
    how=0
    for average in students:
        if average.get("class") == class_name:
            suni+=float(average.get("grade"))
            how+=1
    
            if how == 0:
                return how
    return  suni / how


def top_student(students):
    topist=""
    nom_top=0
    for top in students:
        if int(top.get("grade")) > nom_top:
            nom_top=int(top.get("grade"))
            topist=str(top.get("name"))
            if len(students) == 0 :
                return None
    return topist

n = load_students("students.csv")
# a = find_student(n, "Noa")
# a=class_average(n,"10A")
a=top_student(n)
print(a)
