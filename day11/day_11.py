import numpy as np
from scipy import signal
import time

def create_grid(serial: int) -> 'np.array':
    grid = np.zeros((300, 300))
    for x in range(300):
        rack_id = x + 11
        for y in range(300):
            power = (y+1) * rack_id
            power += serial
            power *= rack_id
            digit = int(str(power)[-3])
            digit -= 5
            grid[y][x] = digit
    return grid

def convolute(grid: 'np.array', size: int) -> 'np.array':
    matrix = np.ones((size,size))
    grad = signal.convolve2d(grid, matrix, mode='valid')
    return grad

def find_coors(grad: 'np.array') -> tuple:
    max_value = np.amax(grad)
    where_result = np.where(grad == max_value)
    coors = (where_result[1][0]+1, where_result[0][0]+1)
    return (max_value, coors)

def solution1(serial: int) -> tuple:
    grid = create_grid(serial)
    grad = convolute(grid, 200)
    _, coors = find_coors(grad)
    return coors

def solution2(serial: int) -> tuple:
    grid = create_grid(serial)
    biggest = 0
    best_coors = ()
    best_size = 0
    for size in range(1, 20):
        grad = convolute(grid, size)
        max_value, coors = find_coors(grad)
        if max_value > biggest:
            biggest = max_value
            best_coors = coors
            best_size = size 
    return (best_size, best_coors)
        

print(solution1(18))
print(solution2(7165))