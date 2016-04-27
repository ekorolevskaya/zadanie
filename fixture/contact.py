from model.contact import Contact


class ContactHelper:

    # конструктор
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_new_contact_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("Send e-Mail")) > 0):
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
        self.open_new_contact_page()
        self.fill_contact_form(contact)
        # нажимаем на кнопку Enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        # выбираем первую группу
        wd.find_element_by_name("selected[]").click()


#
    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        # отправляемся на страницу со списком контактов
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # удаляем первый контакт
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # подтверждаем удаление
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modific_first_contact(self):
        self.modific_contact_by_index(0)

    def modific_contact_by_index(self, index, contact):
        # отправляемся на страницу со списком групп
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # нажимаем на кнопку редактировать
        wd.find_elements_by_xpath("//img[@src='icons/pencil.png']")[index].click()
        # меняем текст в полях
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_contacts_page()
        self.contact_cache = None

    def return_to_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                first = element.find_element_by_xpath("./td[3]").text
                lastname = element.find_element_by_xpath("./td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(name=first, Last_name=lastname, id=id))
        return list(self.contact_cache)







