from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class Login_page(Base):

    url = 'http://zip69.ru/'


    def __init__(self, driver_g):
        self.driver_g = driver_g
        super().__init__(driver_g)

     # locators
    cabinet = "//a[@id='logInModal']"
    user_name = "//input[@id='login_modal']"
    password = "//input[@id='pass_modal']"
    button_login = "//input[@id='go_modal']"
    main_word = "/html/body/div[2]/section/div/div/article/div/article/div[2]/div[1]"

    #getters


    def get_cabinet(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cabinet)))

    def get_user_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions

    def click_cabinet(self):
        self.get_cabinet().click()
        print("Click cabinet")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")



    # Methods

    def autorization(self):
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        self.click_cabinet()
        self.input_user_name("testovich_2023@inbox.ru")
        self.input_password("finalexam2023")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Подбор по автомобилю")









