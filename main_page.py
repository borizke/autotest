#
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):




    def __init__(self, driver_g):
        self.driver_g = driver_g
        super().__init__(driver_g)

     # locators
    catalogi = "//*[@id='my-menu']/li[3]/a"
    shini_i_diski = "/html/body/div[2]/section/div/div/article/table/tbody/tr[4]/td[1]/a/img"


    #getters

    def get_select_catalogi(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalogi)))

    def get_shini_i_diski(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.shini_i_diski)))


    # Actions
    def click_select_catalogi(self):
        self.get_select_catalogi().click()
        print("Click catalogi")

    def click_shini_i_diski(self):
        self.get_shini_i_diski().click()
        print("Click shini i diski")


     # Methods

    def select_menu(self):

        self.get_current_url()
        self.click_select_catalogi()
        self.click_shini_i_diski()

