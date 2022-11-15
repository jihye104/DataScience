position = ['과장','부장','대리','사장','대리','과장']
wc = {}

setpo = set(position)
listpo = list(setpo)
print(listpo)

for key in position:
    wc[key] = wc.get(key,0)+1

print(wc)