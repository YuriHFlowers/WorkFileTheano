from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()

url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=2&orderBy=relevance'

options.add_argument('--start-maximized')
options.add_argument('--disable-infobars')
path = ("C:/webdrivers/chromedriver.exe")
s = Service(path)
driver = webdriver.Chrome(options=options,service=s)
driver.implicitly_wait(30)
driver.get(url)

print(driver.current_url)

keep_browsing = driver.find_element(By.ID,'uc-btn-accept-banner')
keep_browsing.click()
