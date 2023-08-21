from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import urllib
import pandas as pd
import time, os, math

print("=" * 80)
print("쿠팡 사이트의 식품 카테고리 Best Seller 상품 정보 추출하기")
print("=" * 80)

cnt = int(input("1. 크롤링 할 건수는 몇건입니까? "))
page_cnt = math.ceil(cnt / 60)

f_dir = input("2. 파일을 저장할 폴더명만 쓰세요(기본경로 : c:/py_temp/): ")
if f_dir == "":
    f_dir = "c:/py_temp/"

print("\n")

if cnt > 30:
    print("요청 건수가 많아서 시간이 제법 소요되오니 잠시만 기다려 주세요")
else:
    print("요청하신 데이터를 수집하고 있습니다.")

sec_name = "식품"
query_txt = "쿠팡"

n = time.localtime()
s1 = "%04d-%02d-%02d-%02d-%02d-%02d" % (
    n.tm_year,
    n.tm_mon,
    n.tm_mday,
    n.tm_hour,
    n.tm_min,
    n.tm_sec,
)

os.makedirs(f_dir + s1 + "-" + query_txt + "-" + sec_name)
os.chdir(f_dir + s1 + "-" + query_txt + "-" + sec_name)

ff_dir = f_dir + s1 + "-" + query_txt + "-" + sec_name
ff_name = (
    f_dir
    + s1
    + "-"
    + query_txt
    + "-"
    + sec_name
    + "\\"
    + s1
    + "-"
    + query_txt
    + "-"
    + sec_name
    + ".txt"
)
fc_name = (
    f_dir
    + s1
    + "-"
    + query_txt
    + "-"
    + sec_name
    + "\\"
    + s1
    + "-"
    + query_txt
    + "-"
    + sec_name
    + ".csv"
)
fx_name = (
    f_dir
    + s1
    + "-"
    + query_txt
    + "-"
    + sec_name
    + "\\"
    + s1
    + "-"
    + query_txt
    + "-"
    + sec_name
    + ".xls"
)

# 제품 이미지 저장용 폴더 생성
img_dir = ff_dir + "/images"
os.makedirs(img_dir)
os.chdir(img_dir)

s_time = time.time()

# 웹사이트 접속 후 해당 메뉴로 이동
driver = webdriver.Chrome()

query_url = "https://www.coupang.com"
driver.get(query_url)
time.sleep(5)

# Access Denied 메세지가 나오면 아래코드로 쿠키를 삭제
driver.delete_all_cookies()
time.sleep(2)

# 카테고리 -> 식품 버튼을 눌러 페이지를 엽니다
driver.find_element(By.XPATH, '//*[@id="header"]/div').click()
driver.find_element(By.XPATH, '//*[@id="gnbAnalytics"]/ul[1]/li[4]/a').click()

time.sleep(5)

# 내용 수집
print("\n")
print("===== 곧 수집된 결과를 출력합니다 =====")
print("\n")

ranking2 = []
title2 = []
p_price2 = []
discount2 = []
sat_count2 = []

img_src2 = []
file_no = 0
count = 1


def scroll_down(driver):
    driver.execute_script("window.scrollBy(0, 1100)")
    time.sleep(4)


for x in range(1, page_cnt + 1):
    # for cc in range(1, 7):
    #     scroll_down(driver)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    item_result = soup.find("ul", class_="baby-product-list").find_all("li")
    for li in item_result:
        if cnt < count:
            break
        # 제품 이미지 다운로드 하기
        try:
            photo = li.find("dt", class_="image").find("img")["src"]
        except:
            continue

        file_no += 1
        full_photo = "https:" + photo
        urllib.request.urlretrieve(full_photo, str(file_no) + ".jpg")
        time.sleep(0.5)
        # 제품 내용 추출하기
        f = open(ff_name, "a", encoding="UTF-8")
        f.write("-----------------------------------------------------" + "\n")
        print("-" * 70)

        ranking = count
        print("1.판매순위:", ranking)
        f.write("1.판매순위:" + str(ranking) + "\n")

        try:
            t = li.find("div", class_="name").get_text().replace("\n", "")
        except:
            title = "제품소개가 없습니다"
            print(title.replace("\n", ""))
            f.write("2. 제품소개:" + title + "\n")
        else:
            title = t.replace("\n", "").strip()
            print("2.제품소개:", title.replace("\n", "").strip())
            f.write("2.제품소개:" + title + "\n")

        try:
            p_price = li.find("strong", "price-value").get_text().replace("\n", "")
        except:
            p_price = "0"
            print("3.판매가격:", p_price.replace("\n", ""))
            f.write("3.판매가격:" + p_price + "\n")
        else:
            print("3.판매가격:", p_price.replace("\n", ""))
            f.write("3.판매가격:" + p_price + "\n")
        try:
            discount = (
                li.find("span", "discount-percentage").get_text().replace("\n", "")
            )
        except:
            discount = "0"
            print("4:할인률:", discount)
            f.write("4.할인율:" + discount + "\n")
        else:
            print("4:할인률:", discount)
            f.write("4.할인율:" + discount + "\n")
        try:
            sat_count_1 = li.find("span", "rating-total-count").get_text()
            sat_count_2 = sat_count_1.replace("(", "").replace(")", "")
        except:
            sat_count_2 = "0"
            print("5.상품평 수: ", sat_count_2)
            f.write("5.상품평 수:" + sat_count_2 + "\n")
        else:
            print("5.상품평 수:", sat_count_2)
            f.write("5.상품평 수:" + sat_count_2 + "\n")
        print("-" * 70)

        f.close()
        time.sleep(0.5)

        ranking2.append(ranking)
        title2.append(title.replace("\n", ""))

        p_price2.append(p_price.replace("\n", ""))
        discount2.append(discount)

        try:
            sat_count2.append(sat_count_2)
        except IndexError:
            sat_count2.append(0)
        count += 1

    x += 1
    try:
        driver.find_element(By.LINK_TEXT, "%s" % (x)).click()
    except:
        break

# csv, xls 형태로 저장하기
co_best_seller = pd.DataFrame()
co_best_seller["판매순위"] = ranking2
co_best_seller["제품소개"] = pd.Series(title2)
co_best_seller["제품판매가"] = pd.Series(p_price2)
co_best_seller["할인률"] = pd.Series(discount2)
co_best_seller["상품평수"] = pd.Series(sat_count2)

co_best_seller.to_csv(fc_name, encoding="utf-8-sig", index=False)
time.sleep(3)
co_best_seller.to_excel(fx_name, index=False, engine="openpyxl")

e_time = time.time()
t_time = e_time - s_time

import win32com.client as win32
import win32api

excel = win32.gencache.EnsureDispatch("Excel.Application")
wb = excel.Workbooks.Open(fx_name)
sheet = wb.ActiveSheet
sheet.Columns(2).ColumnWidth = 30
row_cnt = cnt + 1
sheet.Rows("2:%s" % row_cnt).RowHeight = 120

ws = wb.Sheets("Sheet1")
col_name2 = []
file_name2 = []

for a in range(2, cnt + 1):
    col_name = "B" + str(a)
    col_name2.append(col_name)

for b in range(1, cnt + 1):
    file_name = img_dir + "/" + str(b) + ".jpg"
    file_name2.append(file_name)

# 사진 저장하는 부분 오류발생, 추후 디버깅 필요
for i in range(0, cnt):
    rng = ws.Range(col_name2[i])
    image = ws.Shapes.AddPicture(
        file_name2[i], False, True, rng.Left, rng.Top, 130, 100
    )
    excel.Visible = True
    excel.ActiveWorkbook.Save()

driver.close()
