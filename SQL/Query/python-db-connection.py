#mysql-connector-python
import mysql.connector

#연결 설정
db = mysql.connector.connect(
    host = '127.0.0.1', #localhost
    user = 'root',
    password = 'brian1026',
    database = 'big_leader'
)
#cursor 선언
cursor = db.cursor()
from urllib import request
from bs4 import BeautifulSoup
url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=bib_t&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=search&isFDetailSearch=N&sflag=1&searchQuery=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn='
soup = BeautifulSoup(request.urlopen(url),'html.parser')
#extarct
titles = soup.find('div',class_="srchResultListW").findAll('p','title')
for title in titles:
    title = title.get_text()
    print(f'제목 : {title}')
    query = f"INSERT INTO riss_table VALUES ('{title}');"
    cursor.execute(query)
db.commit()
#종료-
cursor.close()
db.close()