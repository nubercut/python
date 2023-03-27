from selenium.webdriver.support.select import Select
from model.contact import Contact
import re

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
        self.contact_cache = None

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.submit_first_contact_deletion()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def submit_first_contact_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def modify_test_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_modify_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        self.update_modify_changes(wd)
        self.app.return_to_home_page()
        self.contact_cache = None


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

    def select_modify_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("[name=entry]"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_homepage=all_phones, all_emails_from_homepage=all_emails, address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        tel_home = wd.find_element_by_name("home").get_attribute("value")
        tel_work = wd.find_element_by_name("work").get_attribute("value")
        tel_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_2 = wd.find_element_by_name("phone2").get_attribute("value")
        email_1 = wd.find_element_by_xpath("//input[@name='email']").get_attribute("value")
        email_2 = wd.find_element_by_xpath("//input[@name='email2']").get_attribute("value")
        email_3 = wd.find_element_by_xpath("//input[@name='email3']").get_attribute("value")
        address = wd.find_element_by_xpath("//textarea[@name='address']").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id,tel_home=tel_home, tel_work=tel_work,
                       tel_mobile=tel_mobile, phone_2=phone_2, email_1=email_1, email_2=email_2, email_3=email_3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        tel_home = re.search("H: (.*)", text).group(1)
        tel_work = re.search("W: (.*)", text).group(1)
        tel_mobile = re.search("M: (.*)", text).group(1)
        phone_2 = re.search("P: (.*)", text).group(1)
        return Contact(tel_home=tel_home, tel_work=tel_work,
                       tel_mobile=tel_mobile, phone_2=phone_2)
