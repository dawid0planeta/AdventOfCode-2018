import numpy as np

def convert_signs_to_ones(text: str) -> str:
    new_text = ''
    for each in text:
        if each == '#':
            new_text += '1'
        else:
            new_text += '0'
    return new_text


def create_rule_dict(filename: str) -> dict:
    rules = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            key = convert_signs_to_ones(line[:5])
            value = convert_signs_to_ones(line[9])
            rules[key] = int(value)
    return rules


def add_padding(data: 'np.array', zeroth_index: int) -> '(np.array, int)':
    #front
    first_occurance = np.where(data==1)[0][0]
    while first_occurance < 5:
        data = np.insert(data, 0, 0)
        first_occurance += 1
        zeroth_index += 1
    #back
    last_occurance = len(data) - 1 - np.where(data==1)[0][-1]
    while last_occurance < 5:
        data = np.append(data, 0)
        last_occurance += 1
    return (data, zeroth_index)


def rolling_window(a: 'np.array', window: int) -> 'np.array':
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.array(np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides))


def generation(data: 'np.array', rules: dict, zeroth_index: int) -> '(np.array, int)':
    data, zeroth_index = add_padding(data, zeroth_index)
    windows = rolling_window(data, 5)
    new_data = np.zeros(data.shape)
    index = 2
    for window in windows:
        key = ''.join(window.astype(str))
        if key in rules:
            new_data[index] = rules[key]
        else:
            new_data[index] = 0
        index += 1
    return (new_data.astype(int), zeroth_index) 


def score(data: 'np.array', zeroth_index: int) -> int:
    total = 0
    for i in range(len(data)):
        total += data[i] * (i-zeroth_index)
    return total


def solution1(data: 'np.array', filename: str, generations: int) -> int:
    rules = create_rule_dict(filename)
    zeroth_index = 0
    for _ in range(generations):
        data, zeroth_index = generation(data, rules, zeroth_index)
        total = score(data, zeroth_index)
    return total

def solution2(data: 'np.array', filename:str ) -> int:
    generations_to_stabalize = 108
    before_stabilized = solution1(data, filename, generations_to_stabalize)
    return (before_stabilized + 65 * (50000000000 - generations_to_stabalize))


data = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0]
data = np.array(data)
test_data= [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]
test_data = np.array(test_data)


#print(solution1(data1, 'input.txt'))
print(solution1(data, 'input.txt', 20))
print(solution2(data, 'input.txt'))
