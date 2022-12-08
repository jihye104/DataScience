# xlwt 모듈설치
# 목적 : 단일 워크시트 처리
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/2output_basic.xls'

# 새로 쓰고자하는 워크북 생성
output_workbook = Workbook()

# 새로운 워크시트 추가 및 이름설정
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
# 파일에 있는 모든데이터를 workbook으로 이름정함.
    worksheet = workbook.sheet_by_name('january_2013')
    # workbook 안에있는 january_2013 이름을 가진 워크시트를 worksheet로 변수명 정함

    for row_index in range(worksheet.nrows):
    # worksheet의 전체 행개수 -1 만큼 row_index 변수명으로 돌린다.
        for column_index in range(worksheet.ncols):
        # worksheet의 전체 열개수 -1 만큼 column_index 변수명으로 돌린다.
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
            # output_worksheet에 cell_value(행번호, 열번호)에 매치가 되는 셀의 값을 반환해서
            # output_worksheet에서 write(행번호, 열번호, 쓰고자하는 데이터값) 해당 행번호, 열번호에 쓴다.

output_workbook.save(output_file)