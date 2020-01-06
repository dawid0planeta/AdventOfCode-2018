def read_data(filename: str) -> list:
    file = open(filename)
    data = []
    for line in file:
        line = line.rstrip()
        data.append([line[5], line[36]])
    return data

def create_steps_dict(data: list) -> set:
    steps_dict = {}
    unique_steps = set([item for sublist in data for item in sublist])
    for step in unique_steps:
        steps_dict[step] = []
    for each in data:
        steps_dict[each[1]].append(each[0])
    
    return steps_dict

    
def timestep(steps_dict: dict, possible_steps: list, done_steps: str) -> tuple:
    to_delete = []
    for key, value in steps_dict.items():
        if len(value) == 0:
            possible_steps.append(key)
            to_delete.append(key)
    possible_steps.sort()
    print(possible_steps)
    next_step = possible_steps[0]
    possible_steps.pop(0)
    print(next_step)
    done_steps += next_step
    for each in to_delete:
        del(steps_dict[each])
    for value in steps_dict.values():
        if next_step in value:
            value.remove(next_step)
    return (steps_dict, possible_steps, done_steps)



def solution1(filename: str) -> str:
    steps_dict = create_steps_dict(read_data(filename))
    possible_steps = []
    done_steps = ''
    while True:
        steps_dict, possible_steps, done_steps = timestep(steps_dict, possible_steps, done_steps)
        if not bool(steps_dict):
            return done_steps
            
            



filename = 'input.txt'
print(solution1(filename))
 