# -*- coding: utf-8 -*-
import pytest
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

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    contact_added = contact
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact_added)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

