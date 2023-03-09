from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.modify_test_contact(Contact(firstname="Modified", middlename="Modified", lastname="Modified", nickname="Modified",
                            file_path="", title="Modified", company="Modified", address="This is Modified",
                            tel_home="Modified", tel_mobile="Modified", tel_work="Modified", tel_fax="Modified",
                            email_1="email@client.com", email_2="email2@client.com", email_3="email3@client.com",
                            homepage="homeeeeee", bday_day="11", bday_month="December", bday_year="1995", aday_day="16",
                            aday_month="November", notes="Modified", address_2="address2", aday_year="2000",
                            phone_2="yes"))

def test_modify_birthday(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.modify_test_contact(Contact(bday_day="13", bday_month="October", bday_year="2000"))