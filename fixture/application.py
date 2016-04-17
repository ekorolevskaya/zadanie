# занятие 2
# задание 4
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper




class Application:

    def __init__(self):
        # контруктор, который инициализирует ссылку на драйвер и на помощников
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            #какой адрес страницы
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        # навигация
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        # метод разрушает фикстуру
        self.wd.quit()
