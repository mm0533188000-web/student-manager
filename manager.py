import csv
import os 
def load_students(filename):
    if not os.path.exists (filename):
        return []
    with open(filename, "r" ,encoding="utf-8",newline="") as f:
        
        a=csv.DictReader(f)
    return list(a)

def add_student(students, name, grade, class_name):
    with open(students,"a",encoding="utf-8",newline="") as f:
        c=csv.writer(f)
        c.writerow([name, grade, class_name])
