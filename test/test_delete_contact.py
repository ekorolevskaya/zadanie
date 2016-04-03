#занятие 2
#задание 6
from model.contact import Contact



def delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_page()
    app.contact.delete_contact()
    app.contact.return_to_page()
    app.session.logout()