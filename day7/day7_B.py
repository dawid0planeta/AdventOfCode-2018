from Worker import * 

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

def timestep(steps_dict: dict, possible_steps: list, second: int, worker_list: list) -> tuple:
    for worker in worker_list:
        if worker.wants_new_job:
            if worker.job != None:
                for value in steps_dict.values():
                    if worker.job in value:
                        value.remove(worker.job)

    for worker in worker_list:
        if worker.wants_new_job:
            steps_dict, possible_steps, new_job = find_new_job(steps_dict, possible_steps)
            worker.give_new_job(new_job)

    second += 1
    if sum([worker.wants_new_job for worker in worker_list]) == 5:
        return (steps_dict, possible_steps, second, -1)
    for worker in worker_list:
        worker.second_passed()
    return (steps_dict, possible_steps, second, 1)

def find_new_job(steps_dict: dict, possible_steps: list) -> tuple:
    to_delete = []
    for key, value in steps_dict.items():
        if len(value) == 0:
            possible_steps.append(key)
            to_delete.append(key)
    if len(possible_steps) == 0:
        return (steps_dict, possible_steps, None)
    possible_steps.sort()
    new_job = possible_steps[0]
    possible_steps.pop(0)
    for each in to_delete:
        del(steps_dict[each])
    return (steps_dict, possible_steps, new_job)
    
    
def solution(filename: str) -> int:
    steps_dict = create_steps_dict(read_data(filename))
    possible_steps = []
    second = 0
    worker0 = Worker(0)
    worker1 = Worker(1)
    worker2 = Worker(2)
    worker3 = Worker(3)
    worker4 = Worker(4)
    worker_list = [worker0, worker1, worker2, worker3, worker4]
    while True:
        steps_dict, possible_steps, second, finished = timestep(steps_dict, possible_steps, second, worker_list)
        if finished < 0:
            return second - 1

filename = 'input.txt'
print(solution(filename))
