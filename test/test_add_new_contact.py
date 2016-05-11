from model.contact import Contact
import pytest
from random import *
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])

testdata = [Contact(firstname="",   Middle="",      lastname="",    Nickname="",    Title="",
                    Company="",     address="",     homephone="",   mobilephone="",
                    workphone="",   fax="",         email="",       email2="",      email3="",
                    byear="",       addres_2="",    phone2="",      notes="")] + [
        Contact(firstname=random_string("firstname", 10),   Middle=random_string("Middle", 10),         lastname=random_string("lastname", 10),
                Nickname=random_string("Nickname", 10),     Title=random_string("Title", 10),           Company=random_string("Company", 10),
                address=random_string("address", 10),       homephone=random_string("homephone", 10),   mobilephone=random_string("mobilephone", 10),
                workphone=random_string("workphone", 10),   fax=random_string("fax", 10),               email=random_string("email", 10),
                email2=random_string("email2", 10),         email3=random_string("email3", 10),
                byear=random_string("byear", 4),            addres_2=random_string("addres_2", 10),
                phone2=random_string("phone2", 10),         notes=random_string("notes", 10))
        for i in range(3)
]



@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_contact_1(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


