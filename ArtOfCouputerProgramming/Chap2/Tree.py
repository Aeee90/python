#Linked Tree left 우선 => 중위 운행
result = []

class Tree:
    NodeValue, LLink, RLink = None
    def __init__(self, value):
        self.NodeValue = value

    def add(self, value):
        if self.LLink is not None:
            self.LLink = value
        elif self.RLink is not None:
            self.RLink = value

        return self

def infix(tree):
    if tree.LLink is not None:
        infix(tree.LLink)

    if tree.RLink is not None:
        infix(tree)

    result.append(tree.NodeValue)

T = Tree("A")
T.add("A")
