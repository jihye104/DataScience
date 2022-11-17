# 1. 모듈 추가 (방법1)
# 형식) import 패키지명.모듈명
import Chapter06.myPackage.scattering

#데이터 셋
data = [1,3,1.5,2,1,3.2]

#산술평균 함수 호출
print("평균 :",Chapter06.myPackage.scattering.Avg(data))

#분산과 표준편차 함수 호출
var,sd = Chapter06.myPackage.scattering.var_sd(data)
print(f"분산 : {var}")
print(f"표준편차 : {sd}")

# 2. 모듈 추가 (방법2)
# 형식) from 패키지명.모듈명 import 함수명
from Chapter06.myPackage.scattering import Avg,var_sd

print(f"평균 : {Avg(data)}")

var,sd = var_sd(data)
print(f"분산 : {var}")
print(f"표준편차 : {sd}")