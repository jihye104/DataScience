# 목적 : 파이썬 기본문법으로 특정행을 필터링하기
import csv
import sys

input_file = 'supplier_data.csv'
output_file = 'output_files/3output.csv'

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader) # 현재포인터를 읽고 다음라인으로 포인터가 넘어감
        filewriter.writerow(header) # writerow => 메서드를 통해 list 데이터를 한라인 추가하게 됨

        for row_list in filereader:
            supplier = str(row_list[0]).strip() # row_list에 0번째 값에서 공백없앰
            # cost = str(row_list[3]).strip('$').replace(',', '')
            cost = str(row_list[3]).strip('$')

            # cost의 값이 600보다 크고 620보다 작은 행을 필터링하는 조건
            if (float(cost) > 600.00) and (float(cost) < 620.00):
                filewriter.writerow(row_list)

            # 같은 결과의 검색 => Supplier Name열의 값이 Z인 경우
            # if supplier == 'Supplier Z':
            # 	filewriter.writerow(row_list)

            # 복합검색
            # if supplier == 'Supplier Y' and float(cost) < 200.0:
            # 	filewriter.writerow(row_list)