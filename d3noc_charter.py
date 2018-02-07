from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("C:\Users\jdas\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
driver.get("https://www.goibibo.com/")
driver.maximize_window()

#input Src detail
inputSrc = driver.find_element_by_xpath('//input[@class="form-control inputTxtLarge inputSrc"]')
inputSrc.click()
inputSrc.clear()
inputSrc.send_keys('Pune')

#input Dest detail

inputDest = driver.find_element_by_xpath('//input[@class="form-control inputTxtLarge inputDest"]')
inputDest.click()
inputDest.clear()
inputDest.send_keys('ccu')

#Departed date
driver.find_element_by_xpath('//*[@id="searchWidgetCommon"]/div/div[3]/div[1]/div[1]/div/input').click()
reqMonth = 'February 2018'
button = '//span[@role="button" and @class="DayPicker-NavButton DayPicker-NavButton--next"]'

for d in range(12):
    try:
        driver.find_element_by_xpath('//div[contains(text(),"February 2018")]')

    except:
        driver.find_element_by_xpath(button).click()

driver.find_element_by_xpath("//div[@class='DayPicker-Day' and @aria-label='Sun Feb 25 2018']").click()

#search button
driver.find_element_by_xpath("//button[@class='width100 button orange xlarge']").click()