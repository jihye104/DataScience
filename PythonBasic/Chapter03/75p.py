string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = []
words = []

for sen in string.split(sep = "\n"):
    sents.append(sen)

    for word in sen.split():
        words.append(word)

print(f"문장 : {sents}")
print(f"문장수 : {len(sents)}")
print(f"단어 : {words}")
print(f"단어수 : {len(words)}")