# bianliang = time.strftime("%Y年%m月%d日 %H点钟%M分%S秒", time.localtime())
# print(bianliang)
# a='1,19,355|1,737,412'
# num=2
# i=1
# for i in range(1,10):
#     if i == num:
#         print(1)
#
#     else:
#        print(2)
#        continue
# time.sleep(3)
# a=['1', '19', '355', '1', '737', '412']

# ss=a.strip('|')
# print(a)
# array=a.split('|')
# arrayN=[]
# for i in range(len(array)):
#   array1=array[i].split(',')
#   arrayN.append(array1)
# print(arrayN)
# for i in range(len(arrayN)):
#     if int(arrayN[i][1]) > 300:
#         print(arrayN[i])
#         print(int(arrayN[i][0]),type(int(arrayN[i][1])))
# a=(49,84,849,684)
# re=[]
# for i in range(2,len(a))[::3]:
#     print(i)
#     print(a[i])
#     if int(a[i-1])>300:
#
#         print(a[i-1], a[i])


# print(re)
import time

# aa1= ["熟练者", "#422", "功师", 422]
# aa1, bb1, cc1, dd1 = "熟练者", "#422", "功师", "#422"
# def aad(aa1, bb1, dd1 ,cc1=0,ss1=0):
#     print(aa1, bb1, dd1 ,cc1,ss1)
# if __name__ == '__main__':
#     print(aad.__defaults__) #查找默认值用的 某某.__defaults__
#     print()
#     aa1 = ["熟练者", "#422", 422,]
#     aad(*aa1)
a = [1, 3, 4, 6, 7, 9]
for i in a[0: 9]:
    print(i)


    def nvQiGong(self, num_parameter, move_seepx, move_seepy, Restart_computer_parameter, aa1, bb1, cc1, dd1, hh1=0.75,
                 hh2=0.75):
        # 女气功 花花
        print(num_parameter, move_seepx, move_seepy, Restart_computer_parameter, aa1, bb1, cc1, dd1, hh1, hh2)
        # 定位坐标[606,401,75,499, 502,481, 460,481, 360,454]
        # self.forxunhuan(460,481)
        for i in range(1, 60):
            time.sleep(0.5)
            num = num_parameter  # num不能是奇数 运行几次
            # move_seep = -0.52  # 57.7   气功4.2  40.8
            # move_seep1= -0.26

            move_seep = -move_seepx
            move_seep1 = -move_seepy
            # move_seep = -0.8  # 57.70
            # move_seep1 = -0.23
            m_button = 'h'
            print(move_seep)
            a_error = 0
            Restart_computer = Restart_computer_parameter  # Restart_computer为0或者1，0关闭电脑，1不关闭电脑
            for j in range(1, 9):
                # print('right开始按下{}次'.format(j))
                # a_error = 0
                if j == 1:
                    time.sleep(0.65)  # 按下两秒
                    dt.press('g')
                    time.sleep(0.65)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.65)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.65)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.5)

                    if self.FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:

                        time.sleep(1.35)
                        self.FuBen_INFO6()
                        dt.keyDown('down')  # ：模拟按键按下 向下
                        time.sleep(0.5 + move_seep1)
                        dt.keyUp('down')  # ：模拟按键松开按键

                        if self.FuBen_INFO() == 1:

                            self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                            time.sleep(1)  # 按下两秒
                            dt.keyDown('right')  # ：模拟按键按下 向下
                            time.sleep(1.5 + move_seep1)
                            dt.keyUp('right')  # ：模拟按键松开按键


                        else:
                            pass

                elif j == 2:
                    dt.press('y')
                    time.sleep(0.5)  # 按下两秒
                    time.sleep(1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    # self.Find_srt("熟练者", "#422", "功师", "#422")
                    dt.press('y')
                    time.sleep(0.65)
                    dt.press('g')
                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    dt.keyDown('right')  # ：模拟按键按下 向下
                    time.sleep(0.7)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    time.sleep(0.75)
                    dt.press('v')
                    time.sleep(0.5)  # 按下两秒
                    self.FuBen_INFO6()
                    dt.press('9')
                    time.sleep(1)
                    self.FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    print('二操作9成功')
                    # time.sleep(1.2)
                    # Caozuolei().FuBen_INFO1()

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键





                elif j == 3:

                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.66 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    time.sleep(0.5)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.5)  # 按下两
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('g')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('d')
                    time.sleep(0.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.5)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    self.FuBen_INFO6()
                    time.sleep(0.5)
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO6
                    self.FuBen_INFO1()
                    self.Find_srt(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('left')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('left')  # ：模拟按键按下
                    time.sleep(3.5 + move_seep)
                    dt.keyUp('left')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.press('y')
                    time.sleep(0.75)
                    dt.press('f')
                    self.FuBen_INFO6(1)
                    dt.press('9')
                    time.sleep(1)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(3.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 4:
                    time.sleep(0.5)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')

                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')

                    time.sleep(0.75)  # 按下两秒
                    dt.press('f')
                    time.sleep(0.7)
                    dt.press('g')

                    time.sleep(2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.65 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    time.sleep(1)
                    self.FuBen_INFO6()
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.7 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(0.05)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.75 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.55 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按
                    dt.press('t')
                    time.sleep(1.5)
                    dt.press('c')

                    time.sleep(0.5)
                    dt.press('d')
                    time.sleep(0.5)
                    self.FuBen_INFO6()
                    time.sleep(0.7)
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                    dt.press('9')
                    time.sleep(0.75)
                    self.FuBen_INFO1()
                    time.sleep(1)
                    time.sleep(0.56)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.95 + move_seep1)
                    dt.keyUp('right')  # ：模拟按键松开按键


                elif j == 6:
                    time.sleep(0.75)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.6)
                    dt.keyDown('right')  # ：模拟按键按下 向下

                    time.sleep(0.8 + move_seep1)

                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.6)
                    dt.keyUp('right')
                    dt.press('g')
                    time.sleep(1)
                    # self.Find_srt(aa1, bb1, cc1, dd1)
                    dt.keyDown('right')  # ：模拟按键按下 向下
                    time.sleep(0.6 + move_seep1)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    self.FuBen_INFO6(c=6)
                    time.sleep(0.1)
                    dt.press('9')
                    time.sleep(0.75)
                    self.FuBen_INFO1()
                    time.sleep(0.5)  # 按下两秒
                    # Caozuolei().FuBen_INFO1()

                    time.sleep(0.75)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按

                    # c=1



                elif j == 7:  # 奇数 反之偶数
                    time.sleep(0.75)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.8 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('g')
                    time.sleep(1)
                    time.sleep(0.7)  # 按下19秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('d')

                    time.sleep(1.2)
                    self.FuBen_INFO1()

                    time.sleep(1.5)

                    # self.forxunhuan(aa1, bb1, cc1, dd1)

                    dt.press('9')
                    time.sleep(0.5)
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键


                elif j == 8:  # 奇数 反之偶数
