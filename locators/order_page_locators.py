from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    LAST_NAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_FIELD = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    STATION_1 = By.XPATH, "//li[@class='select-search__row' and @data-index='0' and @data-value='1']"
    STATION_2 = By.XPATH, "//li[@class='select-search__row' and @data-index='3' and @data-value='4']"
    PHONE_NUMBER_FIELD = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"
    DATE_FIELD = By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"
    DATE_1 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--010']"
    DATE_2 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--013']"
    RENT_TIME_FIELD = By.XPATH, "//div[text()='* Срок аренды']"
    TIME_1 = By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"
    TIME_2 = By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"
    BLACK_COLOR = By.ID, "black"
    GREY_COLOR = By.ID, "grey"
    COMMENTS = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    YES_BUTTON = By.XPATH, "//button[text()='Да']"
    ORDER_SUCCESS_WINDOW = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"