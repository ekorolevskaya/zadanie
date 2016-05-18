from model.contact import Contact
import re

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
        self.change_field_value("firstname",  contact.firstname)
        self.change_field_value("middlename", contact.Middle)
        self.change_field_value("lastname",   contact.lastname)
        self.change_field_value("nickname",   contact.Nickname)
        self.change_field_value("title",      contact.Title)
        self.change_field_value("company",    contact.Company)
        self.change_field_value("address",    contact.address)
        self.change_field_value("home",       contact.homephone)
        self.change_field_value("mobile",     contact.mobilephone)
        self.change_field_value("work",       contact.workphone)
        self.change_field_value("email",      contact.email)
        self.change_field_value("email2",     contact.email2)
        self.change_field_value("email3",     contact.email3)
        # заполняем число и месяц рождения
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[28]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[28]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").click()
        # заполняем год рождения
        self.change_field_value("byear",    contact.byear)
        self.change_field_value("address2", contact.addres_2)
        self.change_field_value("phone2",   contact.phone2)
        self.change_field_value("notes",    contact.notes)

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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # подтверждаем удаление
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modific_first_contact(self):
        self.modific_contact_by_index(0)

    def modific_contact_by_index(self, index, contact):
        # отправляемся на страницу со списком групп
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # нажимаем на кнопку редактировать
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # меняем текст в полях
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_contacts_page()
        self.contact_cache = None

    def modific_contact_by_id(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(new_contact_data.id)
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                adress = cells[3].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=adress,
                                                  all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, phone2=phone2)

    def add_contact_to_group(self, id):
        wd = self.app.wd
        wd.find_element_by_id("%s" % id).click()
        if not wd.find_element_by_xpath("//div[@class='right']/select//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@class='right']/select//option[12]").click()
        wd.find_element_by_name("add").click()
        self.open_contacts_page()

    def delete_contact_from_group(self, id):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//form[@id='right']/select//option[14]").is_selected():
            wd.find_element_by_xpath("//form[@id='right']/select//option[14]").click()

        wd.find_element_by_id("%s" % id).click()
        wd.find_element_by_name("remove").click()
        self.open_contacts_page()








