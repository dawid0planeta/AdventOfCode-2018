initial_state, rules, generations = None, {}, 50000000000
for line in open('day_12.txt'):
    if not initial_state:
        initial_state = line.split()[2]
    elif len(line) > 1:
        l = line.split()
        rules[l[0]] = l[2]

current = dict((idx, char) for idx, char in enumerate(initial_state) if char == "#")
last_sum, difference = 0, {}
for gen in range(generations):
    min_key, max_key = min(current) - 2, max(current) + 2
    next_state = {}
    for char in range(min_key, max_key + 1):
        pattern = ""
        for idx in range(char - 2, char + 3):
            if idx in current:
                pattern += current[idx]
            else:
                pattern += "."
        next_state[char] = rules[pattern]
    current = dict((idx, next_state[idx]) for idx in next_state if next_state[idx] == "#")
    diff = sum(current) - last_sum
    if gen == 19:
        print("1: %d" % sum(current))
    if diff in difference and difference[diff] > 1000:
        print("2; %d" % (sum(current) + (generations - gen - 1) * diff))
        break
    if diff not in difference:
        difference[diff] = 1
    else:
        difference[diff] += 1
    last_sum = sum(current)