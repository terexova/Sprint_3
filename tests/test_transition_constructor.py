import settings
from locators import UserLocators

class TestTransitionConstructor:
    def test_transition_constructor(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        constructor_button = driver.find_element(*UserLocators.ENTER_CONSTRUCTOR_BUTTON)
        constructor_button.click()
        assert driver.current_url == settings.URL

    def test_transition_logo_Stellar_Burger(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        logo_Stellar_Burger_button = driver.find_element(*UserLocators.ENTER_LOGO_STELLAR_BURGER_BUTTON)
        logo_Stellar_Burger_button.click()
        assert driver.current_url == settings.URL