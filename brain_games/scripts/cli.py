
name = ''


def welcome_user():
    """
    Приглашает пользователя ввести свое имя, а затем приветствует его по имени.
    """
    global name
    while not name.strip():
        name = input("May I have your name? ")
    print(f'Hello, {name}!')
