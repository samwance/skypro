from utils import load_random_word
from player import Player

name = input("Введите имя игрока: ").title()
word = load_random_word()
player = Player(name)


def start_game():
    """
    Приветствует игрока, запрашивает имя
    """
    print(f'Привет, {name}!')
    print(f'Составьте {len(word.subwords)} слов из слова {word.word}')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop" или "стоп"')
    print('Поехали, ваше первое слово?')


start_game()


def play_game():
    """
    Проводит игру
    """
    player_score = player.count_used_words()
    total_words = len(word.subwords)

    while player_score < total_words:
        user_input = input("Предложите слово: ")

        if user_input.lower() == "stop" or user_input.lower() == "стоп":
            break
        elif len(user_input) < 3:
            print("Слишком короткое слово")
        elif player.is_word_used(user_input):
            print("Уже использовано")
        elif not word.is_valid_subword(user_input):
            print("Неверно")
        else:
            player.add_used_word(user_input)
            player_score += 1
            print("Верно")
    print("Игра завершена")
    print(f"Вы угадали {player_score} слов из {total_words}")


play_game()
