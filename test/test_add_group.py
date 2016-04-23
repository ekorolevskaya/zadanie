from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="new", logo="mimi", comment="comment")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    # добавляем сортировку sorted для списка по id, чтобы группы шли в одинаковом порядке
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", logo="", comment="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)