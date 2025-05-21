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
# formatedTime = now.strftime("%Y%m%d%H%M%S%M") #year-month-day-hour-minutes-sec-msec

numberlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numberlist, "\n")

# result = random.sample(numberlist, 1) # [n]
result = []
count = 0

# while len(result) < 6:
    
#     seedTime = time3 + timedelta(count)
#     print("seedTime:", seedTime)

#     seedValue = seedTime.strftime("%Y%m%d%H%M%S%m")
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

seedList = [7, 9 , 24, 40, 42, 44]
for x in seedList:
    random.seed(float(x))
    index = random.randint(0, len(numberlist) - 1)
    value = numberlist[index]
    result.append(value)

# result.sort()
print("result:", result)