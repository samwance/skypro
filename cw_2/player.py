class Player:
    """
    Имя игрока и использованные слова
    """
    def __init__(self, name):
        self.name = name
        self.used_words = set()

    def __repr__(self):
        return f"Player({self.name}, {self.used_words})"

    def count_used_words(self):
        """
        Считает колличество использованных слов
        """
        return len(self.used_words)

    def add_used_word(self, word):
        """
        Добавляет слово в список использованных
        """
        self.used_words.add(word)

    def is_word_used(self, word):
        """
        Проверяет использовано ли слово уже
        """
        return word in self.used_words
