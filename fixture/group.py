from model.group import Group


class GroupHelper:


    # конструктор
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.logo)
        self.change_field_value("group_footer", group.comment)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # название группы
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # нажимаем на кнопку Сохранить группу
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None


    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        # отправляемся на страницу со списком групп
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # удаляем первую группу
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modific_first_group(self):
        wd = self.app.wd
        self.modific_group_by_index(0)

    def modific_group_by_index(self, index, new_group_data):
        # отправляемся на страницу со списком групп
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # нажимаем на кнопку Edit
        wd.find_element_by_name("edit").click()
        # меняем текст в полях
        self.fill_group_form(new_group_data)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
