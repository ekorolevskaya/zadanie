# занятие 2
# задание 5

class GroupHelper:


    # конструктор
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # название группы
        wd.find_element_by_name("new").click()
        # открытие формы для заполнения полей группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.logo)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.comment)
        # нажимаем на кнопку Сохранить группу
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        # отправляемся на страницу со списком групп
        wd = self.app.wd
        self.open_groups_page()
        # выбираем первую группу
        wd.find_element_by_name("selected[]").click()
        # удаляем первую группу
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modific_first_group(self, group):
        # отправляемся на страницу со списком групп
        wd = self.app.wd
        self.open_groups_page()
        # выбираем группу
        wd.find_element_by_name("selected[]").click()
        # нажимаем на кнопку Edit
        wd.find_element_by_name("edit").click()
        # меняем текст в полях
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.logo)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.comment)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
