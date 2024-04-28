
from faker import Faker

import settings
from locators import EntranceLocators

fake = Faker()

class TestEntrance:
    def test_entrance_in_account(self, driver):
        driver.get(settings.URL)
        entrance_in_account_button = driver.find_element(*EntranceLocators.ENTRANCE_IN_ACCOUNT)
        entrance_in_account_button.click()

        email_input = driver.find_element(*EntranceLocators.LOGIN_EMAIL)
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*EntranceLocators.LOGIN_PASSWORD)
        password_input.send_keys(fake.password())

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        entrance_button.click()
        assert driver.current_url == settings.URL + '/login'

    def test_entrance_personal_account(self, driver):
        driver.get(settings.URL)
        entrance_personal_account = driver.find_element(*EntranceLocators.ENTRANCE_PERSONAL_ACCOUNT)
        entrance_personal_account.click()

        email_input = driver.find_element(*EntranceLocators.LOGIN_EMAIL)
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*EntranceLocators.LOGIN_PASSWORD)
        password_input.send_keys(fake.password())

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        entrance_button.click()
        assert driver.current_url == settings.URL + '/login'

    def test_entrance_in_registration(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*EntranceLocators.ENTRANCE_PERSONAL_ACCOUNT)
        personal_account_button.click()

        button_registration = driver.find_element(*EntranceLocators.ENTRANCE_REGISTRATION)
        button_registration.click()

        entrance_registration = driver.find_element(*EntranceLocators.ENTRANCE_TEXT)
        entrance_registration.click()

        email_input = driver.find_element(*EntranceLocators.LOGIN_EMAIL)
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*EntranceLocators.LOGIN_PASSWORD)
        password_input.send_keys(fake.password())

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        entrance_button.click()
        assert driver.current_url == settings.URL + '/login'

    def test_entrance_in_password_recovery(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*EntranceLocators.ENTRANCE_PERSONAL_ACCOUNT)
        personal_account_button.click()

        password_recovery_button = driver.find_element(*EntranceLocators.PASSWORD_RECOVERY_BUTTON)
        password_recovery_button.click()

        password_recovery_entrance = driver.find_element(*EntranceLocators.PASSWORD_RECOVERY_ENTRANCE_TEXT)
        password_recovery_entrance.click()

        email_input = driver.find_element(*EntranceLocators.LOGIN_EMAIL)
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*EntranceLocators.LOGIN_PASSWORD)
        password_input.send_keys(fake.password())

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        entrance_button.click()
        assert driver.current_url == settings.URL + '/login'