from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # Переключится на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Вычислить значение, требуемое для ввода в поле
    num_x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    print(num_x)
    y = calc(num_x)
    print(y)

    # Заполнение поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
