import time
from selenium import webdriver

class SendSMS():
    def __init__(self):
        self.url = 'http://192.168.0.1/index.html#login'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome('D:\\chrome\\chromedriver.exe')
        self.driver.get(self.url)
        time.sleep(0.1)
        self.login()

    def login(self):
        # admin text filed
        admin = self.driver.find_element_by_id("txtUname")
        admin.clear()
        admin.send_keys("admin")
        # passwd
        passwd = self.driver.find_element_by_id("txtPwd")
        passwd.clear()
        passwd.send_keys("admin")
        # login
        login = self.driver.find_element_by_id("btnLogin")
        login.click()

    def gotoSMS(self):
        self.driver.get('http://192.168.0.1/#sms')
        time.sleep(1)
        self.driver.find_element_by_id("smslist-new-sms").click()
        time.sleep(1)

    def SendSMS(self, text, nums):
        final_nums = self.Refactor(nums)
        for num in final_nums:
            self.SendMessage(text, num)
        self.driver.close()


    def SendMessage(self, text, nums):
        self.gotoSMS()
        # set the numbers
        numfield = self.driver.find_element_by_id("chosen-search-field-input")
        numfield.clear()
        numfield.send_keys(nums)
        # set the text
        textfield = self.driver.find_element_by_id("chat-input")
        textfield.clear()
        textfield.send_keys(text)
        self.driver.find_element_by_id("btn-send").click()
        time.sleep(5)
        print(nums + " : sent !")

    def Refactor(self, nums):
        final_nums = []
        numbers = ""
        counter = 1
        for num in nums:
            numbers = numbers + num + ";"
            if counter % 5 == 0 or counter == len(nums):
                final_nums.append(numbers)
                numbers = ""
            counter += 1
        return final_nums