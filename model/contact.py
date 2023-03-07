class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, file_path="", title=None,
                 company=None, address=None, tel_home=None, tel_mobile=None, tel_work=None, tel_fax=None, email_1=None,
                 email_2=None, email_3=None, homepage=None, bday_day="-", bday_month="-", bday_year=None,
                 aday_day="-", aday_month="-", aday_year=None, notes=None, address_2=None, phone_2=None):
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