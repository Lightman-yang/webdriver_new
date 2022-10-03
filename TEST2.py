class YangLei1:
    def NumberInput():
        try:
            a = int(input("输入一个数： "))

            return a

        except  Exception as e:
            print("请输入正确的数据！")
            i = YangLei1.NumberInput()
        return i

    def NumberFloatInput():
        try:
            b = float(input("输入一个半分比： "))
            return b

        except  Exception as e:
            print("请输入正确的数据百分比！")
            ii = YangLei1.NumberFloatInput()
        return ii

    def NumberInputnum():
        try:
            c = int(input("输入叠加多少次： "))
            return c
        except Exception as e:
            print("请输入正确的叠加测试！ ")
            iii = YangLei1.NumberInputnum()
        return iii


if __name__ == '__main__':
    aa = YangLei1.NumberInput()
    ab = YangLei1.NumberFloatInput()
    ad = YangLei1.NumberInputnum()
    num = (aa * ab) + aa

    # '%.2f' % num  2f为保存两位小数
    print("股市一个板的涨停金额为： ", ('%.2f' % num))

# for i in  range(0,c):
# #      a *= b
# # print(a)
