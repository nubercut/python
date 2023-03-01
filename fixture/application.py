from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
class Application:
    wd: WebDriver

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost:8085/addressbook/")
    def destroy(self):
        self.wd.quit()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()