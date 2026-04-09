def student_averages(students):
    result = {}

    # Recorrer estudiantes
    for student, assignments in students.items():
        total = 0
        count = 0

        # Recorrer tareas del estudiante
        for grade in assignments.values():
            total += grade
            count += 1

        prom = round(total / count)
        result[student] = prom

    return result
def assignment_averages(students):
    result = {}
    for student, assignments in students.items():
        for assignment, grade in assignments.items():
            if assignment not in result:
                result[assignment] = []
            result[assignment].append(grade)
    for assignment, grades in result.items():
        prom = round(sum(grades) / len(grades))
        result[assignment] = prom
    return result