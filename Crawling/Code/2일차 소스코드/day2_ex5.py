from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller as ca
import time, os, requests

query_txt = input("검색 : ")
user_cnt = int(input("개수 : "))

now = "c:/py_temp/" + time.strftime("%Y%m%d_%H%M%S") + "-" + query_txt
os.makedirs(now)
os.chdir(now)

try:
    driver = webdriver.Chrome()
    driver.get("https://pixabay.com/images/search/" + query_txt)
except:
    pass

a = user_cnt // 100 + 1
for _ in range(a):
    for _ in range(6):
        time.sleep(3)
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
    if a > 1:
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[4]/div[2]/a'
        ).send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source, "html.parser")
a = soup.find_all("img")
img_src = []
for i in a:
    try:
        img_src.append(i["src"])
    except:
        continue

for idx, save_img in enumerate(img_src, start=1):
    # 이미지 URL이 "*.jpg"로 끝나는 경우에만 다운로드
    if save_img.lower().endswith(".jpg"):
        response = requests.get(save_img)
        if response.status_code == 200:
            # 이미지 파일 저장 경로
            file_path = os.path.join(now, str(idx) + ".jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)

    if idx == user_cnt:
        break

driver.close()
