x = 50

def local_func(x):
    x += 50 # x = x+50
    print(x)

local_func(x)
print(f"x = {x}")

def global_func():
    global x
    x += 50
    print(x)

global_func()
print(f"x = {x}")
