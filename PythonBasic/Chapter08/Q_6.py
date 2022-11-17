input_name = input("이름을 입력하세요 : ")

with open("방명록.txt", mode="r", encoding="UTF-8") as file:
    names = file.read()
    name = names.split()

def search_visitor(name):
    if name == input_name:
        return input_name

    return name