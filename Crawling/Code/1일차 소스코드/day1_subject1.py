# 필수과제

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()

# 웹사이트 오픈하고 닫기
driver.get("https://korean.visitkorea.or.kr")

# time.sleep(2)
# driver.find_element(By.CLASS_NAME, 'btn_search').click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="placeHolder"]/a').click()

time.sleep(2)
driver.find_element(By.ID, "inp_search").click()

time.sleep(2)
driver.find_element(By.ID, "inp_search").send_keys("여름여행" + "\n")

time.sleep(2)
driver.find_element(By.CLASS_NAME, "option").click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="32"]/button').click()

time.sleep(5)
driver.close()
