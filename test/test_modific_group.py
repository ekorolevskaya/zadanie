#занятие 2
#задание 6
#задание 7
from model.group import Group


def test_modific_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="name modify", logo="logo modify", comment="comment modify"))
    app.session.logout()
