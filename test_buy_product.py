import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.catalogi_page import Catalogi_page
from pages.exit_page import Exit_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.order_page import Order_page
from pages.verify_page import Verify_page


# @pytest.mark.run(order=3)
def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service("Users/borizke/PycharmProjects/resource/chromedriver")
    driver_g = webdriver.Chrome(options=options, service=g)

    print("start test 1")

    login = Login_page(driver_g)
    login.autorization()

    mp = Main_page(driver_g)
    mp.select_menu()

    cp = Catalogi_page(driver_g)
    cp.click_checkbox()

    op = Order_page(driver_g)
    op.confirmation()

    ep = Exit_page(driver_g)
    ep.exit_account()

    vp = Verify_page(driver_g)
    vp.verify()













