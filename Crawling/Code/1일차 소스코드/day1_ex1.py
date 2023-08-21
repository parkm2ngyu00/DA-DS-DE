from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 웹사이트 오픈하고 닫기
driver.get("https://www.riss.kr")

main = driver.window_handles
for handle in main:
    if handle != main[0]:
        driver.switch_to.window(handle)
        driver.close()

driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
driver.find_element(By.ID, "query").send_keys("빅데이터" + "\n")

time.sleep(2)
driver.find_element(By.LINK_TEXT, "학위논문").click()


time.sleep(5)
driver.close()
