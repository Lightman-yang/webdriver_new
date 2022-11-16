#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/10/19 10:29
import os
from git.remote import Repo
# 创建本地存储地址
download_path=os.path.join('jason','NB')
# 从远程仓库下载代码
Repo.clone_from('https://github.com/Lightman-yang/pycharm.git',to_path=download_path,branch='master')