#занятие 2
#задание 6
from model.group import Group

def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modific_group()
    app.group.modific_group(Group(name="new_1", logo="mimi_1", comment="comment_1"))
    app.session.logout()
