from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.implicitly_wait(3)  #隐式等待，页面加载

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//li[@title="所有分类"]').click()    #选择所有li元素，且title="所有分类
        def wait(x):    #自定义函数，一定要有一个参数
            return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]')) >= 1
        WebDriverWait(self.driver,5).until(wait)    #显式等待，元素加载。wait不要写括号（传参），写了括号就是调用函数
        self.driver.find_element(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()