from model.contact import Contact


def test_add_contact_1(app):
    app.contact.open_new_contact_page()
    app.contact.create(Contact(name="Elena", Middle="Yrevna", Last_name="Korolevskaya", Nickname="ekorolevskaya",
                    Title="Title", Company="Name", Adress="Mira 2", Home_telephone="656506", Mobile="89632547821",
                    year="1992", adres_2="Adress 2", phone2="dgdrhtj", notes="segsrhr"))
    app.contact.return_to_page()

def test_add_contact_2(app):
    app.contact.open_new_contact_page()
    app.contact.create(Contact(name="test", Middle="", Last_name="", Nickname="",
                    Title="", Company="", Adress="", Home_telephone="", Mobile="",
                    year="", adres_2="", phone2="", notes=""))
    app.contact.return_to_page()