

def test_phones_on_home_page(app):
    #app.open_contacts_page()
    contact_from_contacts_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_contacts_page.Home_telephone == contact_from_edit_page.Home_telephone
    assert contact_from_contacts_page.workphone == contact_from_edit_page.workphone
    assert contact_from_contacts_page.Mobile == contact_from_edit_page.Mobile
    assert contact_from_contacts_page.phone2 == contact_from_edit_page.phone2