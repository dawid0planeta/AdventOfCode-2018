from Node import *
import itertools

def read_data(filename: str) -> list:
    with open(filename) as f:
        return [int(i) for i in f.read().split()]

def yield_char(data):
    while len(data) != 0:
        yield data[0] 
        data.pop(0)

def read_node(iterator: 'generator', node_list: list, parent=None) -> list:
    node = Node()
    node.parent = parent
    node.number_of_children = next(iterator, 1)
    node.number_of_meta = next(iterator, 1)
    if node.number_of_children == 0:
        node.meta = [next(iterator) for i in range(node.number_of_meta)]
        node_list.append(node)
        return (iterator, node_list)
    else:
        for _ in itertools.repeat(None, node.number_of_children):
            iterator, node_list = read_node(iterator, node_list, node)
            node.children.append(node_list[-1])
        node.meta = [next(iterator) for i in range(node.number_of_meta)]
        node_list.append(node)
        return (iterator, node_list)

def create_tree(filename: str) -> list:
    iterator = yield_char(read_data(filename))
    iterator, nodes = read_node(iterator, [])
    return nodes


def value(node: Node, total: int) -> int:
    if node.number_of_children == 0:
        total += sum(node.meta)
        return total 
    else:
        for index in node.meta:
            if index-1 >= 0 and index-1 < len(node.children):
                total += value(node.children[index-1], 0)
            else:
                total += 0
        return total 



def solution1(filename: str):
    nodes = create_tree(filename)
    return (sum([item for sublist in [node.meta for node in nodes] for item in sublist]))




def solution2(filename: str):
    nodes = create_tree(filename)
    return value(nodes[-1], 0)

print(solution2('input.txt'))





