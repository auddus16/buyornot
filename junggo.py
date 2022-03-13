from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException

url = 'https://m.bunjang.co.kr/search/products?q=%EC%95%84%EC%9D%B4%ED%8F%B0'
# openApi페이지 클릭