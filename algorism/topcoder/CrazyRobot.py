import copy


def check_perf(f, *args):
    import time

    n = 10

    t0 = time.time()
    for i in range(n):
        f(*args)
    t1 = time.time()
    return (t1 - t0) / n


class CrazyRobot:
    pointsX = [1, -1, 0, 0]
    pointsY = [0, 0, -1, 1]
    def __init__(self, prob, depth):
        self.depth = depth
        self.prob = list(map(lambda x: x / 100, prob))

    def solution(self, n=-1, x=0, y=0, ret=1, passedPoint = []):

        point = (x, y)
        if point in passedPoint:
            return 0
        else:
            passedPoint.append(point)

        n += 1
        if n >= self.depth:
            del passedPoint[-1]
            return ret

        result = 0
        for i in range(1, 5):
            if self.prob[i-1] != 0:
                result += self.solution(n, x+self.pointsX[i-1], y+self.pointsY[i-1], ret * self.prob[i-1], passedPoint)

        del passedPoint[-1]

        return result

#print(CrazyRobot([25,25,25,25], 1).solution())
#print(CrazyRobot([25,25,25,25], 2).solution())
#print(CrazyRobot([50,0,0,50], 7).solution())
#print(CrazyRobot([50,50,0,0], 14).solution())
print(CrazyRobot([25, 25, 25, 25], 14).solution())
print(check_perf(CrazyRobot([25, 25, 25, 25], 14).solution))