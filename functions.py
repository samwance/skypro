import os
import json


def load_json(path):
    '''
    Читает json файл
    '''
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_students():
    '''
    Загружает список студентов из файла json
    '''
    path = os.path.abspath('data\students.json')
    return load_json(path)


def load_professions():
    '''
    Загружает список профессий из файла json
    '''
    path = os.path.abspath('data\professions.json')
    return load_json(path)


def get_student_by_pk(pk):
    '''
    Выбиарет студента по индексу
    '''
    student_list = load_students()
    if pk > len(student_list):
        print('У нас нет такого студента')
        exit()
    student = student_list[pk - 1]
    print(f'Студент:{student["full_name"]}')
    print(f'Знает: {", ".join(student["skills"])}')
    return student


def get_profession_by_title(title):
    '''
    Выбирает профессию по названию
    '''
    professions_list = load_professions()
    for profession in professions_list:
        if profession["title"] == title.title():
            return profession

    print('Нет такой профессии')
    exit()


def check_fitness(student, profession):
    '''
    Выводит результаты, насколько подходит студент
    '''
    student_has = set(student["skills"]).intersection(profession["skills"])
    student_lacks = set(profession["skills"]).difference(student["skills"])
    fit_percent = round(100 / len(profession["skills"]) * len(student_has))
    return {"has": student_has, "lacks": student_lacks, "fit_percent": fit_percent}

