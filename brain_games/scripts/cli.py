import prompt


def welcome_user():
    """
    Приглашает пользователя ввести свое имя, а затем приветствует его по имени.
    """
    name = ''
    while not name.strip():
        name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
