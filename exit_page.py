from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class Exit_page(Base):




    def __init__(self, driver_g):
        self.driver_g = driver_g
        super().__init__(driver_g)

     # locators
    user_login = "//*[@id='logInModal']/span"
    confirm_exit = "//*[@id='modalFormLogin']/div/div/div[2]/a"

    #getters

    def get_user_login(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))

    def get_confirm_exit(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_exit)))


    # Actions
    def click_user_login(self):
        self.get_user_login().click()
        print("Click User")

    def click_confirm_exit(self):
        self.get_confirm_exit().click()
        print("Click confirm exit account")


     # Methods

    def exit_account(self):


        self.click_user_login()
        self.click_confirm_exit()











