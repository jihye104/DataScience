candidate_list = []
with open("연습생.txt", mode="r", encoding="UTF-8") as file:
    names = file.read()
    candidate_list = names.split()

def show_candidates(candidate_list):
    for name in candidate_list:
        print(name)



def make_idol(candidate_list):
    for name in candidate_list:
        print(f"신예 아이돌 {name} 인기 급상승")



def make_world_star(candidate_list):
    for name in candidate_list:
        print(f"아이돌 {name} 월드스타 등극")


show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)