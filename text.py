main_menu = ['Главное меню',
             'Открыть телефонную книгу',
             'Сохранить телефонную книгу',
             'Показать контакт',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

choise_main_menu = f'Выберитье пункт меню ({1}--{len(main_menu) - 1}:)'
choise_main_menu_error = f'Нужно вести число от 1 до {len(main_menu)}!'

phon_book_opend_successful = 'Телефонная книга открыта успешно!'
phon_book_saved_successful = 'Телефонная книга  успешно сохранена!'

empty_phone_book_error = 'Телефонная книга пуста или не открыта'
input_new_contact = ['Введитье имя контакта:',
                     'Введить номер контакта:',
                     'Введитье коментарий для контакта:']
no_changes = '(Или ENTER, чтобы оставить без изменений)'
edit_contact = [f'Введитье новое имя({no_changes}):',
                f'Введитье новый телефон имя({no_changes}):',
                f'Введитье новый коментарий({no_changes}):']

input_search_word = 'Введитье слово для поиска'
input_search_word_for_edit = 'Введитье слово для поиска контакта хотьите изменить:'
input_search_word_for_delet = 'Введитье слово для поиска контакта который хотьите хотьите удалить:'
input_id_for_edit = 'Введить ID контакта который хотьите изменить: '
input_id_for_delet = 'Введить ID контакта который хотьите удалить: '


def new_contact_added_successful(name: str) -> str:
    return f'Контакт"{name}" успешно добавлен!'


def find_contact_no_result(word: str) -> str:
    return f'Контакты содержащие "{word}"не найдены!'


def edit_contact_successful(name) -> str:
    return f'Котнакт "{name}"уснешно изменен!'


def delet_contact_successful(name) -> str:
    return f'Котнакт "{name}"уснешно удален!'
