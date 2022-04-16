from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

class jomashop():
    BASE_URL = "https://www.jomashop.com/"
    CATEGORY_PRODUCT = (By.XPATH,'//*[@id="maincontent"]/div[2]/div/div/div/div/div[2]/div[1]/div[1]/a')

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get(self.BASE_URL)
    def view_product_from_category(self):
        self.driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div/div/div/div/div[2]/div['+str(random.randrange(1,6,1))+']/div[1]/a').click()
        time.sleep(5)
        z = 1000
        for timer in range(0,10):
            self.driver.execute_script("window.scrollTo(0, "+str(z)+")")
            time.sleep(random.randrange(1,5,1))
            z += 100
        for i in range(0,20):
            m = 1000
            for timer in range(0,10):
                self.driver.execute_script("window.scrollTo(0, "+str(m)+")")
                time.sleep(random.randrange(1,5,1))
                m += 100
            prod = self.driver.find_element(By.XPATH,'//*[@id="product-list-wrapper"]/ul/li['+str(random.randrange(1,20,1))+']/div/div[2]/h2/a')
            self.driver.execute_script("arguments[0].scrollIntoView();", prod)
            # ActionChains(self.driver).move_to_element(prod).perform()
            time.sleep(5)
            prod.click()
            y = 100
            for timer in range(0,20):
                self.driver.execute_script("window.scrollTo(0, "+str(y)+")")
                time.sleep(random.randrange(1,5,1))
                y += 100
            self.driver.back()
            time.sleep(3)
    def view_sale(self):
        self.driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div/div/div/div/div[3]/div[1]/div[1]/a')