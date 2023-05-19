class BasicWord:
    """
    Данное слово и слова, котоыре можно из него составить
    """

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"BasicWord({self.word}, {self.subwords})"

    def is_valid_subword(self, subword):
        """
        Проверяет входит ли слово в список подслов
        """
        return subword in self.subwords

    def count_subwords(self):
        """
        Считает колличество слов, которые можно составить из стандартного
        """
        return len(self.subwords)
