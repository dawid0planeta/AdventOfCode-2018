import re
import time
import numpy as np
from matplotlib import pyplot as plt

def read_data(filename: str) -> tuple:
    positions = []
    velocities = []
    with open(filename, 'r') as f:
        for line in f:
            data = list(map(int, re.findall(r'-?\d+', line)))
            pos = (data[0], data[1])
            vel = (data[2], data[3])
            positions.append(pos)
            velocities.append(vel)
    return (np.array(positions), np.array(velocities))

def move_by_n_seconds(positions: 'np_array', velocities: 'np_array', n: int) -> list:
    new_positions = []
    for index in range(len(positions)):
        position = positions[index]
        velocity = velocities[index]
        new_pos = [position[0] + n * velocity[0], position[1] + n * velocity[1]]
        new_positions.append(new_pos)
    return np.array(new_positions) 

def move_by_one(positions: list, velocities: list) -> list:
    return positions + velocities


def find_corners(positions: list) -> tuple:
    maxes = np.amax(positions, axis=0)
    mins = np.amin(positions, axis=0)
    return (mins[0], maxes[0], mins[1], maxes[1]) 

def find_size(coors: tuple) -> tuple:
    return ((coors[1] - coors[0]), (coors[3] - coors[2]))


def solution(filename: str) -> tuple:
    positions, velocities = read_data(filename)
    original_positons = positions
    ranges = find_size(find_corners(move_by_n_seconds(positions, velocities, 0)))
    prev_size = ranges[0] + ranges[1]
    index = 0
    while True:
        positions = move_by_one(positions, velocities)
        ranges = find_size(find_corners(positions))
        curr_size = ranges[0] + ranges[1]
        if prev_size < curr_size:
            return (move_by_n_seconds(original_positons, velocities, index), index)
        prev_size = curr_size
        index += 1

def print_solution(filename: str):
    positions, index = solution(filename)
    outer = find_corners(positions)
    size = find_size(outer)
    print(index)

    data = np.zeros((size[0] + 1, size[1] + 1))

    for each in positions:
        data[each[0] - outer[0]][each[1] - outer[2]] = 1

    data = np.transpose(data)

    plt.imshow(data, interpolation='nearest')
    plt.show()


filename = 'input.txt'
print_solution(filename)


