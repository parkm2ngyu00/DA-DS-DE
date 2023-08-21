import math
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image  # pillow 라이브러리 중 Image 객체만 사용


# 함수 선언부


def loadImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window, filetypes=(
        ("칼라", "*.png;*.jpg;*.bmp;*.gif;"), ("모든파일", "*.*")))
    # 파일 크기 알아내기
    pillow = Image.open(filename)
    inH = pillow.height
    inW = pillow.width
    # 메모리 확보 (영상 크기)
    # R, G, B 3차원 배열
    inImage = [[[0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)]
    # 파일 --> 메모리 로딩
    pillowRGB = pillow.convert('RGB')  # RGB 모델로 변경
    for i in range(inH):
        for k in range(inW):
            r, g, b = pillowRGB.getpixel((k, i))  # 내부적으로 바뀌어 있어서 k, i위치가 바꿔어야함
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b

    equalImage()


def displayImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    if canvas != None:
        canvas.destroy()
    window.geometry(str(outW) + 'x' + str(outH))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')

    # for i in range(outH):
    #     for k in range(outW):
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    # 속도가 빨라짐
    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r = outImage[0][i][k]
            g = outImage[1][i][k]
            b = outImage[2][i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)  # 한 칸 띄워야 다음거로 인식
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)

    canvas.pack()


def saveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw', filetypes=(
        ("RAW파일", "*.raw"), ("모든파일", "*.*")))
    import struct
    for i in range(outH):
        for k in range(outW):
            saveFp.write(struct.pack('B', outImage[i][k]))
    saveFp.close()
    messagebox.showinfo('성공', saveFp.name + '으로 저장')


# 영상처리 함수


def equalImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][k]
    displayImage()


def reverseImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    outH = inH
    outW = inW
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255 - inImage[i][k]
    displayImage()


def addImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    value = askinteger("값 입력", "-255부터 255까지 입력", minvalue=-255, maxvalue=255)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (inImage[rgb][i][k] + value > 255):
                    outImage[rgb][i][k] = 255
                elif (inImage[rgb][i][k] + value < 0):
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = inImage[rgb][i][k] + value
    displayImage()


def reverseImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    value = askinteger("값 입력", "0부터 255까지 입력", minvalue=0, maxvalue=255)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (inImage[rgb][i][k] < value):
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0
    displayImage()


def moveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    xVal = askinteger("X 입력", "")
    yVal = askinteger("Y 입력", "")
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (0 <= i + xVal < outH) and (0 <= k + yVal < outW):
                    outImage[rgb][i+xVal][k+yVal] = inImage[rgb][i][k]
    displayImage()


def zoomOutImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    scale = askinteger("축소 배율", "")
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    outH = inH // scale  # 몫
    outW = inW // scale
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i//scale][k//scale] = inImage[rgb][i][k]
    displayImage()


def zoomInImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    scale = askinteger("확대 배율", "")
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    outH = inH * scale
    outW = inW * scale
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]

    # forwarding 기법 --> 문제 : hole문제가 생김
    # for i in range(inH):
    #     for k in range(inW):
    #         outImage[i*scale][k*scale] = inImage[i][k]

    # backwarding 기법
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                outImage[rgb][i][k] = inImage[rgb][i//scale][k//scale]

    displayImage()


def rotateImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    angle = askinteger("각도", "0~360")
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    radian = - angle * math.pi / 180.0  # (-)붙이는 이유는 시계방향 회전 ...
    cx = inH / 2
    cy = inW / 2

    # forwarding
    # for i in range(inH):
    #     for k in range(inW):
    #         newI = int(math.cos(radian)*(i-cx) - math.sin(radian)*(k-cy)+cx)
    #         newK = int(math.sin(radian)*(i-cx) + math.cos(radian)*(k-cy)+cy)
    #         if (0 <= newI < outH) and (0 <= newK < outW):
    #             outImage[newI][newK] = inImage[i][k]

    # backwarding
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                oldI = int(math.cos(radian)*(i-cx) +
                           math.sin(radian)*(k-cy)+cx)
                oldK = int(math.sin(radian)*(i-cx) -
                           math.cos(radian)*(k-cy)+cy)
                if (0 <= oldI < inH) and (0 <= oldK < inW):
                    outImage[rgb][i][k] = inImage[rgb][oldI][oldK]
    displayImage()


def grayImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    for i in range(inH):
        for k in range(inW):
            sum = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
            outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = sum // 3
    displayImage()


def gammaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    value = askfloat("감마값", "0보다 큰 실수를 입력하세요")
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = int(math.pow(
                    inImage[rgb][i][k]/255, value) * 255)
                if outImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                if outImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
    displayImage()


def parabolaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지 크기 결정 --> 알고리즘에 따라서 ...
    parabola = askstring("파라볼라연산(cap or cup)", "cap or cup")
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)]
                 for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if parabola == "cup":
                    outImage[rgb][i][k] = 255 * \
                        int(math.pow(inImage[rgb][i][k]/127, 2))
                elif parabola == "cap":
                    outImage[rgb][i][k] = 255 - 255 * \
                        int(math.pow(inImage[rgb][i][k]/127, 2))
                if outImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                if outImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
    displayImage()


# 전역 변수부
window, canvas, paper = None, None, None
filename = ""
inImage, outImage = None, None
inH, inW, outH, outW = 0, 0, 0, 0

# 메인 코드부
window = Tk()
window.geometry('300x300')
window.title('Colorful Image Processing (GA)')

mainMenu = Menu(window)  # 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)  # 상위 메뉴(파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=loadImage)
fileMenu.add_command(label='저장', command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=None)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='화소점 처리', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)
image1Menu.add_command(label='그레이스케일', command=grayImage)
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='감마연산', command=gammaImage)
image1Menu.add_command(label='파라볼라연산', command=parabolaImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=image2Menu)
image2Menu.add_command(label='이동', command=moveImage)
image2Menu.add_command(label='축소', command=zoomOutImage)
image2Menu.add_command(label='확대', command=zoomInImage)
image2Menu.add_command(label='회전', command=rotateImage)


window.mainloop()
