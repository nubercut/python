# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "" * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            address=random_string("address", 20))
    for i in range(5)
    ]

def test_add_contact(app, db, json_contacts, check_ui):
    contact_added = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_contact(contact_added)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact_added)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(),
                                                                     key=Contact.id_or_max)

