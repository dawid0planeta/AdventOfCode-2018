from constants import *
import numpy as np
from read_data import states, test_states
from itertools import cycle

mode = 'prod'
if mode == 'test':
    filename = 'input/test_input_np.npy'
    cartless_filename = 'input/cartless_input_np.npy'
    states = test_states
else:
    filename = 'input/input_np.npy'
    cartless_filename = 'input/cartless_input_np.npy'

data = np.load(filename)
CARTLESS_DATA = np.load(cartless_filename)
rows = len(data)
cols = len(data[0])
print(rows)
print(cols)
def main_tick(data: 'np.array', states: dict) -> '(new_grid: np.array, new_states: dict)':
    moved = []
    for row in range(rows):
        for col in range(cols):
            elem = data[row, col]
            if elem >= 0 and elem <=3 and (row,col) not in moved:
                data, states, new_coors, crashed = move(data, states, row, col) 
                if crashed:
                    return (data, new_coors, crashed)
                moved.append(new_coors)
    return (data, states, False)


def move(data: 'np.array', states: dict,  row: int, col: int) -> '(data: np.array, states:dict)':
    elem_coors = (row, col)
    elem = data[elem_coors]
    if elem == V_UP:
        next_box_coors = (row-1, col)
    elif elem == V_RIGHT:
        next_box_coors = (row, col+1)
    elif elem == V_DOWN:
        next_box_coors = (row+1, col)
    else:
        next_box_coors = (row, col-1)

    next_box = data[next_box_coors] 
    new_elem, states = get_new_elem(elem, elem_coors, next_box, next_box_coors, states)
    if new_elem == CRASH:
        return (data, states, next_box_coors, True)
    data[next_box_coors] = new_elem
    data[elem_coors] = CARTLESS_DATA[elem_coors]
    return (data, states, next_box_coors, False)

def get_new_elem(elem: int, elem_coors: tuple, next_box: int, next_box_coors: tuple, states: dict) -> tuple:
    if next_box in [V_UP, V_RIGHT, V_DOWN, V_LEFT]:
        new_elem = CRASH
    elif next_box == VER or next_box == HOR:
        new_elem = elem 
    elif next_box == LEFT_SLASH:
        if elem == V_LEFT or elem == V_RIGHT:
            new_elem = (elem + 1) % 4
        else:
            new_elem = (elem + 3) % 4
    elif next_box == RIGHT_SLASH:
        if elem == V_LEFT or elem == V_RIGHT:
            new_elem = (elem + 3) % 4
        else:
            new_elem = (elem + 1) % 4
    elif next_box == INTERSECTION:
        new_elem = (elem + next(states[elem_coors])) % 4
    states[next_box_coors] = states[elem_coors]
    return (new_elem, states)


i = 0    
while True:
    print(i)
    data, states, crashed = main_tick(data, states)
    if crashed:
        print(states)
        break
    i += 1
