# -*- coding: utf-8 -*-
# занятие 2
# задание 4
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="new", logo="mimi", comment="comment"))


def test_add_empty_group(app):
    app.group.create(Group(name="", logo="", comment=""))
