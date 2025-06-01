from datetime import datetime, timedelta, timezone
import random

'''
now - nDay == 어제
현재시간서 nDay timedelta(days=n) 만큼 감소
now() - timedelta(days=1)은 현재시간보다 하루이전 값을 출력
'''
now = datetime.now()
# print("now:", now)
standardDay = now + timedelta(-1)
print("standardDay: ", standardDay)
KST = timezone(timedelta(hours=9))
# time1 = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, tzinfo=KST)
# print("time1:", time1)
# time2 = datetime.datetime(now.year, now.month, now.day, 18, 0, now.second, now.microsecond, tzinfo=KST)
# print("time2:", time2)
# time3 = datetime(standardDay.year, standardDay.month, standardDay.day, standardDay.hour, standardDay.minute, standardDay.second, standardDay.microsecond, tzinfo=KST)
time3 = datetime(standardDay.year, standardDay.month, standardDay.day, 0, 0, 0, tzinfo=KST)
# print("time3:", time3)
# formatedTime = now.strftime("%Y%m%d%H%M%S%f") #year-month-day-hour-minutes-sec-msec

numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45
            ]
print(numberlist, "\n")

# result = random.sample(numberlist, 1) # [n]
result = []
count = 0

# while len(result) < 6:
    
#     seedTime = time3 + timedelta(count)
#     print("seedTime:", seedTime)

#     seedValue = seedTime.strftime("%Y%m%d%H%M%S%f")
#     # print(seedValue)

#     random.seed(int(seedValue))

#     print("numberlist len()", len(numberlist))

#     temp = random.randint(0, len(numberlist) - 1)
#     print("temp:", temp)

#     value = numberlist[temp]    
#     print("value:", value)
    
#     result.append(value)
#     numberlist.remove(value)
#     print(numberlist)

#     count = count + 1
#     print("\n")

# seedList = [920120, 930807, 931004, 940204, 930415, 930817]
seedList = [1, 2, 3, 4, 5, 6]
for x in seedList:
    random.seed(float(x))
    index = random.randint(0, len(numberlist) - 1)
    value = numberlist[index]
    numberlist.remove(value)
    result.append(value)

result.sort()
print("result:", result)