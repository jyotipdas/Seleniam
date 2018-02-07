from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
#driver = webdriver.Chrome(executable_path="C:\Users\jdas\Downloads\chromedriver_win32\chromedriver.exe")
#driver.get("https://www.flipkart.com/")
#print driver.title
#assert "Online Shopping" in driver.title
#driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("moto")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()

class DataFlipkart(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome("C:\Users\jdas\Downloads\chromedriver_win32\chromedriver.exe")

    def test_moto(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        assert "Online Shopping" in driver.title
        driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        elem = driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys('iphone')
        elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source()
        model = driver.find_element_by_xpath("//div[@class='col-7-12']/div[@class='_3wU53n']").text
        price = driver.find_element_by_xpath("//div[@class='col-5-12 _2o7WAb']/div[@class='_6BWGkk']/div["
                                             "@class='_1uv9Cb']/div[@class='_1UoZlX "
                                             "_2rQ-NK']").text
        print '{}:{}'.format(model,price)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()