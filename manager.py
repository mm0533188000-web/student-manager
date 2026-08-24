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
            suni+=int(average.get("grade"))
            how+=1
    
            if how == 0:
                return how
    return  suni / how


n = load_students("students.csv")
# a = find_student(n, "Noa")
a=class_average(n,"10A")
print(a)
