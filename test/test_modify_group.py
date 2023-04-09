from model.group import Group
import random
def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_modify = Group(name="New test group")
    group_modify.id = group.id
    app.group.modify_group_by_id(group.id, group_modify)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(group_modify)
    assert len(old_groups) == len(new_groups)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)