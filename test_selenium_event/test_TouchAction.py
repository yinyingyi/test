from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options = option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_touchaction(self, action=None):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")

        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()
        #方法一
        action.scroll_from_element(ele,0,1000).perform()
    
