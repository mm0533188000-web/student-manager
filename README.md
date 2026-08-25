# Student Manager System

A Python-based student management system developed as a final project. The system manages data using a CSV file and allows users to perform various operations through a command-line interface (CLI).

## Features
- **Data Loading:** Reads all student records from the CSV file using `DictReader`.
- **Data Saving:** Saves and updates data cleanly back to the file with appropriate headers.
- **Add Students:** Collects new student details (name, grade, and class) with validation to ensure the grade is strictly between 0 and 100.
- **Find Student:** Allows searching for a specific student by name to retrieve their full details.
- **Calculations:** Calculates class grade averages and identifies the top-performing student with the highest grade.
- **Interactive Menu:** Features a user-friendly main menu to view all data, add, search, delete, generate text reports, and save upon exiting.
- **Error Handling:** Prevents program crashes in case the user inputs invalid values (such as text instead of a numeric grade).

## Project Structure
The project is fully managed using Git version control, where every step was developed, tested, and pushed in separate commits to GitHub.