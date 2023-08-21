from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time
import os

query_txt = input("1. 크롤링할 이미지의 키워드는?: ")
cnt = int(input("2. 크롤링 할 건수는?: "))

now = "c:/py_temp/" + time.strftime("%Y%m%d_%H%M%S") + "-" + query_txt
os.makedirs(now)
os.chdir(now)

driver = webdriver.Chrome()
base_link = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
driver.get(base_link + query_txt)

for i in range(2):
    time.sleep(3)
    driver.find_element(By.XPATH, "//body").send_keys(Keys.END)


soup = BeautifulSoup(driver.page_source, "html.parser")
img_src = []

for i in soup.find_all("img", class_="_image _listImage"):
    img_src.append(i["src"])

for idx, save_img in enumerate(img_src, start=1):
    urllib.request.urlretrieve(save_img, str(idx) + ".jpg")
    if idx == cnt:
        break

print("%d개의 이미지가 '%s'에 저장되었습니다." % (cnt, now))

driver.close()
