# 목적 : 워크시트 집합에 걸쳐서 특정 행 필터링하기
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/11output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('set_of_worksheets')

# 검색하고자하는 워크시트 인덱스
my_sheets = [0,1]
threshold = 1900.0
sales_column_index = 3

first_worksheet = True
with open_workbook(input_file) as workbook:
	data = []
	# 전체 워크시트에 접근하기 위한 for문
	# workbook.nsheets => 전체 워크시트 개수
	for sheet_index in range(workbook.nsheets):
		# 검색하고자 하는 워크시트와 매칭하는 조건
		if sheet_index in my_sheets:
			worksheet = workbook.sheet_by_index(sheet_index)
			if first_worksheet:
				header_row = worksheet.row_values(0) # 0번째 행 반환
				data.append(header_row)
				first_worksheet = False # 다음 워크시트 읽을 떄 헤더행을 추가하지 않음

			# 모든 행을 접근하기 위한 for문
			for row_index in range(1,worksheet.nrows):
				row_list = []
				sale_amount = worksheet.cell_value(row_index, sales_column_index)
				if sale_amount > threshold:

					# 모든 열을 접근하기 위한 for문
					for column_index in range(worksheet.ncols):
						cell_value = worksheet.cell_value(row_index,column_index)
						cell_type = worksheet.cell_type(row_index, column_index)

						# xls는 데이트타입 설정해서 써줘야함
						if cell_type == 3:
							date_cell = xldate_as_tuple(cell_value,workbook.datemode)
							date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
							row_list.append(date_cell)
						else:
							row_list.append(cell_value)
				if row_list:
					data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)