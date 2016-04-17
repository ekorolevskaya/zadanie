#занятие 2
#задание 7
from model.contact import Contact


def test_modific_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modific_first_contact(Contact(name="Elena modific", Middle="Yrevna modific", Last_name="Korolevskaya modific", Nickname="ekorolevskaya modific",
                    Title="Title modific", Company="Name modific", Adress="Mira 2 modific", Home_telephone="656506", Mobile="89632547821",
                    year="1992", adres_2="Adress 2 modific", phone2="dgdrhtj modific", notes="segsrhr modific"))
    app.session.logout()

