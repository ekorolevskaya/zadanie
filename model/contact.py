from sys import maxsize


class Contact:

    def __init__(self, name=None,    Middle=None,     Last_name=None, Nickname=None,
                       Title=None,   Company=None,    Adress=None,    Home_telephone=None,
                       Mobile=None,  workphone=None,  fax=None,       email=None,
                       email2=None,  email3=None,     year=None,      adres_2=None,
                       phone2=None,  notes=None,      id=None):
        self.name = name
        self.Middle = Middle
        self.Last_name = Last_name
        self.Nickname = Nickname
        self.Title = Title
        self.Company = Company
        self.Adress = Adress
        self.Home_telephone = Home_telephone
        self.Mobile = Mobile
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
       return "%s:%s:%s" % (self.id, self.name, self.Last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.Last_name == other.Last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize