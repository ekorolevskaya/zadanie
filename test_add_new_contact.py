# -*- coding: utf-8 -*-
# занятие 2
# задание 4
import pytest
from contact import Contact
from application_for_contact import Application_for_contact


@pytest.fixture
def app(request):
    fixture = Application_for_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact_1(app):
    app.login(login="admin", password="secret")
    app.open_contact_page()
    app.create_new_contact(Contact(name="Elena", Middle="Yrevna", Last_name="Korolevskaya", Nickname="ekorolevskaya",
                    Title="Title", Company="Name", Adress="Mira 2", Home_telephone="656506", Mobile="89632547821",
                    year="1992", adres_2="Adress 2", phone2="dgdrhtj", notes="segsrhr"))
    app.return_to_contact_page()
    app.logout()

def test_add_contact_2(app):
    app.login(login="admin", password="secret")
    app.open_contact_page()
    app.create_new_contact(Contact(name="test", Middle="", Last_name="", Nickname="",
                    Title="", Company="", Adress="", Home_telephone="", Mobile="",
                    year="", adres_2="", phone2="", notes=""))
    app.return_to_contact_page()
    app.logout()

