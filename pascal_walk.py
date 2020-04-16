import numpy as np
from scipy.linalg import pascal

"""
    Move from one to another end for each '1' in binary representation!
    And also take account of additional 1's we lose per lane switching, then add it as tail...
    We only switch lanes until 32th row!
"""

pascal_triangle = pascal(100, kind='lower')

def to_bin(a: int):
    return [c=='1' for c in bin(a)[2:]][::-1]

def flip_num(bin_flip):
    sds = 0
    for i in bin_flip:
        if i:
            sds += 1
    return sds

def construct_path(target):
    if target <= 32:
        return [(x+1, 1) for x in range(target)]
    else:
        target_ = target - 32
        bin_flip = to_bin(target_)
        flip_nums = flip_num(bin_flip) # add extra tail of 1s
        # print(flip_nums)
        at_tail = False
        route = []
        for i in range(32):
            if i < len(bin_flip) and bin_flip[i]:
                if not at_tail:
                    for j in range(i + 1):
                        route.append((i+1, j+1))
                    at_tail = True
                else:
                    for j in reversed(range(i + 1)):
                        route.append((i+1, j+1))
                    at_tail = False
            else:
                if at_tail:
                    route.append((i + 1, i + 1))
                else:
                    route.append((i + 1, 1))
        for i in range(flip_nums):
            if at_tail:
                route.append((i + 32 + 1, i + 32 + 1))
            else:
                route.append((i + 32 + 1, 1))
        return route


def check_route(route):
    sum_ = 0
    for coord in route:
        sum_ += pascal_triangle[coord[0]-1, coord[1] - 1]
    return sum_



if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        g = construct_path(N)
        print("Case #{}:".format(i))
        for x, y in g:
            print(x, y)
        # print(check_route(g))
        # print(len(g))
