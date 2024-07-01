from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

INTERNET_PROVIDER = ""
PROMISED_DOWN = 100
PROMISED_UP = 110
CHROME_DRIVER_PATH = r"C:\Development\chromedriver.exe"
TWITTER_EMAIL = "kenmuiruri07@gmail.com"
TWITTER_PASSWORD = "(Muiruri07)"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                      'div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(100)
        down_internet_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/'
                                                                 'div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                                                                 '/div[1]/div/div[2]/span')
        self.down = float(down_internet_speed.text)
        print(self.down)
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                      'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(up_speed.text)
        print(self.up)

    def tweet_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(10)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                      'div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label')

        username.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]'
                                                         '/div/div/div[2]/div[2]/div/div/div/button[2]')
        time.sleep(1)
        next_button.click()
        time.sleep(3)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                                           'div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div'
                                                           '/button/div')
        log_in_button.click()
        time.sleep(5)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div'
                                                         '/div[1]/div[3]/a/div/svg/g/path')
        post_button.click()
        time.sleep(10)
        content = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                     'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/'
                                                     'div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/'
                                                     'div/div/div/div/div')
        content.send_keys(f"Hey, {INTERNET_PROVIDER}, why is my internet speed {self.up}up/{self.down}down when I pay "
                          f"for {PROMISED_UP}up/{PROMISED_DOWN}down?")
        time.sleep(5)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                          'div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                          'div[2]/div[2]/div/div/div/button/div/span')
        tweet_button.click()
        time.sleep(7)
        self.driver.quit()
