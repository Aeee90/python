class Tree:
    def addTree(self, data):
        self.data = data

        if data is -1:
            return self

        left, right = input().split(" ")
        self.left = Tree().addTree(int(left))
        self.right = Tree().addTree(int(right))

        return self

    def search(self, M):
        if self.right.data is -1 and self.left.data is -1:
            return self.data
        elif self.left.data is -1:
            return self.right.search(M)
        elif self.right.data is -1:
            return self.left.search(M)
        else:
            remainder = M%2
            quotient = int(M/2)

            if remainder is 0:
                return self.right.search(quotient)
            else:
                return self.left.search(quotient)


N = int(input())
root = Tree().addTree(1)
root = [1, None, None]
parent = root
for i in range(N):
    temp = parent
    left, right = input().split(" ")
    temp[1] = [int(left), None, None]
    temp[2] = [int(right), None, None]

    parent = temp

print(root.right.left.left.right.data)
M = int(input())
print(root.search(M))
