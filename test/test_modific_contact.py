# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_modific_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Elena", lastname="New"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    contact = Contact(firstname="Elena modific", lastname="New")
    contact.id = random_contact.id
    app.modific_contact_by_id(contact.id)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    #assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_modific_contact_Last_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(name="Elena", Middle="Yrevna", Last_name="Korolevskaya", Nickname="ekorolevskaya",
#                    Title="Title", Company="Name", Adress="Mira 2", Home_telephone="656506", Mobile="89632547821",
#                    year="1992", adres_2="Adress 2", phone2="dgdrhtj", notes="segsrhr"))
#    app.contact.modific_first_contact(Contact(Last_name="Korolevskaya modific"))

