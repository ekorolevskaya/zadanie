from sys import maxsize


class Contact:

    def __init__(self, firstname=None, Middle=None, lastname=None, Nickname=None,
                 Title=None, Company=None, adress=None, homephone=None,
                 mobilephone=None, workphone=None, fax=None, email=None,
                 email2=None, email3=None, year=None, adres_2=None,
                 phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.Middle = Middle
        self.lastname = lastname
        self.Nickname = Nickname
        self.Title = Title
        self.Company = Company
        self.adress = adress
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.year = year
        self.adres_2 = adres_2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
       return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize