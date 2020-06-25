import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)

    time.sleep(30)

    language = browser.find_element_by_tag_name("html").get_attribute("lang")
    button = browser.find_element_by_id("add_to_basket_form")
    button_text = button.text

    if language == "fr":
        assert "Ajouter au panier" == button_text
    elif language == "es":
        assert "Añadir al carrito" == button_text
    elif language == "en-gb":
        assert "Add to basket" == button_text
    elif language == "ru":
        assert "Добавить в корзину" == button_text
    else:
        raise pytest.UsageError("Используется неизвестный язык")
