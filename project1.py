# Student Marks Management System

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks (out of 100): "))
    students[name] = marks
    print(f"Student '{name}' added successfully!\n")

def view_all_students():
    if not students:
        print("No students found.\n")
        return
    print("\n--- Student List ---")
    for name, marks in students.items():
        print(f"{name}: {marks}")
    print()

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print(f"{name}'s marks: {students[name]}\n")
    else:
        print("Student not found.\n")

def show_statistics():
    if not students:
        print("No students to show statistics.\n")
        return
    total = sum(students.values())
    count = len(students)
    average = total / count
    highest = max(students.values())
    lowest = min(students.values())
    print("\n--- Statistics ---")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}\n")

def main():
    while True:
        print("=== Student Marks Management ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Show Statistics")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            show_statistics()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main()

