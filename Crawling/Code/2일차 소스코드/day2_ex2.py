# day1_ex2.py의 파일에 있는 내용과 동일

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

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

soup = BeautifulSoup(driver.page_source, "html.parser")

# 웹사이트 닫기
time.sleep(5)
driver.close()

title = soup.find("div", class_="srchResultListW").find_all("p", class_="title")
# for i in title:
#     print(i.get_text().strip())

f_name = "c:/py_temp/riss.txt"

temp = sys.stdout

with open(f_name, "a", encoding="UTF-8") as file:
    sys.stdout = file

    for i in title:
        print(i.get_text().strip())

sys.stdout = temp

print("%s에 저장 성공!" % (f_name))
