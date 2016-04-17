# занятие 2
# задание 5

class ContactHelper:


    # конструктор
    def __init__(self, app):
        self.app = app

    def open_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("Number of results")) > 0):
            wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.Middle)
        self.change_field_value("lastname", contact.Last_name)
        self.change_field_value("nickname", contact.Nickname)
        self.change_field_value("title", contact.Title)
        self.change_field_value("company", contact.Company)
        self.change_field_value("address", contact.Adress)
        self.change_field_value("home", contact.Home_telephone)
        self.change_field_value("mobile", contact.Mobile)
        # заполняем число и месяц рождения
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[28]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[28]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").click()
        # заполняем год рождения
        self.change_field_value("byear", contact.year)
        self.change_field_value("address2", contact.adres_2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        # нажимаем на кнопку Enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def select_first_contact(self):
        wd = self.app.wd
        # выбираем первую группу
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        # отправляемся на страницу со списком групп
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        # удаляем первую группу
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # подтверждаем удаление
        wd.switch_to_alert().accept()


    def modific_first_contact(self, contact):
        # отправляемся на страницу со списком групп
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        # нажимаем на кнопку редактировать
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # меняем текст в полях


    def return_to_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_page()
        return len(wd.find_elements_by_name("selected[]"))


