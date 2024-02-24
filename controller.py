import text
import model
import viev


def find_contact(message):
    search_word = viev.input_data(message)
    result = model.find_contact(search_word)
    viev.show_contact(result, text.find_contact_no_result(search_word))
    return True if result else False


def start_app():
    while True:
        user_choice = viev.show_main_menu()
        match user_choice:
            case 1:
                model.open_phone_book()
                viev.show_mesage(text.phon_book_opend_successful)
            case 2:
                model.save_phone_book()
                viev.show_mesage(text.phon_book_saved_successful)

            case 3:
                viev.show_contact(model.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = viev.input_data(text.input_new_contact)
                model.add_new_contact(new_contact)
                viev.show_mesage(text.new_contact_added_successful(new_contact[0]))

            case 5:
                find_contact(text.input_search_word)

            case 6:
                if find_contact(text.input_search_word_for_edit):
                    u_id = int(viev.input_data(text.input_id_for_edit))
                    edited_contact = viev.input_data(text.edit_contact)
                    name = model.edit_contact(u_id, edited_contact)
                    viev.show_mesage(text.edit_contact_successful(name))
            case 7:
                if find_contact(text.input_search_word_for_delet):
                    u_id = int(viev.input_data(text.input_id_for_delet))

                    name = model.delet_contact(u_id)
                    viev.show_mesage(text.delet_contact_successful(name))
            case 8:
                break
