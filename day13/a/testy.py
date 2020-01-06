from constants import *
import numpy as np
from read_data import cart_dict, test_cart_dict

mode = 'prod'
if mode == 'test':
    filename = 'input/test_input_np.npy'
    cartless_filename = 'input/test_cartless_input_np.npy'
    cart_dict = test_cart_dict
else:
    filename = 'input/input_np.npy'
    cartless_filename = 'input/cartless_input_np.npy'

data = np.load(filename)
CARTLESS_DATA = np.load(cartless_filename)
rows = len(data)
cols = len(data[0])

def iterate(cart_dict: dict, data: list, iteration: int) -> tuple:
    crashed = ()
    for key in range(22500):
        if key in cart_dict:
            cart = cart_dict[key]

            if cart.iteration > iteration:
                continue
            cart_dict, data, crashed = decide(key, data, cart_dict)
            if len(crashed) == 2:
                return (cart_dict, data, crashed)

            cart.iteration += 1
    
    return (cart_dict, data, crashed)

    



def find_next_box_pos(cart: "cart_object", cart_pos: "tuple") -> tuple:
    row = cart_pos[0]
    col = cart_pos[1]

    cart_direction = cart.direction
    if cart_direction == V_UP:
        next_box_pos = (row-1, col)
    elif cart_direction == V_RIGHT:
        next_box_pos = (row, col+1)
    elif cart_direction == V_DOWN:
        next_box_pos = (row+1, col)
    else:
        next_box_pos = (row, col-1)

    return next_box_pos


def decide(key: int, data: "np.array", cart_dict: dict) -> tuple:
    cart = cart_dict[key]
    cart_pos = cart.pos
    cart_direction = cart.direction
    old_weight = cart.weight
    next_box_pos = find_next_box_pos(cart, cart_pos)
    next_box = data[next_box_pos]
    crashed = ()
    next_box_weight = next_box_pos[0] * 150 + next_box_pos[1] 

    if next_box < 4 and next_box > -1:
        data = crash(cart_pos, next_box_pos, data)
        del cart_dict[old_weight]
        del cart_dict[next_box_weight]
        crashed = (next_box_pos) 
    elif next_box == VER or next_box == HOR:
        data = move(cart, cart_pos, cart_direction, next_box_pos, data)
        cart_dict[next_box_weight] = cart_dict.pop(old_weight)
    else:
        data = rotate(cart, cart_pos, cart_direction, next_box_pos, data)
        cart_dict[next_box_weight] = cart_dict.pop(old_weight)

    return (cart_dict, data, crashed)


def crash(cart_pos: tuple, next_box_pos: tuple, data: "np.array") -> "np.array":
    data[cart_pos] = CARTLESS_DATA[cart_pos]
    data[next_box_pos] = CARTLESS_DATA[next_box_pos]
    return data




def move(cart: "cart_object", cart_pos: tuple, cart_direction: int, next_box_pos: tuple, data: "np.array"):
    data[cart_pos] = CARTLESS_DATA[cart_pos] 
    data[next_box_pos] = cart_direction
    cart.pos = next_box_pos
    cart.update()
    return data

def rotate(cart: "cart_object", cart_pos: tuple, cart_direction: int, next_box_pos: tuple, data: "np.array"):
    next_box = data[next_box_pos]
    if next_box == LEFT_SLASH:
        if cart_direction == V_LEFT or cart_direction == V_RIGHT:
            cart.direction = (cart_direction + 1) % 4
        else:
            cart.direction = (cart_direction + 3) % 4
    elif next_box == RIGHT_SLASH:
        if cart_direction == V_LEFT or cart_direction == V_RIGHT:
            cart.direction = (cart_direction + 3) % 4
        else:
            cart.direction = (cart_direction + 1) % 4
    else:
        cart.direction = (cart_direction + next(cart.state)) % 4

    data[cart_pos] = CARTLESS_DATA[cart_pos] 
    data[next_box_pos] = cart.direction
    cart.pos = next_box_pos
    cart.update()
    return data





i = 0    
while True:
    iteration = i
    print(i)
    cart_dict, data, crashed = iterate(cart_dict, data, iteration)
    if len(cart_dict) == 1:
        for each in cart_dict:
            print(cart_dict[each].pos)
        break
    i += 1
