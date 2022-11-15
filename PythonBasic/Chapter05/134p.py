def a():
    print("a 함수")

    def b():
        print("b 함수")
    return b
b = a()
b()

data = list(range(1,101))

def outer_func(data):
    dataset = data

    def tot():
        tot_val = sum(dataset)
        return tot_val

    def avg(tot_val):
        avg_val = tot_val/len(dataset)
        return avg_val

    return tot,avg

tot,avg = outer_func(data)

tot_val = tot()
print(f"tot = {tot_val}")

avg_val = avg(tot_val)
print(f"avg = {avg_val}")