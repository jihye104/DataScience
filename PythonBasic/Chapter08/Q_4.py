import sys

def greet_users(usernames):
    pass

args = sys.argv[1:]

for name in args:
    # print(f"Hello, {name.capitalize()}")
    print(f"Hello, {name[0].upper()}{name[1:]}")