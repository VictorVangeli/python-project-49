import random

from brain_games.scripts.cli import welcome_user


def ask_is_even(username: str):
    """
    Предлагает пользователю ввести 'yes' или 'no' в зависимости от того было предложено четное или нечетное число

    Функция генерирует случайное число и просит пользователя указать, является ли оно четным, вводя 'yes' для четных
    чисел и 'no' для нечетных. Пользователю нужно правильно ответить три раза подряд.

    Args:
        username (str): Имя пользователя.
    """
    counter = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter != 3:
        number = random.randint(1, 100)
        print(f'Question: {number} ')
        answer = input("Your answer: ").strip().lower()
        if answer.strip() == 'yes' and iseven(number) or answer.strip() == 'no' and not iseven(number):
            print('Correct!')
            counter += 1
        else:
            if answer == 'yes':
                print(f'\'yes\' is wrong answer ;(. Correct answer was \'no\'\n'
                      f'Let\'s try again, {username}!')
                break
            else:
                print(f'\'no\' is wrong answer ;(. Correct answer was \'yes\'\n'
                      f'Let\'s try again, {username}!')
                break
    if counter == 3:
        print(f'Congratulations, {username}!')


def iseven(numbers: int) -> bool:
    """
    Проверяет, является ли число четным.

    Args:
        numbers (int): Целое число, которое нужно проверить на четность.

    Returns:
        bool: True, если число четное, иначе False.
    """
    return numbers % 2 == 0


def main():
    username = welcome_user()
    ask_is_even(username)


if __name__ == '__main__':
    main()
