# Лабораторная работа №1
## Установка и начало работы с Python 
Скачиваем с официального сайта Python компилятор. Создаем директорию PIS. В ней создаем файл «helloworld.py» с кодом: ```print("Hello world!")```
Выполняем команду в командной строке 
```
   C:\Users\ASUS> python3 -V       //узнаем версию в командной строке
   Python 3.11.8
```
Запускаем созданный файл
```
cd C:\PIS                    //переходим в нужную директорию
C:\PIS>python3 helloworld.py    // запускаем скрипт запуска файла
Hello world!                    //вывод удался, таким образом, первая программа на Python3 запущена.
```

## Создаем новый файл в директории "mygroup.py" со спиками студентов (моих одногруппников) и их оценками по предметам:
``` groupmates = [
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
```
И также добавляем в файл созданный код для фильтрации студентов:
```
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
```
Вывод после выполнения команды ``` python3 mygroup.py ``` при необходимой средней оценке >= 4.2

<img width="855" height="352" alt="image" src="https://github.com/user-attachments/assets/8fbd85f4-cc63-4a7e-bca8-30183a186936" />

## Начало работы с Django
Переходим на официальный сайт фреймворка Django, где написана команда для установки с указанием последней версии, в моем случае это 
```py -m pip install Django==5.2.8```
После ввода данной команды выидим следующий вывод, который означает, что фреймоврк успешно установлен:

<img width="1062" height="514" alt="image" src="https://github.com/user-attachments/assets/64891993-d4e0-4378-a3a4-997e23a05cbe" />

### Приступим к созданию проекта
Выполнив команду py ```-m django startproject project_name``` создадим папку project_name, в которой автоматически создались новые файлы. Они нужны для модификации проекта.
Далее командой ``` cd project_name ``` перейдем в новую директорию и выполним ```python manage.py runserver ```, которая запускает локальный сервер на порту 8000.

Если ошибок не возникло, то в консоли появится следующее:

<img width="561" height="94" alt="image" src="https://github.com/user-attachments/assets/16c02581-b453-425c-9dea-3a282f42e166" />

Затем перейдите по адресу: http://127.0.0.1:8000/ Если сервер удачно запущен, то будет выведено сообщение:

<img width="955" height="894" alt="image" src="https://github.com/user-attachments/assets/9678ec5e-05ca-496b-974a-de5bacceabff" />

### Изменим параметр NAME базы данных в файле settings.py

<img width="600" height="134" alt="image" src="https://github.com/user-attachments/assets/a5c5d42b-8a11-42e6-9dca-76b0a5364ab0" />

Для создания таблицы базы данных, перейдем в директорию project_name и через командную строку выполним команду:
```
python3 manage.py migrate
```

Затем создаем суперпользователя:
```
C:\PIS\project_name>python3 manage.py createsuperuser
Username (leave blank to use 'asus'): asus
Email address: ckujlobbluttapehb@gmail.com
Password:  //сюда был введен пароль
Password (again):
This password is too short. It must contain at least 8 characters.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y  //подтвердили
Superuser created successfully.
```

Теперь необходимо запустить сервер командой:

```
python3 manage.py runserver 
```
и в браузере пройти по адресу http://127.0.0.1:8000/admin/.

### В случае успеха увидим следующее:

<img width="497" height="387" alt="image" src="https://github.com/user-attachments/assets/1ab28021-3a7e-4ea9-9c6a-aee89d970dd3" />

Авторизовываемся и наблюдаем главную страницу административной панели. Здесь же создадим нового пользователя с правами суперпользователя, а потом забаним его)

<img width="951" height="909" alt="image" src="https://github.com/user-attachments/assets/1cdd8e37-a991-4413-9086-c05dca09e8bf" />












