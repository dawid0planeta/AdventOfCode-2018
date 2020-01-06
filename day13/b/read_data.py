import numpy as np
from constants import *
from itertools import cycle

char_to_int_dict = {
    ' ': EMPT,
    '-': HOR,
    '|': VER,
    '\\': LEFT_SLASH,
    '/': RIGHT_SLASH,
    '+': INTERSECTION,
    '^': V_UP,
    'v': V_DOWN,
    '<': V_LEFT,
    '>': V_RIGHT,
    'X': CRASH
}


def create_data_grid(filename: str) -> list:
    data_grid = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            new_row = []
            for char in line:
                new_row.append(char_to_int_dict[char])
            data_grid.append(new_row)
    np_data = np.array(data_grid, dtype='uint8')
    return np_data 

def create_state_dict(data: 'np.array') -> dict:
    states = {} 
    for dir in [V_DOWN, V_UP, V_LEFT, V_RIGHT]:
        indices = np.where(data == dir)
        for pos in zip(indices[0], indices[1]):
            states[pos] = cycle([3, 0, 1]) 
    return states 

def remove_carts(states: dict, data: 'np.array') -> 'cartless_grid: np.array':
    cartless_grid = np.copy(data)
    for key in states:
        elem = data[key]
        if elem == 0 or elem == 2:
            cartless_grid[key] = VER
        else:
            cartless_grid[key] = HOR
    return cartless_grid


data = create_data_grid('input/input.txt')
test_data = create_data_grid('input/test_input.txt')
states = create_state_dict(data)
test_states = create_state_dict(test_data)
cartless_data = remove_carts(states, data)
cartless_test_data = remove_carts(test_states, test_data)

np.save('input/input_np.npy', data)
np.save('input/test_input_np.npy', test_data)
np.save('input/cartless_input_np.npy', cartless_data)
np.save('input/test_cartless_input_np.npy', cartless_test_data)