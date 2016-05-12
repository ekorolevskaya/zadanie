from model.contact import Contact
from random import *
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])

testdata = [Contact(firstname="",   Middle="",      lastname="",    Nickname="",    Title="",
                    Company="",     address="",     homephone="",   mobilephone="",
                    workphone="",   fax="",         email="",       email2="",      email3="",
                    byear="",       addres_2="",    phone2="",      notes="")] + [
        Contact(firstname=random_string("firstname", 10),   Middle=random_string("Middle", 10),         lastname=random_string("lastname", 10),
                Nickname=random_string("Nickname", 10),     Title=random_string("Title", 10),           Company=random_string("Company", 10),
                address=random_string("address", 10),       homephone=random_string("homephone", 10),   mobilephone=random_string("mobilephone", 10),
                workphone=random_string("workphone", 10),   fax=random_string("fax", 10),               email=random_string("email", 10),
                email2=random_string("email2", 10),         email3=random_string("email3", 10),
                byear=random_string("byear", 4),            addres_2=random_string("addres_2", 10),
                phone2=random_string("phone2", 10),         notes=random_string("notes", 10))
        for i in range(3)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))