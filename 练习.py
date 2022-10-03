import os

b = "子"
a = '{}曰：学而实习之，不亦说乎；{}又曰：友朋自远方来，不亦君子呼！{}'.format(b, b, b)

print(a)
print('%s曰：学而实习之，不亦说乎；%s又曰：友朋自远方来，不亦君子呼！%s' % (b, b, b))

print()

# a=os.system('dir')
# print(a)
# b=os.system('mkdir zzz')
# print(b)
#
# a=os.system('dir')
# print(a)
import random

n = 2
while n > 0:
    z = int(input("输入一个数据： "))
    b = random.randint(1, 50)
    print(b)
    i = 0
    for i in range(i, z):

        if i == 0:
            continue
        else:
            print('第{}次'.format(i))
        if i == z - 1:
            break
        else:
            pass

            j = 0
            for j in range(1, i + 1):
                print('*', end='|')  # end=" "
