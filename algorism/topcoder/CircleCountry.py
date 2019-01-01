class CircleCountry:
    def solve(self, x1, y1, x2, y2, x=[], y=[], r=[]):
        return len([i for i in range(len(x)) if (r[i]**2-(x1-x[i])**2-(y1-y[i])**2)*(r[i]**2-(x2-x[i])**2-(y2-y[i])**2) < 0])

print(CircleCountry().solve(-5, 1, 5, 1, [0], [0],[2]))
print(CircleCountry().solve(-5, 1, 5, 1, [0,-6,6], [0,1,2],[2,2,2]))
print(CircleCountry().solve(-5, 1, 12, 1, [1,-3,2,5,-4,12,12], [1,-1,2,5,5,1,1], [8,1,2,1,1,1,2]))
print(CircleCountry().solve(2, 3, 13, 2, [-3,2,2,0,-4,12,12,12], [-1,2,3,1,5,1,1,1],[1,3,1,7,1,1,2,3]))