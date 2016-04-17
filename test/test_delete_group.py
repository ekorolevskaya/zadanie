#занятие 2
#задание 6
from model.group import Group

def test_delete_group(app):
    app.group.delete_first_group()
