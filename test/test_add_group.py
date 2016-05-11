from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", logo="", comment="")] +[
        Group(name=random_string("name=", 10), logo=random_string("logo", 20), comment=random_string("comment", 20))
        for i in range(5)
]

#testdata = [
#        Group(name=name, logo=logo, comment=comment)
#        for name in ["", random_string("name=", 10)]
#        for logo in ["", random_string("logo", 20)]
#        for comment in ["", random_string("comment", 20)]
#]


@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    #добавляем сортировку sorted для списка по id, чтобы группы шли в одинаковом порядке
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

