## 파일은 두 가지
# 텍스트 파일
# 바이너리 파일 --> 이미지 파일 중 raw 파일(1바이트 안에 1픽셀 정의)
import math
import os.path

filename = 'Etc_RAW/LENA256.RAW'
# 파일 크기 알아 내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
print(height, "x", width)

# 메모리 확보 (영상 크기)
image = [[0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1)) # 1바이트씩 읽어서 문자를 0~255 사이의 숫자로 변환 시킨다

rfp.close()

## 일부만 확인
for i in range(100, 105, 1):
    for k in range(100, 105, 1):
        print("%3d " % image[i][k], end='')
    print()
print()

## 반전 처리
for i in range(width):
    for k in range(height):
        image[i][k] = 255 - image[i][k]