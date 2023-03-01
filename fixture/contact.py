from selenium.webdriver.support.select import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app
    def create_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        self.add_new_contact(wd)
        # fill contact form
        self.fill_contact_form(contact, wd)
        # submit contact creation
        self.submit_contact_creation(wd)
        self.app.return_to_home_page()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def submit_contact_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Select first contact
        self.select_first_contact(wd)
        # submit deletion
        self.submit_first_contact_deletion(wd)

    def select_first_contact(self, wd):
        wd.find_element_by_name("selected[]").click()

    def submit_first_contact_deletion(self, wd):
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def modify_test_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.modify_contact(wd)
        self.fill_contact_form(contact, wd)
        # submit contact creation
        self.update_modify_changes(wd)
        self.app.return_to_home_page()

    def update_modify_changes(self, wd):
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact, wd):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # добавлено условие для пропуска отправки пустого значения, иначе 2й тест валится
        if contact.file_path != "":
            wd.find_element_by_xpath("//input[@type='file']").send_keys(contact.file_path)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.tel_home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.tel_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.tel_work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.tel_fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("%s" % contact.bday_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("%s" % contact.bday_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.bday_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("%s" % contact.aday_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("%s" % contact.aday_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.aday_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def modify_contact(self, wd):
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

