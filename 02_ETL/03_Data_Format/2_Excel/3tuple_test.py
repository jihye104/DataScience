from datetime import date
my_date = (2013, 1, 1, 0, 0, 0)

print(my_date)

print(my_date[0:3])
print(*my_date[0:3])
# strftime() => 원하는 포멧으로 설정 가능, 날짜타입을 스트링 타입으로 변환가능
date_cell = date(*my_date[0:3]).strftime \
					('%m/%d/%Y')
print(date_cell)
print("End")