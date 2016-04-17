#занятие 2
#задание 7
from model.contact import Contact



def test_modific_contact_username(app):
    app.contact.modific_first_contact(Contact(name="Elena modific"))

def test_modific_contact_Last_name(app):
    app.contact.modific_first_contact(Contact(Last_name="Korolevskaya modific"))

