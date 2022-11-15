height = int(input('height : '))

def starcount(height):
    h_cnt = s_cnt = 0

    while h_cnt < height:
        h_cnt += 1
        print("*"*h_cnt)

        s_cnt += h_cnt

    return s_cnt

print(f"start 개수 : {starcount(height)}")