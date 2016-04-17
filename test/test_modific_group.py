#занятие 2
#задание 6
#задание 7
from model.group import Group


def test_modific_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_modific_group_name"))
    old_groups = app.group.get_group_list()
    group = Group(name="new name")
    group.id = old_groups[0].id
    app.group.modific_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modific_group_logo(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test_modific_group_name_logo"))
#    old_groups = app.group.get_group_list()
#    app.group.modific_first_group(Group(logo="new logo"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)