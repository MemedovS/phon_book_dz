from datetime import datetime

phone_book = {}
path = 'phone_book.txt'
SEPARATOR = ';'


def open_phone_book():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):
        contact_data = contact.strip().split(SEPARATOR)
        contact_data.append(datetime.now().strftime('%H:%M:%S'))# если надо полное время  меняем-> %Y-%m-%d %H:%M:%S
        phone_book[u_id] = contact_data


def save_phone_book():
    global phone_book
    data = []
    for contact in phone_book.values():
        data.append(SEPARATOR.join(contact))  # Сохраняем без даты если ставим [:-1]
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_new_contact(new_contact: list[str]):
    global phone_book
    new_contact.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # Добавляем текущую дату
    phone_book[_next_id()] = new_contact


def _next_id():
    global phone_book
    return max(phone_book) + 1 if phone_book else 1


def find_contact(search_word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for u_id, contakt in phone_book.items():
        if search_word.lower() in ' '.join(contakt).lower():
            result[u_id] = contakt
    return result


def edit_contact(u_id: int, edited_contact: list[str]):
    global phone_book
    current_contact = phone_book[u_id]
    for i in range(3):
        current_contact[i] = edited_contact[i] if edited_contact[i] else current_contact[i]
    phone_book[u_id] = current_contact
    return current_contact[0]


def delet_contact(u_id: int) -> str:
    global phone_book
    return phone_book.pop(u_id)[0]
