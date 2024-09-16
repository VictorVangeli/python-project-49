import random

username = ''


def welcome_user_be():
    """
    Приглашает пользователя ввести свое имя, а затем приветствует его по имени
    """
    global username
    while not username.strip():
        username = input("May I have your name? ")
    print(f'Hello, {username}!')


def ask_is_even():
    """
    Предлагает пользователю ввести 'yes' или 'no' в зависимости от того было предложено четное или нечетное число

    Функция генерирует случайное число и просит пользователя указать, является ли оно четным, вводя 'yes' для четных
    чисел и 'no' для нечетных. Пользователю нужно правильно ответить три раза подряд.
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
            print(f'Let\'s try again, {username}!')
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
    welcome_user_be()
    ask_is_even()


if __name__ == '__main__':
    main()
