import pytest

def test_add_to_cart_button(browser,lang):
    link=f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")