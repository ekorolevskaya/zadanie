from model.group import Group
import pytest
#from data.add_group import testdata
from data.groups import constant as testdata



#testdata = [
#        Group(name=name, logo=logo, comment=comment)
#        for name in ["", random_string("name=", 10)]
#        for logo in ["", random_string("logo", 20)]
#        for comment in ["", random_string("comment", 20)]
#]


#@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    #добавляем сортировку sorted для списка по id, чтобы группы шли в одинаковом порядке
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

