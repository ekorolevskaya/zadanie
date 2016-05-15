from model.group import Group
import random

def test_modific_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_modific_group_name"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="new name")
    group.id = random_group.id
    app.modific_group_by_id(group.id)
    assert len(old_groups) == len(db.group.get_group_list())
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modific_group_logo(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test_modific_group_name_logo"))
#    old_groups = app.group.get_group_list()
#    app.group.modific_first_group(Group(logo="new logo"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)