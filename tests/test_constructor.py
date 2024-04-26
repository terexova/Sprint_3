import settings
from locators import ConstructorLocatorsSauce

class TestConstructorSauce:
    def test_constructor(self, driver):
        driver.get(settings.URL)

        nachinki = driver.find_element(*ConstructorLocatorsSauce.NACHINKI)
        assert nachinki
        nachinki.click()

        bulki = driver.find_element(*ConstructorLocatorsSauce.BULKI)
        assert bulki
        bulki.click()

        sauce = driver.find_element(*ConstructorLocatorsSauce.SAUCE)
        assert sauce
        sauce.click()


