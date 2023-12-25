import time


def run():
    print('打印')


def timedaojishi():
    # for i in range(330,0,-1):
    for i in range(190, 0, -1):
        time.sleep(1)
        if i > 180:
            pass
        elif i <= 180:
            if i % 2 == 0:
                print("%.f偶数" % i)

            else:
                print("%.f奇数" % i)
                break
        else:
            print("查询%.f" % i)


if __name__ == '__main__':
    timedaojishi()
