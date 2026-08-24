<!-- Step 1: Load Students (load_students)

Checks if the CSV file exists using the os module.

Reads student records using csv.DictReader into a list of dictionaries, or returns an empty list if the file is missing.

Step 2: Save Students (save_students)

Opens the CSV file in write mode ("w") with utf-8 encoding.

Uses csv.DictWriter with defined fieldnames (name, grade, class), writes the header first, and saves all current student records back to the file.

Step 3: Add Student (add_student)

Collects student details (name, grade, and class) via interactive terminal inputs.

Validates that the entered grade is strictly between 0 and 100 using a validation loop.

Appends the new student dictionary to the list, updates the CSV file, and confirms successful saving.

Step 4: Find Student (find_student)

Searches through the student list by name.

Returns the matching student dictionary if found, or None otherwise.

Step 5: Class Average & Top Student (class_average & top_student)

Class Average: Filters students by a specific class name, sums their grades, and calculates the average score.

Top Student: Iterates through the student records to find and return the name of the student with the highest grade.

Step 6: Interactive Menu & Exit (print_all)

Implements a while True loop presenting a command-line interface with options ranging from 1 to 6 (viewing, adding, searching, calculating averages, finding the top student, and saving and exiting).

Safely breaks the loop and exits the program upon choosing option 6. -->