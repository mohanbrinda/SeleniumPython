from selenium import webdriver
import time
from selenium.webdriver.common.keys import keys

driver = webdriver.Chrome("C:\Users\arvind\PycharmProjects\Selenium\Driver\chromedriver.exe")
driver = webdriver.Firefox()
driver = webdriver.Ie()
driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automobile")
driver.find_element_by_name("btnK").send_keys(keys.ENTER)
time.sleep(4)
driver.quit()


