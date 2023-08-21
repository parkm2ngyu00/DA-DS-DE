import math
import os
from tkinter import *
# 함수


def displayImage():
    # global : 외부의 변수를 대입하기 때문에 사용
    # 사용만 한다? global 쓰지 않아도 됨
    global window, canvas, paper, height, width, filename
    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, height=256, width=256)
    paper = PhotoImage(height=256, width=256)
    canvas.create_image((256 / 2, 256 / 2), image=paper, state='normal')

    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    canvas.pack()


def reverseImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]

    displayImage()


def lightImage():
    for i in range(height):
        for j in range(width):
            if (image[i][j] + 50 > 255):
                image[i][j] = 255
            else:
                image[i][j] += 50
    displayImage()


def darkImage():
    for i in range(height):
        for j in range(width):
            if (image[i][j] - 100 < 0):
                image[i][j] = 0
            else:
                image[i][j] -= 100
    displayImage()


def veryDarkImage():
    for i in range(height):
        for j in range(width):
            if (image[i][j] > 127):
                image[i][j] = 255
            else:
                image[i][j] = 0

    displayImage()


def veryDarkMeanImage():
    sum = 0
    for i in range(height):
        for k in range(width):
            sum += image[i][k]
    avg = sum / (height * width)

    for i in range(height):
        for k in range(width):
            if (image[i][k] < avg):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()


def veryDarkMidImage():
    # 2차원 배열을 1차원 배열로
    list = []
    for i in image:
        for k in i:
            list.append(k)
    for i in range(len(list)):
        minIndex = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    middle = list[int(len(list) / 2)]
    for i in range(height):
        for k in range(width):
            if (image[i][k] < middle):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()


# 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

# 메인
window = Tk()
window.geometry('700x700')
window.title('영상처리 Alpha')


btnRevese = Button(window, text='반전', command=reverseImage)
btnLight = Button(window, text='밝게', command=lightImage)
btnDark = Button(window, text='어둡게', command=darkImage)
btnVeryDark = Button(window, text='흑백', command=veryDarkImage)
btnVeryDarkMean = Button(window, text='흑백(평균)', command=veryDarkMeanImage)
btnVeryDarkMid = Button(window, text='흑백(중간값)', command=veryDarkMidImage)
btnLight.pack()
btnDark.pack()
btnRevese.pack()
btnVeryDark.pack()
btnVeryDarkMean.pack()
btnVeryDarkMid.pack()


filename = 'Etc_Raw\LENA256.RAW'
# 파일 크기 알아내기
fSize = os.path.getsize(filename)  # Byte 단위
height = width = int(math.sqrt(fSize))
# 메모리 확보 (영상 크기)
image = [[0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1))

rfp.close()

displayImage()

window.mainloop()

# 퀴즈 : 밝게, 어둡게, 흑백(127), 흑백(평균)
