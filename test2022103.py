# import requests
import chardet
import requests

cnt = input("请输入你要获取的数量（30，50，100):")
cntINT = int(cnt)
url = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=' + cnt

try:
    if (0 < cntINT <= 100):
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        encoding = chardet.detect(r.content)['encoding']
        r.encoding = encoding
        demo = r.text
    else:
        print("请输入（0-100]的数")
except:
    print("获取数据失败")
