# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modific_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Elena"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Elena modific")
    contact.id = old_contacts[0].id
    app.contact.modific_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modific_contact_Last_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(name="Elena", Middle="Yrevna", Last_name="Korolevskaya", Nickname="ekorolevskaya",
#                    Title="Title", Company="Name", Adress="Mira 2", Home_telephone="656506", Mobile="89632547821",
#                    year="1992", adres_2="Adress 2", phone2="dgdrhtj", notes="segsrhr"))
#    app.contact.modific_first_contact(Contact(Last_name="Korolevskaya modific"))

