from sys import maxsize
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, file_path="", title=None,
                 company=None, address=None, tel_home=None, tel_mobile=None, tel_work=None, tel_fax=None, email_1=None,
                 email_2=None, email_3=None, homepage=None, bday_day="-", bday_month="-", bday_year=None,
                 aday_day="-", aday_month="-", aday_year=None, notes=None, address_2=None, phone_2=None, id=None,
                 all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.file_path = file_path
        self.title = title
        self.company = company
        self.address = address
        self.tel_home = tel_home
        self.tel_mobile = tel_mobile
        self. tel_work = tel_work
        self.tel_fax = tel_fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.bday_day = bday_day
        self.bday_month = bday_month
        self.bday_year = bday_year
        self.aday_day = aday_day
        self.aday_month = aday_month
        self.notes = notes
        self.address_2 = address_2
        self.aday_year = aday_year
        self.phone_2 = phone_2
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)\
            and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)\
            and (self.address is None or other.address is None or self.address == other.address)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize