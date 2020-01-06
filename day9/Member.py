from itertools import repeat
class Member:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left 
        
    
    def remove(self):
        self.right.left = self.left
        self.left.right= self.right

    def n_neighbor(self, dir: bool, n: int):
        curr = self
        if dir == True:
            for _ in repeat(None, n):
                curr = curr.right
        else:
            for _ in repeat(None, n):
                curr = curr.left
        return curr

    