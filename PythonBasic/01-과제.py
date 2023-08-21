import math
import os
from tkinter import *


def displayImage():
    global window, canvas, paper, height, width, filename
    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, height=512, width=512)
    paper = PhotoImage(height=512, width=512)
    canvas.create_image((512 / 2, 512 / 2), image=paper, state='normal')

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
        for j in range(i+1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    middle = list[int(len(list)/2)]
    for i in range(height):
        for k in range(width):
            if (image[i][k] < middle):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()


def rotateImage90():
    pass


def rotateImage180():
    pass


def rotateImage270():
    pass


def lRMirrorImage():
    pass


def uDMirrorImage():
    pass


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
btnVeryDarkMid = Button(window, text='흑백(중앙값)', command=veryDarkMidImage)
btnRotation1 = Button(window, text='90도 회전', command=rotateImage90)
btnRotation2 = Button(window, text='180도 회전', command=rotateImage180)
btnRotation3 = Button(window, text='270도 회전', command=rotateImage270)
btnLRMirror = Button(window, text='좌우 미러링', command=lRMirrorImage)
btnUDMirror = Button(window, text='상하 미러링', command=uDMirrorImage)
btnLight.pack()
btnDark.pack()
btnRevese.pack()
btnVeryDark.pack()
btnVeryDarkMean.pack()
btnVeryDarkMid.pack()
btnRotation1.pack()
btnRotation2.pack()
btnRotation3.pack()
btnLRMirror.pack()
btnUDMirror.pack()


filename = 'myImg.raw'
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
