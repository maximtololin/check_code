from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    # Проверяем, что кнопка существует и видима на странице
    assert add_to_basket_button and add_to_basket_button.is_displayed(), "Корзина на странице отсутствует!"
    print("Корзина присутствует на странице!")
