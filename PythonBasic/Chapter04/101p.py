charset = ['abc','code','band','band','abd']
wc = {}

for key in charset:
    wc[key] = wc.get(key,0)+1

print(wc)