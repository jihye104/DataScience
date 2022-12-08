# 목적: 모든 워크시트에서 특정 행 필터링하기
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/9output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')

sales_column_index = 3
threshold = 2000.0

first_worksheet = True
with open_workbook(input_file) as workbook:
	data = []
	# 모든 워크시트를 처리하기 위해서는 3중 for문이 필요
	# for => 워크시트
	#	for => 행
	#		for => 열
	# sheets() => 모든워크시트를 반환
	for worksheet in workbook.sheets(): # 워크시트 처리하는 for문
		if first_worksheet:
			header_row = worksheet.row_values(0)
			data.append(header_row)
			first_worksheet = False
		for row_index in range(1,worksheet.nrows): # 행처리
			row_list = []
			sale_amount = worksheet.cell_value(row_index, sales_column_index)
			# sale_amount = float(str(sale_amount).replace('$', '').replace(',', ''))
			if sale_amount > threshold:
				for column_index in range(worksheet.ncols): # 열처리
					cell_value = worksheet.cell_value(row_index,column_index)
					cell_type = worksheet.cell_type(row_index, column_index)
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

# 판다스 힌트
# sheet_name 속성을 지정하지 않고 read_excel함수를 수행하면
# 첫번쨰 워크시트만 반환함
# 모든 워크시트를 읽으려면 반드시 sheet_name=None 옵션 설정을 해야함