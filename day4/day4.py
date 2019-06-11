from datetime import datetime
import time


def import_file(filename: str) -> list:
    imported = open(filename)
    data = []
    for line in imported:
        data.append(read_data(line.strip()))
    data.sort(key=lambda time: time[0])   
    return data


def read_data(log: str) -> list:
    log_action = log[19:]
    log_time = datetime.strptime(log[1:17], '%Y-%m-%d %H:%M')

    if log_action == 'wakes up':
        log_action = 1
    elif log_action == 'falls asleep':
        log_action = -1
    else:
        guard_id = log_action.split(' ')[1][1:]
        log_action = guard_id
    return [log_time, log_action]


def create_guards_table(data: list) -> dict:
    guards_table = []
    for line in data:
        if line[1] != 1 and line[1] != -1:
            guards_table.append(line[1])
    return {key: [] for key in (set(guards_table))}


def split_by_guard(guards_table: dict) -> dict:
    for line in data:
        if line[1] in guards_table:
            curr_guard = line[1]
        guards_table[curr_guard].append(line)
    return(guards_table)


def minutes_asleep(guards_table: dict, guard_id: str) ->  list:
    # Returns list of lists of minutes spent sleeping in a day
    guard_log = guards_table[guard_id]
    minutes_asleep = []
    day_index = -1
    pointer = 0
    while pointer < len(guard_log):
        line = guard_log[pointer]
        if type(line[1]) == str:
            day_index += 1
            pointer += 1
            minutes_asleep.append([])
            continue
        if line[1] == -1:
            minutes_asleep[day_index].extend(range(line[0].minute, guard_log[pointer+1][0].minute))
            pointer += 2
    return minutes_asleep


def create_sleep_pattern(minutes_asleep: list) -> list:
    # Converts minutes_asleep to vector of 1: (minute slept) and 0: (minutes awake)
    sleep_pattern = [[1 if i in day else 0 for i in range(60)] for day in minutes_asleep]
    # Returns sum of day vectors
    return [sum(x) for x in zip(*sleep_pattern)]


def analyze_guards_sleep_pattern(data: list) -> dict:
    guards_table = create_guards_table(data)
    split_by_guard(guards_table)
    for id in guards_table:
        guards_table[id] = create_sleep_pattern(minutes_asleep(guards_table, id))
    return guards_table


def find_sleepy_guard(guards_table: dict) -> tuple:
    max_minutes_slept = 0
    max_id = ''
    for guard in guards_table:
        minutes_slept = sum(guards_table[guard])
        if minutes_slept > max_minutes_slept:
            max_minutes_slept = minutes_slept 
            max_id = guard
    return (max_minutes_slept, max_id)


def find_sleepy_minute(guards_table: dict) -> tuple:
    most_sleepy_minute_value = 0
    most_sleepy_id = ''
    for guard in guards_table:
        guard_sleepy_minute_value = max(guards_table[guard])
        if guard_sleepy_minute_value > most_sleepy_minute_value:
            most_sleepy_minute_value = guard_sleepy_minute_value 
            most_sleepy_id = guard

    most_sleepy_minute = guards_table[most_sleepy_id].index(most_sleepy_minute_value)
    return (most_sleepy_minute, most_sleepy_id) 


def solution1(data: list) -> int:
    guards_table = analyze_guards_sleep_pattern(data)
    sleepy_guard = find_sleepy_guard(guards_table)
    minute_index = guards_table[sleepy_guard[1]].index(max(guards_table[sleepy_guard[1]]))
    return int(sleepy_guard[1]) * minute_index


def solution2(data: list) -> int:
    guards_table = analyze_guards_sleep_pattern(data)
    sleep_minute = find_sleepy_minute(guards_table)
    return (sleep_minute[0] * int(sleep_minute[1]))



filename = 'input.txt'
data = import_file(filename)


print(solution1(data))
print(solution2(data))
