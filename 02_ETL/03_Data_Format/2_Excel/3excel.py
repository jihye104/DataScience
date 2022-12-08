# 목적 : 날짜 형식 할당
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/3output_basic.xls'

# 새로추가할 워크시트 이름
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')

	for row_index in range(worksheet.nrows):
		row_list_output = []

		for col_index in range(worksheet.ncols):
			# cell_type의 반환값이 3인 경우는 날짜 타입
			if worksheet.cell_type(row_index, col_index) == 3:
				# xldate_as_tuple => 시간데이터를 읽기위해 사용하는 메서드
				date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
				# worksheet에 cell_value(행번호, 열번호)에 매치가 되는 셀의 값을 반환해서,
				# workbook을 데이트모드로 전환한 걸 date_cell 변수명으로 지정

				# strftime() => 원하는 포켓으로 설정가능, 날짜타입을 문자타입으로 변환
				date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
				# 제공하는 데이트 타입은 년,월,일,시,분,초
				# date_cell의 인덱스 0번부터 2번까지(년,월,일) 슬라이싱해서 %m/%d/%Y 형식으로 변환 후 date_cell 변수명으로 재지정
				row_list_output.append(date_cell)
				output_worksheet.write(row_index, col_index, date_cell)
				# output_worksheet에서 write(행번호, 열번호, 쓰고자하는 데이터값) 해당 행번호, 열번호에 쓴다.

			else:
			# 날짜타입이 아닌경우
				non_date_cell = worksheet.cell_value(row_index, col_index)
				# worksheet에 cell_value(행번호, 열번호)에 매치가 되는 셀의 값을 non_date_cell 변수명으로 지정
				row_list_output.append(non_date_cell)
				# 그 값을 row_list_output에 추가한다.
				output_worksheet.write(row_index, col_index, non_date_cell)
				# output_worksheet에서 write(행번호, 열번호, 쓰고자하는 데이터값) 해당 행번호, 열번호에 쓴다.

output_workbook.save(output_file)