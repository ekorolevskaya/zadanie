# -*- coding: utf-8 -*-
# задание 4
from application import Application
from group import Group

import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="new", logo="mimi", comment="comment"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", logo="", comment=""))
    app.logout()


