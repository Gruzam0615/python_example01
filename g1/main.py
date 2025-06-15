from datetime import datetime, timedelta, timezone
import random


# 기준일 선언을 위한 값
# 값이 -5 는 5일 전
# 값이 5 는 5일 후
timedeltaValue = -5

# 추첨 시 제외시킬 항목 리스트
excludeNumbers = []

# 추첨 시 포함시킬 항목 리스트
includeNumbers = []


'''
now - nDay == 어제
현재시간서 nDay timedelta(days=n) 만큼 감소
now() - timedelta(days=1)은 현재시간보다 하루이전 값을 출력
'''
now = datetime.now()
# print("now:", now)
# 기준일 선언
standardDay = now + timedelta(timedeltaValue)
print("standardDay: ", standardDay)
KST = timezone(timedelta(hours=9))
# time1 = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, tzinfo=KST)
# print("time1:", time1)

# time2 = datetime.datetime(now.year, now.month, now.day, 18, 0, now.second, now.microsecond, tzinfo=KST)
# print("time2:", time2)

time3 = datetime(standardDay.year, standardDay.month, standardDay.day, standardDay.hour, standardDay.minute, standardDay.second, standardDay.microsecond, tzinfo=KST)
# time3 = datetime(standardDay.year, standardDay.month, standardDay.day, 20, 49, 11, 22, tzinfo=KST)
print("time3:", time3)

# 추첨대상 목록
numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45]


for x in excludeNumbers:
    numberlist.remove(x)

print(numberlist, "\n")

# result = random.sample(numberlist, 1) # [n]
result = []
count = 0

for x in includeNumbers:
    result.append(x)

while len(result) < 6:
    seedTime = time3 + timedelta(count)
    print("seedTime:", seedTime)

    seedValue = seedTime.strftime("%Y%m%d%H%M%S%f")
    print("seedValue: " + seedValue)

    random.seed(int(seedValue))

    print("numberlist len()", len(numberlist))

    temp = random.randint(0, len(numberlist) - 1)
    print("index:", temp)

    value = numberlist[temp]    
    print("value:", value)
    
    result.append(value)
    numberlist.remove(value)
    print(numberlist)

    count = count + 1
    print("\n")


result.sort()
print("result:", result)