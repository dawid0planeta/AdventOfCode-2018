from collections import Counter

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

    for line in data:
        if does_repeat_x_times(line, 2):
            count_2 += 1
        if does_repeat_x_times(line, 3):
            count_3 += 1
    return count_2*count_3

def file_to_list(data):
    list_data = []
    for line in data:
        list_data.append(line.strip())
    return list_data


def check_similarity(str1: str, str2: str) -> bool:
    off_by = 0
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            off_by += 1
        if off_by > 1:
            return False

    return True

def find_similar(data) -> tuple:
    data = file_to_list(data)
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


data = open("input.txt")
print(checksum(data))

data = open("input.txt")
similar = find_similar(data)
print(strip_difference(similar[0], similar[1]))

