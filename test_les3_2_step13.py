import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_successful_registration(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(self.fill_registration_form(link1), "Congratulations! You have successfully registered!",
                         "Not all fields are filled")

    def test_unsuccessful_registration(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(self.fill_registration_form(link2), "Congratulations! You have successfully registered!",
                         "Not all fields are filled")

    def fill_registration_form(self, link):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@test.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text


if __name__ == "__main__":
    unittest.main()
