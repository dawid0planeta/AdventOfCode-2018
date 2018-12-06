from functools import reduce

def list_changes(data):
    changes = list(map(lambda line: int(line), data)) 
    return changes


def first_repeat(data):
    changes = list_changes(data)
    curr_freq = 0
    i = 0
    freqs = []
    while True:
        next_item = changes[i % len(changes)]
        curr_freq += next_item
        if curr_freq in freqs:
            return curr_freq 
        freqs.append(curr_freq)
        i += 1



def final_freq(data):
    changes = list_changes(data)
    curr_freq = reduce((lambda x, y: x + y), changes)
    return curr_freq 


data = open("input.txt")
print(final_freq(data))
data = open("input.txt")
print(first_repeat(data))

