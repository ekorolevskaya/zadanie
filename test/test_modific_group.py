#занятие 2
#задание 6
#задание 7
from model.group import Group


def test_modific_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modific_first_group(Group(name="new name"))
    app.session.logout()

def test_modific_group_logo(app):
    app.session.login(username="admin", password="secret")
    app.group.modific_first_group(Group(logo="new logo"))
    app.session.logout()
