import numpy as np

test_input = 409551
real_input = 409551

array = [3, 7]
index_1 = 0
index_2 = 1

for i in range(test_input + 8):
    suma = array[index_1] + array[index_2]
    if suma >= 10:
        first = suma // 10
        second = suma % 10
        array.append(first)
        array.append(second)
    else:
        array.append(suma)
    dlugosc = len(array)
    index_1 = (1 + array[index_1] + index_1) % dlugosc
    index_2 = (1 + array[index_2] + index_2) % dlugosc

print(array[test_input:test_input+10])

