from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.chrome.options import Options

class FacebookBot():
    def __init__(self, username, password):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(options=option,  executable_path='chromedriver.exe')
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024, 768)
        self.driver.get('https://www.facebook.com/')
        sleep(randint(2, 5))

        self.driver.find_element_by_xpath(
            '//*[@id="email"]').send_keys(username)
        self.driver.find_element_by_xpath(
            '//*[@id="pass"]').send_keys(password)

        # click signin
        self.driver.find_element_by_xpath(
            '//*[@id="u_0_b"]').click()
        sleep(randint(4, 6))

    def post_facebook(self, msg):
        fbPost = self.driver.find_element_by_xpath("//*[@name='xhpc_message']")
        sleep(randint(4, 6))
        fbPost.send_keys(msg)
        sleep(randint(4, 6))
        self.driver.find_element_by_xpath("//button[contains(.,'Post')]").click()
        sleep(10)
        print("FB post done")
def main():
    print('done')

if __name__ == '__main__':
    main()
