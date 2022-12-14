# 목적 : 열의 인덱스 값을 사용하여 특정 열을 선택하기
import csv
import sys

input_file = 'supplier_data.csv'
output_file = 'output_files/6output_basic.csv'

# 열의 index를 의미한다.
my_columns = [0,3] # 0번째열, 3번째열

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)

		# 열 필터링 할때는 헤더행을 읽을 필요가 없다.
		# 행 필터링 할때는 헤더행을 읽어야 한다.
		for row_list in filereader: # 행단위
			row_list_output = []

			for index_value in my_columns: # 열단위
				row_list_output.append(row_list[index_value])

			filewriter.writerow(row_list_output)