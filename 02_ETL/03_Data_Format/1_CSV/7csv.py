# 목적 : 열의 헤더명을 사용하여 특정 열을 선택
# 열의 헤더명으로 검색하는 것은 새로운 열이 추가 및 삭제 되었을 경우에
# 기존 프로그램의 수정을 최소화 하기 위해서 필요

import csv
import sys

input_file = 'supplier_data.csv'
output_file = 'output_files/7output_basic.csv'

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)

		# step1. 헤더행을 읽는다.
		header = next(filereader)

		# step2. 필터링할 열의 인덱스를 찾기위해 헤더 열의 값을
		# for문을 돌면서 검색용 열의 인덱스 번호를 찾는다.
		for index_value in range(len(header)):
		# header의 길이만큼 돌려서 index_value 변수에 넣어라
			if header[index_value] in my_columns:
			# 만약 header의 인덱스가 index_value 고, 이게 my_columns 안에 있다면
				my_columns_index.append(index_value)
				# my_columns_index에 index_value를 추가해라

		filewriter.writerow(my_columns)
		# my_columns를 행단위로 써라

		# step3. 인덱스 번호를 기반으로 원하는 열의 모든 데이터를 추출한다.
		for row_list in filereader:
		# 파일 읽은 거를 row_list 변수에 넣어라
			row_list_output = []

			for index_value in my_columns_index:
			# my_columns_index를 index_value 만큼 돌려라
				row_list_output.append(row_list[index_value])
				# row_list_output에 row_list의 인덱스가 index_value인 것을 추가해라

			filewriter.writerow(row_list_output)
			# row_list_output을 행단위로 써라