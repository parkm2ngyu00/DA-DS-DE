from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, sys

word = input("검색어를 입력해주세요: ")
cnt = int(input("검색 건수를 입력해주세요: "))

driver = webdriver.Chrome()
driver.get("https://section.blog.naver.com/")

time.sleep(2)
driver.find_element(By.CLASS_NAME, "textbox").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "textbox").send_keys(word + "\n")
time.sleep(2)

page_cnt = math.ceil(cnt / 7)
count = 1

f_name = "c:/py_temp/blog.txt"
temp = sys.stdout

for x in range(1, page_cnt + 1):
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    titles = soup.find("div", class_="area_list_search").find_all(
        "span", class_="title"
    )

    for title in titles:
        if count > cnt:
            break
        with open(f_name, "a", encoding="UTF-8") as file:
            sys.stdout = file
            print("%d 번째 게시물 제목 : %s" % (count, title.get_text().strip()))
        count += 1

    x += 1
    try:
        driver.find_element(By.LINK_TEXT, "%s" % (x)).click()
    except:
        driver.find_element(By.CLASS_NAME, "button_next").click()

sys.stdout = temp
print("%s에 저장되었습니다" % (f_name))


time.sleep(3)
driver.close()
