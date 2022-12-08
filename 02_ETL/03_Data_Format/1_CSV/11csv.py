# 목적 : 유효데이터 선택하기
import csv
import sys

input_file = 'supplier_data_unnecessary_header_footer.csv'
output_file = 'output_files/11output_basic.csv'

row_counter = 0

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)

		for row in filereader:
		# 파일 읽은거를 row 변수에 넣는다.
			if row_counter >= 3 and row_counter <= 15:
			# row_counter가 3이상 15이하이면

				# 쓰레기 값이 추후 변경될 것이 예상된다면,
				# 좀 더 정교한 조건(패턴, 정규식)을 활용해야함
				filewriter.writerow([value.strip() for value in row])
				# row 를 value 만큼 돌려서 공백제거를 한다.

			row_counter += 1
			# row_counter를 1씩 증가한다.