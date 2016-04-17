#занятие 2
#задание 7
from model.contact import Contact



def test_modific_contact_username(app):
    app.session.login(username="admin", password="secret")
    app.contact.modific_first_contact(Contact(name="Elena modific"))
    app.session.logout()

def test_modific_contact_Last_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modific_first_contact(Contact(Last_name="Korolevskaya modific"))
    app.session.logout()

