from collections import Counter

def read_file(filename):
    file_data = open(filename)
    data = list(map(lambda line: line.strip(), file_data)) 
    return data


def count_letters(line: str) -> Counter:
    return Counter(line)


def does_repeat_x_times(line: str, x: int) -> bool:
    letter_count = count_letters(line)
    for letter in letter_count:
        if letter_count[letter] == x:
            return True
    return False

def checksum(data) -> int:
    count_2 = 0
    count_3 = 0

    letter_count_map = list(map(lambda line: count_letters(line), data))
    count_2_map = list(filter(lambda line: does_repeat_x_times(line, 2), letter_count_map))
    count_3_map = list(filter(lambda line: does_repeat_x_times(line, 3), letter_count_map))
    return len(count_2_map) * len(count_3_map)


def check_similarity(str1: str, str2: str) -> bool:
    off_by = 0
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            off_by += 1
        if off_by > 1:
            return False

    return True


def find_similar(data) -> tuple:
    size = len(data)
    for first_index in range(size):
        for second_index in range(first_index + 1, size):
            if check_similarity(data[first_index], data[second_index]):
                return (data[first_index], data[second_index], first_index, second_index)


def strip_difference(str1: str, str2: str) -> str:
    result = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            result += str1[i]
    return result


filename = 'input.txt'
data = read_file(filename)
print(checksum(data))
similar = find_similar(data)
print(strip_difference(similar[0], similar[1]))

