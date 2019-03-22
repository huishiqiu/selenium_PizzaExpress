from selenium import webdriver
import time
class Login_test():

    #打开webdriver Chrome 版本23.0
    driver = webdriver.Chrome('webdriver/chromedriver')
    # driver.get('http://www.google.com')
    # driver.get('http://localhost:9999/#/login')
    # time.sleep(3)
    # driver.find_element_by_id("code").click()
    # time.sleep(5)
    # driver.find_element_by_id("verifyCode").click()
    # time.sleep(3)
    def test1_0(self):
        self.driver.get('http://localhost:9999/#/login')
        time.sleep(2)
        #根据网页元素ID来访问，此外还有xpath，value等
        self.driver.find_element_by_id("code").click()
        time.sleep(2)
        self.driver.find_element_by_id("verifyCode").click()
        time.sleep(2)
    # driver.close()

if __name__ == '__main__':
    logintest=Login_test()
    logintest.test1_0()
