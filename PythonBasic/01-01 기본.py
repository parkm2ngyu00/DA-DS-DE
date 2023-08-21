## 함수 선언부
def addNum(start, end):
    result = 0
    i = start
    while (i <= end):
        result += i
        i += 1
    return result

## 전역 변수부
sum = 0

## 메인 코드부
sum = addNum(1, 100)
print(sum)