# Parte I
def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}


# Parte II
def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}

    # Nombre del estudiante
    print("Enter student name:")
    name = input().strip().title()

    subjects = {}

    while True:
        print("Enter subject and grade (or 'exit' to finish):")
        entry = input().strip()

        if entry.lower() == "exit":
            break

        try:
            subject, grade = entry.split(",")
            subject = subject.strip().title()
            grade = float(grade.strip())
            subjects[subject] = grade
        except ValueError:
            # Si el formato es incorrecto, simplemente ignora y sigue
            continue

    student_grades[name] = subjects

    print(f"Student {name} successfully added to the grades management system.")

    return student_grades


# Parte III
def get_students(student_grades, keys):
    result = {}

    # Crear un diccionario auxiliar para búsqueda case-insensitive
    lower_map = {k.lower(): k for k in student_grades}

    for name in keys:
        key_lower = name.lower()

        if key_lower in lower_map:
            real_name = lower_map[key_lower]
            result[real_name] = student_grades[real_name]
        else:
            print(f"{name.title()} not found!")

    return result


# Parte IV
def avg_by_student(student_grades, keys=None):
    # Determinar qué estudiantes usar
    if keys is None:
        selected = student_grades
    else:
        selected = get_students(student_grades, keys)

    for student, subjects in selected.items():
        if subjects:
            avg = sum(subjects.values()) / len(subjects)
        else:
            avg = 0.0

        print(f"{student}: {avg:.1f}")