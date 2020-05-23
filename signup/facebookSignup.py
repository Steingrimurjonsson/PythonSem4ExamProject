from selenium import webdriver
from time import sleep
from random import randint
from selenium.common.exceptions import NoSuchElementException
import re
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from captcha_solver import CaptchaSolver


#THIS ASSUMES THAT YOU HAVE MADE A GMAIL BEFOREHAND

class FacebookSignUpBot():
    def __init__(self, firstname, lastname, email, password):

        def slowTyping(element, text):
            for character in text:
                element.send_keys(character)
                sleep(0.2)

        option = Options()
        ua = UserAgent()
        userAgent = ua.random
        print(userAgent)
        option.add_argument(f'user-agent={userAgent}')
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(options=option, executable_path='chromedriver.exe')
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024, 768)
        self.driver.get('https://www.facebook.com/reg/')
        sleep(2)
        # Inputs firstname
        fname = self.driver.find_element_by_xpath(
            '//*[@id="u_0_p"]')
        slowTyping(fname, firstname)
        sleep(1)

        # Inputs lastname
        lname = self.driver.find_element_by_xpath(
            '//*[@id="u_0_r"]')
        slowTyping(lname, lastname)
        sleep(1)

        # Inputs email
        email1 = self.driver.find_element_by_xpath(
            '//*[@id="u_0_u"]')
        slowTyping(email1, email)
        sleep(2)
        # Re Inputs email
        email2 = self.driver.find_element_by_xpath(
            '//*[@id="u_0_x"]')
        slowTyping(email2, email)
        sleep(2)

        # Inputs password
        passw = self.driver.find_element_by_xpath(
            '//*[@id="u_0_z"]')
        slowTyping(passw, password)
        sleep(1)

        # click on year button
        self.driver.find_element_by_xpath(
            '//*[@id="year"]').click()
        sleep(randint(3, 6))
        # click on year 1994 button
        self.driver.find_element_by_xpath(
            '//*[@id="year"]/option[28]').click()
        sleep(randint(3, 6))

        # click on ratio button
        self.driver.find_element_by_xpath(
            '//*[@id="u_0_12"]/span[2]/label').click()
        sleep(randint(5, 6))

        # click on sign up
        self.driver.find_element_by_xpath(
            '//*[@id="u_0_16"]').click()
        sleep(randint(4, 6))

        print('kept going')
        sleep(20)

        # click on request review
        self.driver.find_element_by_xpath(
            '//*[@id="checkpointSubmitButton"]').click()
        sleep(randint(5, 6))
        # click on request review
        self.driver.find_element_by_xpath(
            '//*[@id="recaptcha-anchor"]/div[1]').click()
        sleep(10)
        # click on request review
        self.driver.find_element_by_xpath(
            '//*[@id="checkpointSubmitButton"]').click()
        sleep(randint(5, 6))


        image = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/article/section/section[2]/div/img').screenshot_as_png

        solver = CaptchaSolver('browser')
        raw_data = open(image, 'rb').read()
        print(solver.solve_captcha(raw_data))

        #Opens Gmail and finds the last email with verification code
        self.driver2 = webdriver.Chrome('chromedriver.exe')
        self.driver2.set_window_position(500, 0)
        self.driver2.set_window_size(1024, 768)
        self.driver2.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        sleep(2)

        # Inputs email on gmail
        self.driver2.find_element_by_xpath(
            '//*[@id="identifierId"]').send_keys(
            email)
        sleep(1)

        # Clicks next
        self.driver2.find_element_by_xpath(
            '//*[@id="identifierNext"]/span/span').click()
        sleep(randint(3, 6))

        # Inputs email password
        self.driver2.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(
            password)
        sleep(1)

        # Clicks next
        self.driver2.find_element_by_xpath(
            '//*[@id="passwordNext"]/span/span').click()
        sleep(randint(3, 6))

        # Clicks on the safety verify button
        try:
            self.driver2.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/span/span').click()
            sleep(randint(3, 6))
        except NoSuchElementException:
            pass

        #TODO MAKE IF POP UP FOR VERIFY AND HANGOUT POPUP(NEED POP UP XPATH)

        # Clicks next
        #self.driver2.find_element_by_xpath(
         #   '//*[@id=":3"]').click()
        # sleep(randint(3, 6))

        # Gets the code string value
        preEmailCode = self.driver2.find_element_by_xpath(
            '//*[@id=":2y"]/span').text
        sleep(randint(3, 6))
        emailCode = int(re.search(r'\d+', preEmailCode).group())

        # Inputs the validation code
        self.driver.find_element_by_xpath(
            '//*[@id="code_in_cliff"]').send_keys(
            emailCode)
        sleep(3)

        # Clicks continue
        self.driver.find_element_by_xpath(
            '//*[@id="u_1g_j"]').click()
        sleep(randint(3, 6))

        #NOW THE FACEBOOK ACCOUNT IS CREATED AND IS LOGGED IN.

def main():
    print('done')
    # FacebookSignUpBot(fn, ln, gmail, pwSignup)

if __name__ == '__main__':
    main()
