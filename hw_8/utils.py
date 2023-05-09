import json
from question import Question
from random import shuffle


def load_questions(file_path):
    """
    Читает файл json, выгружает вопросы
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    questions = []

    for item in data:
        text = item['q']
        difficulty = int(item['d'])
        right_answer = item['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions


def shuffle_list(lst):
    """
    Возвращает перемешанный список
    """
    shuffle(lst)
    return lst


def calculate_results(questions):
    """
    Считает итоги
    """
    lenght_questions = len(questions)
    points = 0
    count = 0

    for question in questions:
        if question.is_correct():
            points += question.points
            count += 1

    return f'''Вот и всё!
Отвечено {count} вопроса из {lenght_questions}
Набрано баллов: {points}
'''
