

class Question:
    """
    Содержит вопрос и ответ на него
    """
    def __init__(self, text, difficulty, right_answer):
        self.text = text
        self.difficulty = int(difficulty)
        self.right_answer = right_answer

        self.asked = False
        self.user_answer = None
        self.points = self.difficulty * 10


    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.right_answer == self.user_answer


    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'''Вопрос: {self.text}
Сложность {self.difficulty}/5
'''

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        return f'Ответ верный, получено {self.points} баллов\n'

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        print(f'Ответ неверный, верный ответ {self.right_answer}\n')

    def build_feedback(self):
        """
        Определяет реакцию на ответ
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.points} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.right_answer}'