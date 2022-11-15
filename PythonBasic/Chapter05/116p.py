dataset = list(range(1,6))
print(dataset)

print(f"len = {len(dataset)}")
print(f"sum = {sum(dataset)}")
print(f"max = {max(dataset)}")
print(f"min = {min(dataset)}")

import statistics
print(f"평균 = {statistics.mean(dataset)}")
print(f"중위수 = {statistics.median(dataset)}")

from statistics import variance,stdev
print(f"표본 분산 = {variance(dataset)}")
print(f"표본 표준편차 = {stdev(dataset)}")