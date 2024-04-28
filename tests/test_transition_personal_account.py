import settings
from locators import UserLocators

class TestTransitionPersonalAccount:
    def test_personal_account(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()
        assert driver.current_url == settings.URL + '/login'