from model.contact import Contact


def test_add_contact_1(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", Middle="Yrevna", lastname="Korolevskaya", Nickname="ekorolevskaya",
                      Title="Title", Company="Name", address="Mira 2", homephone="656506",
                      mobilephone="89632547821", workphone="123", fax="123", email="email",
                      email2="email2", email3="email3", year="1992", addres_2="Address 2",
                      phone2="28956", notes="segsrhr")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
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

