from functions import *


def main():
    pk = int(input("Введите номер студента:\n"))
    student = get_student_by_pk(pk)
    title = input('Выберите специальность для оценки \n')
    profession = get_profession_by_title(title)
    result = check_fitness(student, profession)
    print(f'Пригодность: {result["fit_percent"]}')
    print(f'{student["full_name"]} знает {", ".join(result["has"])}')
    print(f'{student["full_name"]} не знает {", ".join(result["lacks"])}')


if __name__ == '__main__':
    main()
