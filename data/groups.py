from model.group import Group
#import random
#import string


constant = [
    Group(name="name1", logo="logo1", comment="comment1"),
    Group(name="name2", logo="logo2", comment="comment2")
]


#задание 6.3-6.4
#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", logo="", comment="")] +[
#        Group(name=random_string("name=", 10), logo=random_string("logo", 20), comment=random_string("comment", 20))
#        for i in range(5)
#]
