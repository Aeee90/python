#Stack
class Stack:
    top = -1
    data = []

    def push(self, item):
        self.data.append(item)
        self.top += 1

    def pop(self):

        if self.top < 0:
            print("UNDERFLOW")
            return

        result =  self.data[self.top]
        self.top -= 1

        return result

#Queeu (일정 데이터가 push되면, 일정 데이터는 소비된다고 가정)
class Queue:
    F = -1
    R = -1
    M = 10
    data = []

    def push(self, item):
        self.R += 1
        if self.R is self.M:
            self.R = 0

        if self.R is self.F:
            print("OVERFLOW")
            return

        self.data.append(item)

    def pop(self):
        if self.F is self.M:
            self.F = -1
        self.F += 1

        if self.F is self.R:
            print("UNDERFLOW")
            return

        return self.data[self.F]

#class Deque:
