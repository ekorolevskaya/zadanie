#занятие 2
#задание 6
from model.contact import Contact



def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Elena", Middle="Yrevna", Last_name="Korolevskaya", Nickname="ekorolevskaya",
                    Title="Title", Company="Name", Adress="Mira 2", Home_telephone="656506", Mobile="89632547821",
                    year="1992", adres_2="Adress 2", phone2="dgdrhtj", notes="segsrhr"))
    app.contact.delete_first_contact()
