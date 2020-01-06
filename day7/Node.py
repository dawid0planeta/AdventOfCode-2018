class Node:
    def __init__(self, label):
        self.label = label
        self.parents = []
        self.children = []

#    def get_best_child(self):
#        for child in self.children:
#            self.children_scores.append(ord(child.label))
#        best_child_index = self.children_scores.index(min(self.children_scores))
#        return self.children[best_child_index] 


    def is_orphan(self) -> bool:
        if len(self.parents) == 0:
            return True
        else:
            return False
