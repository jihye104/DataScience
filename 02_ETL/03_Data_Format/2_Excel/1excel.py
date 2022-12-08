# xlrd 모듈 설치
# 목적 : 엑셀 기본정보 확인
import sys
from xlrd import open_workbook

input_file = 'sales_2013.xls'

# 워크시트를 모두 포함한 엑셀 데이터를 workbook으로 표기
# 워크시트 : 단일 목적으로 데이터를 수집한 데이터셋
workbook = open_workbook(input_file)

# nsheets => 워크시트 개수
print('Number of worksheets :',workbook.nsheets)

for worksheet in workbook.sheets():
# workbook의 시트만큼 돌려서 worksheet 변수에 넣는다.

	# nrows => 헤더까지 포함한 전체행수
	print('Worksheet name :',worksheet.name, '\tRows :',worksheet.nrows, '\tColumns :',worksheet.ncols)