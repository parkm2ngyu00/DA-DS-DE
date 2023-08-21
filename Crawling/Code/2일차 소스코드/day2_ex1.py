# Beautiful Soup 예제 3
from bs4 import BeautifulSoup

ex1 = """
    <html>
        <head>
            <title> HTML 연습 </title>
        </head>
        <body>
            <p align="center"> text 1 </p>
            <p align="center"> text 2 </p>
            <p align="center"> text 3 </p>
            <img src="c:\\temp\\image\\솔개.png">
        </body>
    <html> 
"""

soup = BeautifulSoup(ex1, "html.parser")
# print(soup.find("p").get_text().strip())

x = soup.find_all("p")
for idx, i in enumerate(x, start=1):
    print(idx, i.get_text().strip().replace("text", "txt"))
