#занятие 2
#задание 6
from model.group import Group

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_delete_group"))
    app.group.delete_first_group()
