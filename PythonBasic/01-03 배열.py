import random

ary = []
for i in range(0, 10, 1) :
    ary.append(random.randint(0, 10))

print(ary)

# 배열 값의 합
sum = 0
for i in range(len(ary)):
    sum += ary[i]
print(sum)

# 배열 중 홀수만 합계
sum = 0
for i in range(len(ary)):
    if (ary[i] % 2 == 0):
        continue
    sum += ary[i]
print(sum)