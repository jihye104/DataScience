# 목적 : 분산데이터 값의 통계값 구하는 메카니즘 이해
import csv
import glob
import os
import string
import sys

input_path = '.'
output_file = 'output_files/10output_basic.csv'

# 헤더를 새로 정의
output_header_list = ['file_name', 'total_sales', 'average_sales']

# a => 파일에 내용 덧붙임
csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)
# 새로정의한 헤더를 덧붙인다.

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
# 현재 경로에 있는 파일 중 sales_ 가 들어가는 파일을 input_file 변수에 넣는다.
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        # output_list에 input_file을 추가
        header = next(filereader)
        # 헤더행을 읽는다.

        total_sales = 0.0
        # 평균을 구하기 위해 전체 sale amount 행 갯수를 파악하기 위한 변수
        number_of_sales = 0.0

        for row in filereader:
        # (열단위)파일 읽은거를 row 변수에 넣는다.
            sale_amount = row[3]
            total_sales += float(str(sale_amount).strip('$').replace(',',''))
            # total_sales에 sale_amount를 문자열로 변경후 $ 문자 없애고 ,를 empty로 변경해서 하나씩 추가
            number_of_sales += 1.0
            # number_of_sales에 1.0씩 증가

        average_sales = '{0:.2f}'.format(total_sales/number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)

        filewriter.writerow(output_list)
csv_out_file.close()