def read_data(filename: str) -> list:
    with open(filename) as f:
        output = []
        for line in f:
            row = []
            for char in line.rstrip():
                row.append(char)
            output.append(row)
    return output
                

print(read_data('test_input.txt'))
        
        