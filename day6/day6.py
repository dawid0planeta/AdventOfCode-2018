def read_data(filename: str) -> list:

    file = open(filename)
    data = []

    for line in file:
        line = line.rstrip()
        coor = line.split(", ")
        coor = list(map(int, coor))
        data.append(coor)
    return data


def solution1(filename: str) -> int:
    data = read_data(filename)
    return find_largest(data)


def taxi_dist(point_a: list, point_b: list) -> int:
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

def find_infinte(data: list) -> list:
    infinite = []
    x_coors = []
    y_coors = []
    for each in data:
        x_coors.append(each[0])
        y_coors.append(each[1])
    left_bound = min(x_coors)
    right_bound = max(x_coors) 
    top_bound = min(y_coors)
    bot_bound = max(y_coors) 
    for each in data:
        if each[0] == left_bound or each[0] == right_bound or each[1] == top_bound or each[1] == bot_bound:
            infinite.append(data.index(each))
    return infinite



def find_point_owner(data: list, coors: list) -> int:
    point_list = [] 
    for line in data:
        dist = taxi_dist(line, coors)
        point_list.append(dist)
    min_dist = min(point_list)
    if point_list.count(min_dist) > 1:
        return -1
    else:
        return point_list.index(min_dist)

import sys


def create_owner_table(data: list, size: int) -> dict:
    owner_table = {}
    for index in range(len(data)):
        owner_table[index] = 0

    for i in range(-size, size):
        for j in range(-size, size):
            owner = find_point_owner(data, [j,i])
            if owner >= 0:
                owner_table[owner] += 1

    
    for key in owner_table:
        if key in find_infinte(data):
            owner_table[key] = -1
    return owner_table


import operator
def find_largest(data: list) -> int:
    owner_table_small = create_owner_table(data, 500)
    owner_table_big = create_owner_table(data, 600)
    for i in range(len(data)):
        if owner_table_big[i] != owner_table_small[i]:
            owner_table_big[i] = -1
    return max(owner_table_big.items(), key=operator.itemgetter(1))


def sum_distance(data: list, coors: list) -> int:
    sum = 0
    for each in data:
        sum += taxi_dist(each, coors)
    return sum


def solution2(data: list) -> int:
    region_size = 0
    for i in range(500):
        for j in range(500):
            if sum_distance(data, [j,i]) < 10000:
                region_size += 1
    return region_size




filename = 'input.txt'
data = read_data(filename)
print(solution2(data))


