import pytest
from selenium.webdriver.common.by import By
import time
import math

links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236897/step/1",
         # "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236896/step/1",
         # "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('link', links)
def test_correct_feedback_message(browser, link):
    browser.get(link)

    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()

    mes = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    assert mes == "Correct!", f"Feedback message isn't correct: {mes}"
