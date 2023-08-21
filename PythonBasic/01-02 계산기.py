## 함수
def addFunc(num1, num2):
    return num1 + num2

def subFunc(num1, num2):
    return num1 - num2

def mulFunc(num1, num2):
    return num1 * num2

def divFunc(num1, num2):
    return num1 / num2

## 전역변수
num1, num2 = 0, 0
result = 0

## 메인
while(True) :
    opcode = int(input('어떤 연산을 할까요?(1 : 덧셈, 2 : 뺄셈, 3 : 곱셈, 4 : 나눗셈, 0 : 종료) '))
    if (opcode == 0) :
        break
    num1 = int(input('숫자1 : '))
    num2 = int(input('숫자2 : '))
    if (opcode == 1) :
        result = addFunc(num1, num2)
    elif (opcode == 2) :
        result = subFunc(num1, num2)
    elif (opcode == 3) :
        result = mulFunc(num1, num2)
    elif (opcode == 4) :
        result = divFunc(num1, num2)
    print(result)
    continue