from model.contact import Contact
import random
from model.group import Group

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)

def test_delete_contact_from_group(app, db):
    groups = db.get_group_list()
    if not groups:
        app.group.create(Group(name="Added group"))
        groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contacts_in_group(group)
    if not contacts:
        app.contact.create_contact(Contact(firstname="Added Contact"))
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_random_group(contact, group)
        contacts = db.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.remove_contact_from_group(contact, group)
    assert not contact in db.get_contacts_in_group(group)
