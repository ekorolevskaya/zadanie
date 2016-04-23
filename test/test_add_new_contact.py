from model.contact import Contact


def test_add_contact_1(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Elena", Middle="Yrevna", Last_name="Korolevskaya", Nickname="ekorolevskaya",
                    Title="Title", Company="Name", Adress="Mira 2", Home_telephone="656506", Mobile="89632547821",
                    year="1992", adres_2="Adress 2", phone2="dgdrhtj", notes="segsrhr")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_contact_2(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(name="test", Middle="", Last_name="", Nickname="",
#                    Title="", Company="", Adress="", Home_telephone="", Mobile="",
#                    year="", adres_2="", phone2="", notes="")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

