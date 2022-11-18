import random

def coffee_lotto(student_list, target_num):
    # names = ["김유진", "문성준", "박종민", "송지예", "양석훈", "이예지", "임성혁", "한권제", "현재봉", "이현구"]
    #
    # # win = int(input("당첨자 수를 입력하세요 : "))
    #
    # for i in range(select_num):
    #     name = random.randint(names)
    #
    #     while name in names:
    #         name = random.randint(names)
    #
    #     names.append(name)

    name = random.sample(student_list,target_num)



def presentation_order(student_list):
    pass

select_num = int(input("1. 커피로또, 2. 발표자순서 : "))

if select_num == 1:
    name = coffee_lotto()

    target_num = int(input("당첨자 수를 입력하세요 : "))

else:
    pass
