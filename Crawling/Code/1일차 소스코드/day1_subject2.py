# 필수과제
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

# .txt 파일에 저장할 파일 경로
file_path = "c:/py_temp/output.txt"

driver = webdriver.Chrome()
driver.set_window_size(1300, 768)  # 가로 1024px, 세로 768px로 설정
# 웹사이트 오픈하고 닫기
driver.get("https://korean.visitkorea.or.kr")

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

time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn01").click()

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(driver.page_source, "html.parser")

# class가 "tit"인 모든 div element 가져오기
div_elements = soup.find_all("div", class_="tit")

texts = []

for idx, div in enumerate(div_elements, start=1):
    if idx > 10:
        break
    text = div.get_text(strip=True)
    texts.append(text)
print(texts)

temp = sys.stdout

with open(file_path, "a", encoding="UTF-8") as file:
    sys.stdout = file

    for text in texts:
        print(text)

sys.stdout = temp

time.sleep(10)
driver.close()
