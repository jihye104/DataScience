# 목적 : 특정 조건을 충족하는 행의 필터링
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/4output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

sale_amount_column_index = 3

with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = []
	header = worksheet.row_values(0)
	data.append(header)

	for row_index in range(1,worksheet.nrows):
	# 헤더를 뺀 나머지를 row_index 변수명으로 전체행 개수만큼 돌린다.
		row_list = []
		sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)
		# worksheet에 cell_value(행번호, 열번호)에 매치가 되는 셀의 값을 sale_amount 변수명으로 지정

		if sale_amount > 1400.0:
		# sale_amount가 1400.0 보다크면
			for column_index in range(worksheet.ncols):
			# 모든 열개수-1 만큼 column_index 변수명으로 돌린다.
				cell_value = worksheet.cell_value(row_index, column_index)
				# worksheet에 cell_value(행번호, 열번호)에 매치가 되는 셀의 값을 cell_value 변수명으로 지정
				cell_type = worksheet.cell_type(row_index, column_index)
				# worksheet에 해당 행, 열의 셀타입을 cell_type 변수명으로 지정

				if cell_type == 3:
				# 만약 그 셀타입이 3이면
					# xldate_as_tuple => 시간데이터를 읽기위해 사용하는 메서드
					date_cell = xldate_as_tuple(cell_value, workbook.datemode)
					# 위에 지정한 cell_value를 반환해서 workbook을 데이트모드로 전환한 걸 date_cell 변수명으로 지정
					date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
					# date_cell의 인덱스 0번부터 2번까지(년,월,일) 슬라이싱해서 %m/%d/%Y 형식으로 변환 후 date_cell 변수명으로 재지정
					row_list.append(date_cell)

				else:
				# 3이 아니면
					row_list.append(cell_value)

			if row_list:
			# 만약 row_list면
				data.append(row_list)

	# enumerate() => 인덱스와 원소를 동시에 접근하려고
	for list_index, output_list in enumerate(data):
	# data에 인덱스는 list_index로 원소는 output_list로 변수명을 지정해서 돌린다.
		for element_index, element in enumerate(output_list):
		# output_list에 인덱스는 element_index로 원소는 element로 변수명을 지정해서 돌린다.
			output_worksheet.write(list_index, element_index, element)
			# output_worksheet에서 write(행번호, 열번호, 쓰고자하는 데이터값) 해당 행번호, 열번호에 쓴다.

output_workbook.save(output_file)