import re

def test_email_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.email == clear(contact_from_edit_page.email)
    assert contact_from_home_page.email2 == clear(contact_from_edit_page.email2)
    assert contact_from_home_page.email3 == clear(contact_from_edit_page.email3)

def test_email_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3


def clear(s):
    return re.sub("[() -]", "", s)
