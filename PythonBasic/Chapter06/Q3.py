class Person:
    name = gender = age = 0

    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        if self.gender == "female":
            print(f"이름 : {self.name}, 성별 : 여자\n나이 : {self.age}")

        elif self.gender == "male":
            print(f"이름 : {self.name}, 성별 : 남자\n나이 : {self.age}")

name = input("이름 입력 : ")
age = input("나이 입력 : ")
gender = input("성별(male/femali) 입력 : ")

p = Person(name,gender,age)

print("="*30)

p.display()

print("="*30)