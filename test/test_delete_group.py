#занятие 2
#задание 6
from model.group import Group

def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
