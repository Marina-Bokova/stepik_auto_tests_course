from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # говорим Selenium проверять в течение 15 секунд, цена не снизится
    text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку
    button_book = browser.find_element(By.CSS_SELECTOR, "#book")
    button_book.click()

    # Вычислить значение, требуемое для ввода в поле
    num_x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    print(num_x)
    y = calc(num_x)
    print(y)

    # Заполнение поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
