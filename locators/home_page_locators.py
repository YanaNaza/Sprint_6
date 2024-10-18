from selenium.webdriver.common.by import By


class HomePageLocators:
    QUESTION = By.XPATH, "//div[@id = 'accordion__heading-{}']"
    ANSWER = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    LAST_QUESTION = By.XPATH, "(//div[contains(@id,'accordion__heading-')])[last()]"
    ORDER_BUTTON_HEADER = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    ORDER_BUTTON_PAGE = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    SAMOKAT_LOGO = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    DZEN_HOME_PAGE = 'https://dzen.ru/?yredirect=true'
    YANDEX_LOGO = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
    COOKIES_BUTTON = By.ID, "rcc-confirm-button"