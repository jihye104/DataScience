file = open("data/ftest1.txt", mode="r")

lines = file.readlines()
docs = []
words = []

for li1 in lines:
    docs.append(li1.strip())

    for li2 in li1.split():
        words.append(li2)

print(f"문장 내용\n{docs}")
print(f"문장 수 : {len(docs)}")
print(f"단어 내용\n{words}")
print(f"단어 수 : {len(words)}")