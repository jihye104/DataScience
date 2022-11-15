def adder(x,y):
    add = x+y
    return add
print(f"add = {adder(10,20)}")

print(f"add = {(lambda x,y : x+y)(10,20)}")