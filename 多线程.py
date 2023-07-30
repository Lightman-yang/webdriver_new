# coding:utf-8

import time  # 导入时间休眠函数
from threading import Thread  # 导入线程函数

xxyy = ['x', 'y', 'x', 'y']


class MYthreading():

    def task1(self,AA):  # 定义任务1
        for x in range(1, 10000):  # 遍历数组n里的x
            xxyy[0:2] = x + 1, x + 10
            time.sleep(5)
            print((x + AA))
            n=x+AA
            print(n)

    def task2(self,NN):  # 定义任务2

        for i in range(2, 20000):  # 遍历list1里的信息
            xxyy[-2:] = i + 2, i + 20
            time.sleep(5)
            print(NN)

    def main(self):  # 定义main函数
        pass


if __name__ == '__main__':
    a=[10,20,30]

    t1 = Thread(target=MYthreading().task1,args=(30,))  # 定义线程t1，线程任务为调用task1函数，task1函数的参数是6
    t2 = Thread(target=MYthreading().task2,args=(20,))  # 定义线程t2，线程任务为调用task2函数，task2函数无参数
    t1.start()  # 开始运行t1线程
    t2.start()  # 开始运行t2线程
