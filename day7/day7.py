from Node import *
import time


def read_data(filename: str) -> list:
    file = open(filename)
    data = []
    for line in file:
        line = line.rstrip()
        data.append([line[5], line[36]])
    return data

def create_tree(data: list) -> list:
    tree = [Node(data[0][0]), Node(data[0][1])]
    tree[0].children.append(tree[1])
    tree[1].parents.append(tree[0])
    for edge in data[1:]:
        parent_index = None
        child_index = None
        for node in tree:
            if node.label == edge[0]:
                parent_index = tree.index(node)
            
            if node.label == edge[1]:
                child_index = tree.index(node)

        if parent_index == None:
            tree.append(Node(edge[0]))
            parent_index = len(tree) - 1

        if child_index == None:
            tree.append(Node(edge[1]))
            child_index = len(tree) - 1

        tree[parent_index].children.append(tree[child_index])
        tree[child_index].parents.append(tree[parent_index])

    return tree


def find_orphan(tree: list) -> int:
    for each in tree:
        if each.is_orphan():
            return each


def get_next(avalible: list, path: str) -> Node:
    min_label = 512
    index = 0
    banned = []
    for each in avalible:
        if each.label in path:
            banned.append(each)
            continue
        for parent in each.parents:
            if parent.label not in path:
                banned.append(each)

    avalible = [item for item in avalible if item not in banned]

    if len(avalible) == 0:
        return Node('DONE')

    for each in avalible:
        if ord(each.label) < min_label:
            min_label = ord(each.label)
            index = avalible.index(each)
    return avalible[index]
    


def create_path(orphan: int, tree: list) -> str:
    path = ''
    while True:
        next = get_next(tree, path).label
        if next == 'DONE':
            break
        path += get_next(tree, path).label

    return path

def solution(filename: str) -> str:
    data = read_data(filename)
    tree = create_tree(data)
    orphan = find_orphan(tree)
    path = create_path(orphan, tree)
    return path




start_time = time.time()
times = []
filename = 'input.txt'
for i in range(1000):
    solution_exe = solution(filename)
    times.append(time.time() - start_time)
    start_time = time.time()

print(str(sum(times)/len(times)))
        



        


