import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from helpers.urls import Urls

class HomePage(BasePage):

    @allure.step('Клик на вопрос')
    def click_on_question(self, question_number):
        locator = HomePageLocators.QUESTION.format(question_number)
        self.click_to_element(locator)

    @allure.step('Получение ответа')
    def get_answer(self, question_number):
        locator = HomePageLocators.ANSWER.format(question_number)
        return self.get_text(locator)

    @allure.step('Клик на лого Яндекса в шапке')
    def click_on_yandex_logo(self):
        self.click_to_element(HomePageLocators.YANDEX_LOGO)

    @allure.step('Клик на лого Самоката в шапке')
    def click_on_samokat_logo(self):
        self.click_to_element(HomePageLocators.SAMOKAT_LOGO)


    @allure.step("Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»")
    def open_home_page(self):
        self.open_url(Urls.HOME_PAGE)
        self.wait_element_visibility_of_element_located(HomePageLocators.COOKIES_BUTTON)
        assert self.get_current_page_url() == Urls.HOME_PAGE