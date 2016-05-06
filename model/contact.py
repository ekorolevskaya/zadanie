from sys import maxsize


class Contact:

    def __init__(self, firstname=None, Middle=None, lastname=None, Nickname=None,
                 Title=None, Company=None, address=None, homephone=None,
                 mobilephone=None, workphone=None, fax=None, email=None,
                 email2=None, email3=None, year=None, addres_2=None,
                 phone2=None, notes=None, id=None, all_phones_from_home_page=None, all_email_from_home_page=None):
        self.firstname = firstname
        self.Middle = Middle
        self.lastname = lastname
        self.Nickname = Nickname
        self.Title = Title
        self.Company = Company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.year = year
        self.addres_2 = addres_2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
       return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize