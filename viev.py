import text
from datetime import datetime


def show_main_menu() -> int:
    for i, item in enumerate(text.main_menu):
        if i:
            print(f"\t{i}-{item}")
        else:
            print(item)
    while True:

        choise = input(text.choise_main_menu)
        if choise.isdigit() and 0 < int(choise) < len(text.main_menu):
            return int(choise)
        print(text.choise_main_menu_error)


def show_contact(phone_book: dict[int, [str, datetime]], error_message: str):
    if phone_book:
        print('\n''|' + '=' * 91,'|')
        for u_id, contact in phone_book.items():
            print(f'|{u_id:>3} {contact[0]:<15} | {contact[1]:<20} | {contact[2]:<20}   |  {contact[3]:<20} |')
        print('=' * 93 + '|', '\n')
    else:
        show_mesage(error_message)


def show_mesage(mesage: str):
    print('\n' + '=' * len(mesage))
    print(mesage)
    print('\n' + '=' * len(mesage) + '\n')


def input_data(message) -> list[str] | str:
    if isinstance(message, str):
        return input('\n' + message)
    return [input(mes) for mes in message]
