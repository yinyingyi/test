from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.get('http://sahitest.com/demo/label.htm')
        # input1 = self.driver.find_element_by_tag_name('input')[3]
        # input2 = self.driver.find_element_by_tag_name('input')[4]
        # action = ActionChains(self.driver)
        # input1.click()
        # action.send_keys('username').perform()
        # action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        # action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
        # action.key_down(Keys.CONTROL,input2).send_keys('v').key_up(Keys.CONTROL)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_case_click(self):
        pass

    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element(By.ID,"s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(10)

    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element_by_class_name("drag")
        drop_element = self.driver.find_element_by_xpath("//body/div[2]")
        action = ActionChains(self.driver)
        #方法一
        # action.drag_and_drop(drag_element,drop_element).perform()
        #方法二
        # action.click_and_hold(drag_element).release(drop_element).perform()
        #方法三
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        def wait(x):    #自定义函数，一定要设置一个参数
            return len(self.driver.find_elements(By.XPATH,'//body/div')) >= 1
        WebDriverWait(self.driver,5).until(wait)

    def test_sendkeys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        action = ActionChains(self.driver)
        ele.click()
        action.send_keys('username')
        action.send_keys(Keys.SPACE)
        action.send_keys('tom')
        action.send_keys(Keys.BACK_SPACE).perform()