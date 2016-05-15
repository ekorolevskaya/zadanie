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
def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    #добавляем сортировку sorted для списка по id, чтобы группы шли в одинаковом порядке
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

