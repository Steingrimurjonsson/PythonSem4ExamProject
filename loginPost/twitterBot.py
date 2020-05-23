from selenium import webdriver
from time import sleep
from random import randint
from selenium.common.exceptions import NoSuchElementException

class TwitterBot():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024, 768)
        self.driver.get('https://twitter.com/')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input').send_keys(
            username)
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input').send_keys(
            password)
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div/div/span/span').click()
        sleep(randint(3, 6))

    def tweet(self, msg):
        # Clicks on the safety verify button
        try:
            self.driver.find_element_by_xpath(
                "//div[@role = 'button']/div/span").click()
            sleep(1)
        except NoSuchElementException:
            pass

        # click blue 'Tweet' button
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div/div[3]/a').click()
        sleep(randint(2, 3))
        # Enter tweet
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/span').send_keys(
            msg)
        sleep(randint(3, 5))
        # Tweet it!
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
        sleep(2)

def main():
    print('done')

if __name__ == '__main__':
    main()
