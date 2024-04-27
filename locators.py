from selenium.webdriver.common.by import By


class UserLocators:
    ENTER_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[p[text() = 'Личный Кабинет']]")
    ENTER_CONSTRUCTOR_BUTTON = (By.XPATH, "//a[p[text() = 'Конструктор']]")
    ENTER_LOGO_STELLAR_BURGER_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/div/a")

class LoginLocators:
    ENTER_REGISTRATION = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    LOGIN_NAME = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    LOGIN_EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    LOGIN_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    BUTTON_REGISTRATION = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    ENTRANCE_TEXT = (By.XPATH, "//h2[text() = 'Вход']")
    EXIT_TEXT = (By.XPATH, "//button[text() = 'Выход']")

class EntranceLocators:
    ENTRANCE_IN_ACCOUNT = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    LOGIN_EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    LOGIN_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    ENTRANCE_BUTTON = (By.XPATH, "//button[text() = 'Войти']")

    ENTRANCE_PERSONAL_ACCOUNT = (By.XPATH, "//a[p[text() = 'Личный Кабинет']]")
    ENTRANCE_REGISTRATION = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    ENTRANCE_TEXT = (By.XPATH, "//button[text() = 'Войти']")
    LOGIN_NAME = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    ENTRANCE_TEXT = (By.XPATH, "//a[text() = 'Войти']")

    ENTRANCE_IN_REGISTRATION = (By.XPATH, "//label[text() = 'Войти']/following-sibling::input")

    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']")
    PASSWORD_RECOVERY_ENTRANCE_TEXT = (By.XPATH, "//a[text() = 'Войти']")

class ConstructorLocatorsSauce:
    BREAD = (By.XPATH, "//div[./span[text() = 'Булки']]")
    SAUCE = (By.XPATH, "//div[./span[text() = 'Соусы']]")
    FILLING = (By.XPATH, "//div[./span[text() = 'Начинки']]")