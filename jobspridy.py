import requests
import lxml.etree as et
import re
import os
import csv
from  multiprocessing import Pool
import time

# 设置头部信息
header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

# 获取网址列表
def get_url(url,id):
   
    response = requests.get(url,headers = header)
    print(f"第{id}页请求成功")  
    seletor = et.HTML(response.text)
    js = '/html/body/script[2]/text()'
    web=seletor.xpath(js)[0] #获取的是一个列表的列表, js 是第一个元素 
   
    ze = '.+?"job_href":"(.+?)","job_name' # 正则表达式选取网址信息,括号中间是要获取的部分
    pattern = re.compile(ze)    #编译正则表达式, 得到一个正则对象
    urls = pattern.findall(web) # 查找所有符合的字段
   
    return urls #返回一个urls列表

def get_data(url):
    
    url =  url.replace('\\','') # 首先要处理一下url , 将\\ 替换成空白
    response = requests.get(url,headers = header)
    response.encoding='gbk'   # 重要的一步,根据网站编码设置,否则会乱码


    try:
      with open(r'./data/data.csv','a+') as f : #用这种方法打开文件,不用关闭
        
        seletor = et.HTML(response.text) 
        job = seletor.xpath('//h1/@title')# 选择属性内容
        wages = seletor.xpath("//div[@class='cn']/strong/text()") #选择文本内容
        location = seletor.xpath("//div[@class='cn']/p[@class='msg ltype']/@title")# 注意: 如果里面存在'' 需要用"" 避免语法错误
        
        Welfare = seletor.xpath("//div[@class='t1']/span/text()") # 如果所需多个标签的信息,可以获取该标签名的文本,会返回所有符合的内容
        req = seletor.xpath("//div[@class='bmsg job_msg inbox']/p/text()") # 查找所有 <p> 标签内容                 
        key = ['job','wages','welfare','location','req'] # 设置列表头
        writer = csv.DictWriter(f,key)
        writer.writerow({'job':job,'wages':wages,'welfare':Welfare,'location':location,'req':req}) #以字典的形式写入文件
    
    except Exception:

        print(Exception)
        pass

if __name__ == "__main__" :
    if os.path.exists(r'./data') is False: #如果没有数据文件夹,创建一个
        os.mkdir(r'./data')
   
    with open(r'./data/data.csv','a+') as f: #提前处理好csv 文件的列表头
        key = ['job','wages','welfare','location','req'] # 设置列表头
        writer = csv.DictWriter(f,key) # 将列表头写入文件
        writer.writeheader() #初始化列表 

    for i in range(1,61):
      
       url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,{i}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
       urls = get_url(url,i)
      
       with Pool(15) as p: #运用线程池,多线程获取数据
           p.map(get_data,urls)# map函数的运用
       for m in range(5):
           time.sleep(m)
