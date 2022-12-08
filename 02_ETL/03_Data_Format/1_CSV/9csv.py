# 목적 : 분산데이터 병합
import csv
import glob
import os
import sys

input_path = '.'
output_file = 'output_files/9output_basic.csv'

# 플래그 변수
first_file = True

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
# 현재 경로에 있는 파일 중 sales_ 가 들어가는 파일을 input_file 변수에 넣는다.
	print(os.path.basename(input_file))

	with open(input_file, 'r', newline='') as csv_in_file:
		with open(output_file, 'a', newline='') as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)

			if first_file:
			# 참이면
				for row in filereader:
				# 파일 읽은거를 row 변수에 넣는다.
					filewriter.writerow(row)
					# row 변수를 행단위로 쓴다.

				first_file = False
				# for문을 나와서 플래그 변수를 false(거짓)로 바꾼다.
			else:
			# 거짓이면
				header = next(filereader)
				# 헤더행을 읽는다.

				for row in filereader:
				# 파일 읽은거를 row 변수에 넣는다.
					filewriter.writerow(row)