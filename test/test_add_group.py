from model.group import Group
import pytest
import random
import string


testdata = [
        Group(name="fdhsdgfg", logo="sfdgh", comment="sdrfgth"),
        Group(name="", logo="", comment=""),
]


@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_add_group(app, group):
    pass
    #old_groups = app.group.get_group_list()
    #app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    #new_groups = app.group.get_group_list()
    #old_groups.append(group)
    # добавляем сортировку sorted для списка по id, чтобы группы шли в одинаковом порядке
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

