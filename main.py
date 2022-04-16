from pages.AmazonPage import AmazonPage
from pages.EbayPage import EbayPage
from pages.jomashop import jomashop
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver.v2 as uc
import random
import time

def setup (browser):
    if browser.lower() == "chrome":
        # options = Options()
        # options.add_argument("user-data-dir=C:\\Users\\Hoannt\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
        # driver = webdriver.Chrome(executable_path= "./resources/chromedriver.exe",  chrome_options=options)
        options = uc.ChromeOptions()

        # setting profile
        options.user_data_dir = "c:\\temp\\profile"

        # another way to set profile is the below (which takes precedence if both variants are used
        options.add_argument('--user-data-dir=c:\\temp\\profile2')

        # just some options passing in to skip annoying popups
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        driver = uc.Chrome(options=options, version_main=100)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path="./resources/geckodriver.exe")
    else:
        raise Exception("{} Browser is not supported".format(browser))

    #Implicit wait 
    driver.implicitly_wait(3)
    #driver.maximize_windows()
    return driver  

def teardown(driver):
    driver.quit()

def sort_combined_result(results):
    results.sort(key=getPrice)
    return results

def getPrice(list_content):
    #return price 
    return list_content[2]


if __name__ == "__main__":
    product = ["iphone", "macbook", "pussy", "dell", "nike", "puma","Mesh Chair", "T-shirt", "adidas", "bag","shock"]
    driver = setup("chrome")
    while True:
        # c = random.choice(product)
        # amazon_page = AmazonPage(driver)
        # amazon_page.load_page()
        # #need to change currency to MYR since amazon price in USD. 

        # amazon_page.search_item(c)
        # # amazon_page.scroll_page(c)
        # amazon_page.find_link(c)

    #get the list of the result that have been verified is iphone11 related
        # amazon_results = amazon_page.get_searchresult()

    # ebay_page = EbayPage(driver)
    # ebay_page.load_page()
    # ebay_page.search_item(random.choice(product))
    # #get the list of the result that have been verified is iphone11 related
    # ebay_results = ebay_page.get_searchresult()
    
    # all_results = amazon_results + ebay_results
    # sorted_results = sort_combined_result(all_results)
    # #use for debugging - see the price is sorted ascending order
    # for item in sorted_results:
    #     print(item[2])
    # for item in sorted_results:
    #     print(item)
        joma_shop = jomashop(driver)
        joma_shop.load_page()
        joma_shop.view_product_from_category()
        
    teardown(driver)

