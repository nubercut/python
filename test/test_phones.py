import re
from random import randrange

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_view_page.tel_work == contact_from_edit_page.tel_work
    assert contact_from_view_page.tel_mobile == contact_from_edit_page.tel_mobile
    assert contact_from_view_page.phone_2 == contact_from_edit_page.phone_2

def test_random_user_homepage_details(app):
    contacts_from_homepage_details = app.contact.get_contact_list()
    index = randrange(len(contacts_from_homepage_details))
    random_contact_from_homepage = app.contact.get_contact_list()[index]
    random_contact_from_editpage = app.contact.get_contact_info_from_edit_page(index)
    assert random_contact_from_homepage.firstname == random_contact_from_editpage.firstname
    assert random_contact_from_homepage.lastname == random_contact_from_editpage.lastname
    assert random_contact_from_homepage.address == random_contact_from_editpage.address
    assert random_contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(random_contact_from_editpage)
    assert random_contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(random_contact_from_editpage)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.tel_home, contact.tel_mobile,
                                                                 contact.tel_work, contact.phone_2]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email_1, contact.email_2, contact.email_3]))