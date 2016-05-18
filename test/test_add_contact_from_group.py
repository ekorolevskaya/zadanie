from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

def test_add_contact_to_group(app, db):
    base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="firstname"))
    old_contacts = db.get_contact_list()
    old = base.get_contact_in_group(Group(id="191"))
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group(contact.id)
    new = base.get_contact_in_group(Group(id="191"))
    assert len(old) == len(new)
