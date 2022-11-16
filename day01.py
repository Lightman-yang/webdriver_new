# 04,11,13,19,22,33   01,07,13,17,18,31
c = []


def LiangShuXiangJIA(aa):
    a = aa
    # 两个数据相减
    c = []
    for i in range(0, len(a) - 1):
        b = int(a[i]) + int(a[i + 1])
        c.append(b)
        # print(b)
    return c


def LiangShuXiangJian(aaa):
    # 两个数据相减
    a = aaa
    c = []
    for i in range(len(a) - 1, 0, -1):
        b = int(a[i]) - int(a[i - 1])
        c.append(b)
        # print(b)
    return c


def XiangJianH(aaa):
    # 后减前一个数
    a = aaa
    c = []
    for i in range(len(a) - 1, 0, -1):
        b = int(a[i - 1]) - int(a[0])
        print(int(a[0]), int(a[i - 1]))
        c.append(b)
        # print(b)
    return c


def XiangJiaH(aaa):
    # 第一个数加上后面的数据
    a = aaa
    c = []
    for i in range(len(a) - 1, 0, -1):
        b = int(a[i - 1]) + int(a[0])
        print(int(a[0]), int(a[i - 1]))
        c.append(b)
        # print(b)
    return c


if __name__ == '__main__':
    a = [13, 14, 20, 24, 27, 29]
    zz = LiangShuXiangJian(a)
    zz1 = LiangShuXiangJIA(a)
    zz2 = XiangJianH(a)
    zz3 = XiangJiaH(a)
    print('两数相加', zz1, '两输相减', zz, )
    print('原数据：%r' % a)
    print("减去末尾数据%r" % zz2)
    print('第一个数加后面的数据%r' % zz3)
