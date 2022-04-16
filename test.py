from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://psychoticelites.com/")

assert "Psychotic" in driver.title

continue_link = driver.find_element_by_tag_name('a')
elem = driver.find_elements_by_xpath("//*[@href]")
#x = str(continue_link)
#print(continue_link)
print(elem)