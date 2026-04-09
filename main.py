from grades_manager import initialize_dict, add_student, get_students, avg_by_student


def main():
    print("Welcome to the Student Grades Manager!\n")

    my_grades = {}

    while True:
        print("Select an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")

        choice = input().strip()

        # Opción 1: Agregar estudiante
        if choice == "1":
            my_grades = add_student(my_grades)

        # Opción 2: Mostrar promedios
        elif choice == "2":
            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students")

            sub_choice = input().strip().lower()

            if sub_choice == "a":
                avg_by_student(my_grades)

            elif sub_choice == "b":
                print("Enter student names (comma-separated):")
                names_input = input().strip()

                # Convertir a lista
                names_list = [name.strip() for name in names_input.split(",")]

                avg_by_student(my_grades, names_list)

            else:
                print("Invalid option selected!")

        # Opción 3: Salir
        elif choice == "3":
            print("Goodbye!")
            break

        # Opción inválida
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()