from model.group import Group


def test_modific_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_modific_group_name"))
    app.group.modific_first_group(Group(name="new name"))

def test_modific_group_logo(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_modific_group_name_logo"))
    app.group.modific_first_group(Group(logo="new logo"))