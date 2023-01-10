from datetime import date, time, datetime, timedelta
from time import localtime, strftime


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def times(num1, num2):
    return num1 * num2


def dev(num1, num2):
    return num1 / num2


# datetime 모듈 사용하기
# 오늘 날짜
today = date.today()
# 1999년 12월 31일
new_date = date(1999, 12, 31)

print(today)
print(new_date)

# 9시
print(time(9))
# 9시 2분
print(time(9, 2))
# 9시 2분 2초
print(time(9, 2, 2))
# 9시 2분 2초 델타 0.000002초
print(time(9, 2, 2, 2))

# 2002년 10월 20일 14시 5분 2초
dt = datetime(2002, 10, 20, 14, 5, 2)
print(dt)

todayDelta = datetime.now()
print(todayDelta)
print(todayDelta + timedelta(days=20))


# time 모듈 사용하기
now = localtime()
print(now)

# strftime : string format time
now = strftime("%Y-%m-%d %H:%M")
print(now)

now = strftime("%Y년 %m월 %d일 %H시 %M분")
print(now)
