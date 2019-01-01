import decimal as deci
pi = deci.Decimal(3.1415926535897932384626433832795028841971)

import math

pi = math.pi

with open("./A-small-practice1.in", 'r') as input:
    with open("./A-small-result.txt", 'w') as ouput:

        testCount = int(input.readline())

        for i in range(1,testCount+1):
            temp = input.readline().split(" ")
            N = int(temp[0])
            K = int(temp[1])

            arr = []
            for j in range(N):
                temp = input.readline().split(" ")
                arr.append([int(temp[0]), int(temp[1])])

            arr.sort(reverse= True)

            print(min(arr))

            result =0
            max = 0

            a = range(N-K+1)
            if len(a) is 0:
                a = [0]

            for n in a:
                rd = arr[n][0]
                hd = arr[n][1]

                print("{} : {} ".format(rd, hd))

                result = pi*rd*rd
                print(range(n, n+K))
                for k in range(n, n+K):
                    rd = arr[k][0]
                    hd = arr[k][1]

                    result += 2*pi*rd*hd

                if result > max:
                    max = result
                    print(max)

            print("Case #{} : {:.9f}".format(i, max))
            ouput.write("Case #{}: {:.9f} \n".format(i, max))

