def read_data(filename: str) -> list:
    with open(filename, 'r') as f:
        return [item.strip() for item in list(f.read().strip())]


def solution(data: list) -> int:
    iterator = 0
    while iterator < len(data)-1:
        if abs(ord(data[iterator+1]) - ord(data[iterator])) == 32:
            data.pop(iterator + 1)
            data.pop(iterator)
            iterator -= 1
            if iterator < 0:
                iterator = 0
        else:
            iterator += 1
    return len(data) 

def solution2(data) -> int:
    smallest = solution(data)
    for each in range(65, 91):
        length = solution([a for a in data if chr(each) != a and chr(each + 32) != a])
        if length < smallest:
            smallest = length
    return smallest

filename = 'input.txt'
data = read_data(filename)
print(solution(data))
data = read_data(filename)
print(solution2(data))

