import sys

input = '409551'
test_input = '409551'
array = '37'
index_1 = 0
index_2 = 1

while True:
    suma = str(int(array[index_1]) + int(array[index_2]))
    array += suma
    dlugosc = len(array)
    index_1 = (1 + int(array[index_1]) + index_1) % dlugosc
    index_2 = (1 + int(array[index_2]) + index_2) % dlugosc
    if test_input in array[-8:]:
        print(dlugosc - 6)
        break
    

array = '37'
index_1 = 0
index_2 = 1


while True:
    suma = str(int(array[index_1]) + int(array[index_2]))
    array += suma
    dlugosc = len(array)
    index_1 = (1 + int(array[index_1]) + index_1) % dlugosc
    index_2 = (1 + int(array[index_2]) + index_2) % dlugosc
    if input in array[-7:]:
        print(dlugosc - 6)
        break
    

