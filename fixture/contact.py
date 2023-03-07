from selenium.webdriver.support.select import Select
class ContactHelper:
    def __init__(self, app):
        self.app = app
    def create_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.add_new_contact()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.app.return_to_home_page()

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        self.submit_first_contact_deletion()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def submit_first_contact_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def modify_test_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.modify_contact()
        self.fill_contact_form(new_contact_data)
        self.update_modify_changes(wd)
        self.app.return_to_home_page()

    def update_modify_changes(self, wd):
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        if contact.file_path != "":
            wd.find_element_by_xpath("//input[@type='file']").send_keys(contact.file_path)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.tel_home)
        self.change_field_value("mobile", contact.tel_mobile)
        self.change_field_value("work", contact.tel_work)
        self.change_field_value("fax", contact.tel_fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.bday_year)
        if contact.bday_day != "-":
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text("%s" % contact.bday_day)
        if contact.bday_month != "-":
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text("%s" % contact.bday_month)
        self.change_field_value("ayear", contact.aday_year)
        if contact.aday_day != "-":
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text("%s" % contact.aday_day)
        if contact.aday_month != "-":
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text("%s" % contact.aday_month)
        self.change_field_value("address2", contact.address_2)
        self.change_field_value("phone2", contact.phone_2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, fieldname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fieldname).click()
            wd.find_element_by_name(fieldname).clear()
            wd.find_element_by_name(fieldname).send_keys(text)

    def modify_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))