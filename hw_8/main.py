from utils import load_questions, calculate_results, shuffle_list

if __name__ == '__main__':
    filename = 'data/questions.json'
    questions = load_questions(filename)
    shuffled_questions = shuffle_list(questions)

    for question in shuffled_questions:
        print(question.build_question())
        user_answer = input('Ваш ответ: ')
        question.user_answer = user_answer
        print(question.build_feedback())

    print('')
    print(calculate_results(questions))
