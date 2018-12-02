def list_changes(data):
    changes = []
    for line in data:
        line = line.strip()
        if (line[0] == '+'):
            changes.append(int(line[1:]))
        else:
            changes.append( - int(line[1:]))
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
    curr_freq = 0
    for change in changes:
        curr_freq += change
    return curr_freq 


data = open("input.txt")
print(final_freq(data))
data = open("input.txt")
print(first_repeat(data))

