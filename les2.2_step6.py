from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Вычислить значение, требуемое для ввода в поле
    num_x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    print(num_x)
    y = calc(num_x)
    print(y)

    # Заполнение поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Выполнить скролл и дозаполнять форму
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.click()


    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
