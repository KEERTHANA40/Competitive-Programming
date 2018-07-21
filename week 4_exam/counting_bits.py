def countBits(num):
        res = [0]
        for i in range(1, num + 1):
            res.append((i & 1) + res[i >> 1])
        print(res)

countBits(15)
countBits(16)
countBits(1)
countBits(25)
countBits(5)
countBits(6)	