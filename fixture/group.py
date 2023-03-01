class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        self.init_group_creation(wd)
        # fill group form
        self.fill_group_form(group, wd)
        # submit group creation
        self.submit_group_creation(wd)
        self.return_to_group_page()

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, group, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self, wd):
        wd.find_element_by_name("new").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        self.select_first_group(wd)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        self.select_first_group(wd)
        # submit modyfying
        self.edit_first_group(wd)
        self.fill_group_form(group, wd)
        # submit group creation
        self.update_first_group(wd)
        self.return_to_group_page()

    def update_first_group(self, wd):
        wd.find_element_by_name("update").click()

    def edit_first_group(self, wd):
        wd.find_element_by_name("edit").click()

    def select_first_group(self, wd):
        wd.find_element_by_name("selected[]").click()

    def open_group_page(self):
        # open groups page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
