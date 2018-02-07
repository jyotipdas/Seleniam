from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("C:\Users\jdas\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(30)
driver.maximize_window()
#input source location
inputSrc=driver.find_element_by_xpath('//*[@id="hp-widget__sfrom"]')
inputSrc.click()
inputSrc.clear()
time.sleep(5)
inputSrc.send_keys('pune')

#input destination location

inputDest = driver.find_element_by_xpath('//*[@id="hp-widget__sTo"]')
inputDest.click()
inputDest.clear()
time.sleep(5)
inputDest.send_keys('ccu')

#input date
driver.find_element_by_id("hp-widget__depart").click()

for d in range(12):
    try:
        driver.find_element_by_xpath("//div[contains(@class,'ui-datepicker-title')]/span[contains(text(),'February') and contains(@class,'ui-datepicker-month')]").text
        driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']//td[@data-year='2018' and @data-month='1']//*[contains(text(),'25')]").click()
        break
    except:
        driver.find_element_by_xpath("//a[@title='Next' and contains(@class,'ui-datepicker-next ui-corner-all')]/span[@class='ui-icon ui-icon-circle-triangle-e']").click()


#press search button

driver.find_element_by_xpath('//*[@id="searchBtn"]').click()

time.sleep(30)

price1 = driver.find_element_by_xpath("//*[@id='content']/div/div[5]/div[5]/div[2]/div[5]/div/div[2]/div[6]/p["
                                      "1]/span[2]").text
price2 = driver.find_element_by_xpath("//*[@id='content']/div/div[5]/div[5]/div[2]/div[6]/div/div[2]/div[6]/p["
                                      "1]/span[2]").text

print "Pune to Kolkata for 25th Feb is {} and {}".format(price1,price2)
driver.quit()