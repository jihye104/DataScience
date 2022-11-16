class Restaurant:
    restaurant_name = None
    cuisine_type = None

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def __del__(self):
        print(f"{self.restaurant_name} 레스토랑 문닫습니다.")

    def describe_restaurant(self):
        print(f"저희 레스토랑 명칭은 {self.restaurant_name} 이고 {self.cuisine_type} 전문점입니다.")

    def open_restaurant(self):
        print(f"저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.")

restaurant = []

for i in range(0,3):
    restaurant_name,cuisine_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split()
    restaurant.append(Restaurant(restaurant_name,cuisine_type))
    restaurant[i].describe_restaurant()
    restaurant[i].open_restaurant()

print("저녁 10시가 되었습니다.")
