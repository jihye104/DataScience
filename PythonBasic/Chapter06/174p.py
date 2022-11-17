# (1) 모듈 내장클래스 import
# import datetime
from datetime import date,time

# (2) date 클래스
today = date(2022,11,17) #date 객채생성
print(today)

#date 객체 멤버변수 호출
print(today.year)
print(today.month)
print(today.day)

#date 객체 메서드 호출
w = today.weekday()
print(f"요일정보 : {w}")

# (3) time 클래스
currtime = time(10,18,30) #time 객체생성
print(currtime)

#time 객체 멤버변수 호출
print(currtime.hour)
print(currtime.minute)
print(currtime.second)

#time 객체 메서드 호출
isotime = currtime.isoformat() #HH:MM:SS isoformat()디폴트
print(isotime)