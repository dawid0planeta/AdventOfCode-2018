import numpy as np
from constants import *
from itertools import cycle
from Cart import Cart

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

def create_cart_dict(data: 'np.array') -> dict:
    cart_dict = {}
    for dir in [V_DOWN, V_UP, V_LEFT, V_RIGHT]:
        indices = np.where(data == dir)
        for pos in zip(indices[0], indices[1]):
            new_cart = Cart(pos, dir)
            cart_dict[new_cart.weight] = new_cart
    return cart_dict

def remove_carts(cart_dict: dict, data: 'np.array') -> 'cartless_grid: np.array':
    cartless_grid = np.copy(data)
    for key in cart_dict:
        elem = cart_dict[key].direction
        if elem == 0 or elem == 2:
            cartless_grid[cart_dict[key].pos] = VER
        else:
            cartless_grid[cart_dict[key].pos] = HOR
    return cartless_grid


data = create_data_grid('input/input.txt')
test_data = create_data_grid('input/test_input.txt')
cart_dict= create_cart_dict(data)
test_cart_dict= create_cart_dict(test_data)
cartless_data = remove_carts(cart_dict, data)
test_cartless_data = remove_carts(test_cart_dict, test_data)

np.save('input/input_np.npy', data)
np.save('input/test_input_np.npy', test_data)
np.save('input/cartless_input_np.npy', cartless_data)
np.save('input/test_cartless_input_np.npy', test_cartless_data)