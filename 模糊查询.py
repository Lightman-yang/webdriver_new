#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/5/25 18:42

from fuzzywuzzy import fuzz
q=1

while q<2:
     z = input("abc:")
     x="新标签页 n"
     asdf=fuzz.ratio(str(z),str(x))
     print(asdf)
