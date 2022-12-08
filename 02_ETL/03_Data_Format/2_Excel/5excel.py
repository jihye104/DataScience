# 목적 : 특정 집합의 값을 포함하는 행의 필터링
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/5output_basic.xls'

