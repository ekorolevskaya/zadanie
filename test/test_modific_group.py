#занятие 2
#задание 6
#задание 7
from model.group import Group


def test_modific_group_name(app):
    app.group.modific_first_group(Group(name="new name"))

def test_modific_group_logo(app):
    app.group.modific_first_group(Group(logo="new logo"))
