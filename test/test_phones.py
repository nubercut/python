import re
from random import randrange
from model.contact import Contact
def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.tel_home == contact_from_edit_page.tel_home
    assert contact_from_view_page.tel_work == contact_from_edit_page.tel_work
    assert contact_from_view_page.tel_mobile == contact_from_edit_page.tel_mobile
    assert contact_from_view_page.phone_2 == contact_from_edit_page.phone_2

def test_random_user_homepage_details(app):
    contacts_from_homepage_details = app.contact.get_contact_list()
    index = randrange(len(contacts_from_homepage_details))
    random_contact_from_homepage = app.contact.get_contact_list()[index]
    random_contact_from_editpage = app.contact.get_contact_info_from_edit_page(index)
    assert random_contact_from_homepage.id == random_contact_from_editpage.id
    assert random_contact_from_homepage.firstname == random_contact_from_editpage.firstname
    assert random_contact_from_homepage.lastname == random_contact_from_editpage.lastname
    assert random_contact_from_homepage.address == random_contact_from_editpage.address
    assert random_contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(random_contact_from_editpage)
    assert random_contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(random_contact_from_editpage)


def test_contacts_assertion_from_homepage_and_db(app, json_contacts, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(json_contacts)
    contacts_from_homepage = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert sorted(contacts_from_homepage, key=Contact.id_or_max) == sorted(map(clear_contact, contacts_from_db),
                                                                           key=Contact.id_or_max)
    for i, contact in enumerate(sorted(contacts_from_homepage, key=Contact.id_or_max)):
        assert contact.lastname == clear_space(contacts_from_db[i].lastname)
        assert contact.firstname == clear_space(contacts_from_db[i].firstname)
        assert contact.address == clear_space(contacts_from_db[i].address)
        assert contact.all_emails_from_homepage == merge_emails_like_on_homepage(contacts_from_db[i])
        assert contact.all_phones_from_homepage == merge_phones_like_on_homepage(contacts_from_db[i])

def clear(s):
    return re.sub("[() -]", "", s)

def clear_space(s):
    return " ".join(s.split()) if s is not None else ""

def clear_address_spaces(s):
    return re.sub(" +", " ", re.sub(" \n", "\n", re.sub("\n ", "\n", s))).strip() if s is not None else ""

def clear_contact(contact):
    _ = clear_space
    __ = clear_address_spaces
    return Contact(firstname=_(contact.firstname), middlename=contact.middlename,
                   lastname=_(contact.lastname), nickname=contact.nickname,
                   title=contact.title, company=contact.company,
                   address=__(contact.address), tel_mobile=_(contact.tel_mobile),
                   tel_home=_(contact.tel_home), tel_work=_(contact.tel_work),
                   tel_fax=_(contact.tel_fax), email_1=_(contact.email_1),
                   email_2=_(contact.email_2), email_3=_(contact.email_3),
                   homepage=contact.homepage, bday_day=contact.bday_day, bday_month=contact.bday_month,
                   bday_year=contact.bday_year, aday_day=contact.aday_day, aday_month=contact.aday_month, aday_year=contact.aday_year,
                   address_2=contact.address_2, phone_2=_(contact.phone_2),
                   notes=contact.notes, id=contact.id,
                   all_emails_from_homepage=merge_emails_like_on_homepage(contact),
                   all_phones_from_homepage=merge_phones_like_on_homepage(contact))

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.tel_home, contact.tel_mobile,
                                                                 contact.tel_work, contact.phone_2]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x is not None and x != "",
                            [clear_space(contact.email_1), clear_space(contact.email_2), clear_space(contact.email_3)]))