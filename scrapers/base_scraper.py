from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys, subprocess, traceback
import MySQLdb as mdb
sys.path.append("..")
from settings import *

class BaseScraper(object):
    def __init__(self):
        self.base_dir = base_dir
        self.mysql_connect()
        try: 
            self.main()
        except: 
            traceback.print_exc()
        self.mysql_close()
        self.clear_system()

    def get_chromedriver(self, url, proxy):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server:{}'.format(proxy))
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(url)

    def get_geckodriver(self, url, proxy, mode):
        if mode == True:
            profile = webdriver.FirefoxProfile()
            profile.set_preference('network.proxy.type', 1)
            profile.set_preference('network.proxy.http', proxy)
            profile.set_preference('network.proxy.http_port', 3128)
            profile.set_preference('network.proxy.ssl', proxy)
            profile.set_preference('network.proxy.ssl_port', 3128)
            profile.update_preferences()
            self.driver = webdriver.Firefox(firefox_profile=profile)
        else:
            self.driver = webdriver.Firefox()

        self.driver.get(url)

    def wait_visibility(self, driver, element, delay):
        return WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element)))

    def clear_system(self):
        subprocess.call(['sudo pkill geckodriver ; sudo pkill firefox ; sudo pkill chromium-browse'], shell=True)
        subprocess.call(['sudo pkill chromedriver'], shell=True)

    def mysql_connect(self):
        self.conn = mdb.connect(
            user = user,
            passwd = passwd,
            db = db,
            host = host
        )
        self.cur = self.conn.cursor()

    def mysql_close(self):
        self.conn.close()
