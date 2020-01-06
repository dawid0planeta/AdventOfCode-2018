def gen():
    while True:
        suma = array[index_1] + array[index_2]
        if suma >= 10:
            first = suma // 10
            second = suma % 10
            yield first
            yield second
            yield None
        else:
            yield suma
            yield None
