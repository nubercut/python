from model.contact import Contact
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(firstname="Modified", lastname="Modified", address="This is Modified")
    contact_modify.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_modify)
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)

#def test_modify_birthday(app):
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(bday_day="13", bday_month="October", bday_year="2000")
#    contact.id = old_contacts[0].id
#    app.contact.modify_test_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0]= contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
