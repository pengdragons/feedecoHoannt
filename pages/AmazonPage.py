"""
This class contain Amazon main page object 
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AmazonPage():
    #all the element locators used in Amazon Page
    WEBSITE_NAME = "Amazon"
    BASE_URL = "https://www.amazon.com/"
    SEARCH_TEXTBOX_LOCATOR = (By.ID,"twotabsearchtextbox")
    SEARCH_BUTTON_LOCATOR = (By.ID,"nav-search-submit-button")
    SEARCH_RESULT_DIV_LOCATOR = (By.XPATH,"*//div[@data-component-type='s-search-result']")
    PRODUCT_NAME = (By.XPATH,"*//a[@class='a-link-normal a-text-normal']/span[@class='a-size-medium a-color-base a-text-normal']")
    PRODUCT_PRICE_WHOLE = (By.XPATH,"*//span[@class='a-price-whole']")
    PRODUCT_PRICE_FRACTION = (By.XPATH,"*//span[@class='a-price-fraction']")
    PRODUCT_LINK = (By.XPATH,"*//a[@class='a-link-normal s-no-outline']")
    CURRENCY_DROPDOWN = (By.ID,"icp-currency-dropdown-selected-item-prompt")
    CURRENCY_LINK = (By.ID,"icp-nav-flyout")
    MYR_OPTION = (By.XPATH,'//*[@id="USD"]')
    SAVE_BUTTON = (By.CLASS_NAME,"a-button-input")


    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get(self.BASE_URL)
        
    def search_item(self,item):
        self.driver.find_element(*self.SEARCH_TEXTBOX_LOCATOR).send_keys(item)
        self.driver.find_element(*self.SEARCH_BUTTON_LOCATOR).click()
    def scroll_page(self,item):
        y = 500
        for timer in range(0,20):
            i = 1
            self.driver.execute_script("window.scrollTo(0, "+str(y)+")")
            elems = self.driver.find_elements(By.XPATH,"//a[@href]")
            for elem in elems:
                if str(elem.get_attribute("href")).lower().find(item) != -1:
                    elem.click()
                    z = 1000
                    for timer in range(0,10):
                        self.driver.execute_script("window.scrollTo(0, "+str(z)+")")
                        time.sleep(1)
                        z += 100
                    self.driver.back()
            i += 1
            y += 500  
            time.sleep(1)
    def find_link(self,item):
        elems = self.driver.find_element(*self.PRODUCT_LINK)
        # for elem in elems:
        #     print(elem)
        # link = elems.get_attribute("href")
        # print(link)
        print(elems)
    def get_searchresult(self):
        validated_results = []  
        #get the list search result webelements
        search_result_elems = self.driver.find_elements(*self.SEARCH_RESULT_DIV_LOCATOR)

        #skip whole function if no webelement present in the list 
        if search_result_elems == None:
            return validated_results

        #iterate in each web element to get product name, product price and product link 
        for result_elem in search_result_elems: 
            product_name = result_elem.find_element(*self.PRODUCT_NAME).text  

            #validate the product name is Iphone 11 related. If not skipped inspecting the webelement
            if "iphone 11" not in product_name.lower():
                continue

            try :
                #need to replce "," with "" in the whole price or error will be thrown when conversting to float
                product_price = result_elem.find_element(*self.PRODUCT_PRICE_WHOLE).text.replace(",","") +"."+ result_elem.find_element(*self.PRODUCT_PRICE_FRACTION).text
                #print(product_price)    
            except Exception as e:
                #if no element for price in DOM, just put 0. no elements occurs due to out of stock in the website
                product_price = 0
                #print(product_price,e.args)

            product_link = result_elem.find_element(*self.PRODUCT_LINK).get_attribute("href")
            validated_results.append([self.WEBSITE_NAME,product_name,float(product_price),product_link])
            
        return validated_results

    #amazon website did not set the currency according to country, so need to set for correct comparision with the Ebay prices.
    def change_currency_to_myr(self):
        self.driver.find_element(*self.CURRENCY_LINK).click()
        self.driver.find_element(*self.CURRENCY_DROPDOWN).click()
        self.driver.find_element(*self.MYR_OPTION).click()
        self.driver.find_element(*self.SAVE_BUTTON).click()



