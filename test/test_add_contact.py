# -*- coding: utf-8 -*-
import unittest
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Nubar", middlename="Petrosian", lastname="G", nickname="nick",
                            file_path="C:\Нубэрдо.jpg", title="aaaaaaaaaa", company="bercut", address="This is address",
                            tel_home="987654321", tel_mobile="123456789", tel_work="987321456", tel_fax="654456654",
                            email_1="email@client.com", email_2="email2@client.com", email_3="email3@client.com",
                            homepage="homeeeeee", bday_day="11", bday_month="December", bday_year="1995", aday_day="16",
                            aday_month="November", notes="ahahahaha", address_2="address2", aday_year="2000",
                            phone_2="yes")
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="",
#                            file_path="", title="", company="", address="",
#                            tel_home="", tel_mobile="", tel_work="", tel_fax="",
#                            email_1="", email_2="", email_3="",
#                            homepage="", bday_day="", bday_month="-", bday_year="", aday_day="",
#                            aday_month="-", notes="", address_2="", aday_year="",
#                            phone_2="")
#    app.contact.create_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#if __name__ == "__main__":
#    unittest.main()
