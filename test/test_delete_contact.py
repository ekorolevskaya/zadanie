#занятие 2
#задание 6
from model.contact import Contact



def test_delete_first_contact(app):
    app.contact.delete_first_contact()
