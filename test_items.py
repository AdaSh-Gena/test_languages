from asyncio.windows_events import NULL
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_exist_add_to_cart_button(browser):
	# переход на нужную страницу
    browser.get(link)
    #time.sleep(30)
	# поиск кнопки добавления товара в корзину
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    
    assert button is not NULL, "No add to cart button on page"

