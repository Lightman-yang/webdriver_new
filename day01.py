# 04,11,13,19,22,33   01,07,13,17,18,31
c = []


def LiangShuXiangJIA(aa):
    a = aa
    c = []
    for i in range(0, len(a) - 1):
        b = int(a[i]) + int(a[i + 1])
        c.append(b)
        # print(b)
    return c


def LiangShuXiangJian(aaa):
    a = aaa
    c = []
    for i in range(len(a) - 1, 0, -1):
        b = int(a[i]) - int(a[i - 1])
        c.append(b)
        # print(b)
    return c


if __name__ == '__main__':
    a = [13, 14, 20, 24, 27, 29]
    zz = LiangShuXiangJian(a)
    zz1 = LiangShuXiangJIA(a)
    print('两数相加', zz1, '两输相减', zz, )
    print('原数据：04,11,13,19,22,33')
