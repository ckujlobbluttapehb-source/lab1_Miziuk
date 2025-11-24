groupmates = [
    {
        "name": "Николай",
        "surname": "Мизюк",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Никита",
        "surname": "Кирсанов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Полина",
        "surname": "Кирсанова",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Марат",
        "surname": "Орлов",
        "exams": ["Математический анализ", "Физика", "Иностранный язык"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Анна",
        "surname": "Афанасьева",
        "exams": ["Химия", "Биология", "История"],
        "marks": [5, 4, 4]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), 
              str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def filter_students_by_average(students, min_average):
    filtered_students = []
    for student in students:
        average = sum(student["marks"]) / len(student["marks"])
        if average >= min_average:
            filtered_students.append(student)
    return filtered_students

# Основная программа
if __name__ == "__main__":
    print("Список всех студентов:")
    print_students(groupmates)
    
    print("\n" + "="*50)
    
    try:
        min_avg = float(input("\nВведите минимальный средний балл для фильтрации: "))
        
        filtered = filter_students_by_average(groupmates, min_avg)
        
        if filtered:
            print(f"\nСтуденты со средним баллом >= {min_avg}:")
            print_students(filtered)
        else:
            print(f"\nНет студентов со средним баллом >= {min_avg}")
            
    except ValueError:
        print("Ошибка! Введите числовое значение для среднего балла.")