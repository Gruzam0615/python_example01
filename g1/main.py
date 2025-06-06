from datetime import datetime, timedelta, timezone
import random

'''
now - nDay == 어제
현재시간서 nDay timedelta(days=n) 만큼 감소
now() - timedelta(days=1)은 현재시간보다 하루이전 값을 출력
'''
now = datetime.now()
# print("now:", now)
standardDay = now + timedelta(-6)
print("standardDay: ", standardDay)
KST = timezone(timedelta(hours=9))
# time1 = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, tzinfo=KST)
# print("time1:", time1)

# time2 = datetime.datetime(now.year, now.month, now.day, 18, 0, now.second, now.microsecond, tzinfo=KST)
# print("time2:", time2)

time3 = datetime(standardDay.year, standardDay.month, standardDay.day, standardDay.hour, standardDay.minute, standardDay.second, standardDay.microsecond, tzinfo=KST)
# time3 = datetime(standardDay.year, standardDay.month, standardDay.day, 20, 49, 11, 22, tzinfo=KST)
print("time3:", time3)

# formatedTime = now.strftime("%Y%m%d%H%M%S%f") #year-month-day-hour-minutes-sec-msec

numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45
            ]

# 추첨시 제외 하고 싶은 숫자 리스트
excludeNumbers = [2, 4, 5, 6, 11, 17, 19, 20, 25, 32, 34, 36, 39] 

for x in excludeNumbers:
    numberlist.remove(x)

print(numberlist, "\n")


# 추첨시 추가하고 싶은 숫자 리스트
includeNumbers = []

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