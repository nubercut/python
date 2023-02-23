# -*- coding: utf-8 -*-
import unittest
import pytest
from contact import Contact
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Nubar", middlename="Petrosian", lastname="G", nickname="nick",
                            file_path="C:\Нубэрдо.jpg", title="aaaaaaaaaa", company="bercut", address="This is address",
                            tel_home="987654321", tel_mobile="123456789", tel_work="987321456", tel_fax="654456654",
                            email_1="email@client.com", email_2="email2@client.com", email_3="email3@client.com",
                            homepage="homeeeeee", bday_day="11", bday_month="December", bday_year="1995", aday_day="16",
                            aday_month="November", notes="ahahahaha", address_2="address2", aday_year="2000",
                            phone_2="yes"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                            file_path="", title="", company="", address="",
                            tel_home="", tel_mobile="", tel_work="", tel_fax="",
                            email_1="", email_2="", email_3="",
                            homepage="", bday_day="", bday_month="-", bday_year="", aday_day="",
                            aday_month="-", notes="", address_2="", aday_year="",
                            phone_2=""))
    app.logout()

if __name__ == "__main__":
    unittest.main()
