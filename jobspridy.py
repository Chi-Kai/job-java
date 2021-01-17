import requests
from bs4 import BeautifulSoup as bs
import lxml.etree as et
import re
import os
import csv
from  multiprocessing import Pool


header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

def get_url(url,id):
   
    response = requests.get(url,headers = header)
    print(f"第{id}页请求成功")
    seletor = et.HTML(response.text)
    js = '/html/body/script[2]/text()'
    web=seletor.xpath(js)[0]
   
    ze = '.+?"job_href":"(.+?)","job_name'
    pattern = re.compile(ze)
    urls = pattern.findall(web)
   
    return urls

def get_data(url):
    
    url =  url.replace('\\','')
    response = requests.get(url,headers= header)
    response.encoding='gbk'   
    item={}
    key = ['job','wages','welfare','location','req']

    try:
      with open(r'./data/data.csv','a+') as f :
        
        seletor = et.HTML(response.text)
        job = seletor.xpath('//h1/@title')
        wages = seletor.xpath("//div[@class='cn']/strong/text()")
        location = seletor.xpath("//div[@class='cn']/p[@class='msg ltype']/@title")
      # Degree   
        
        Welfare = seletor.xpath("//div[@class='t1']/span/text()")
        req = seletor.xpath("//div[@class='bmsg job_msg inbox']/p/text()") # 查找所有 <p> 标签内容                 
        writer = csv.DictWriter(f,key)
        writer.writeheader()
        writer.writerow({'job':job,'wages':wages,'welfare':Welfare,'location':location,'req':req})


      #  item['job'] = job
      #  item['wages']=wages
      #  item['welfare'] = Welfare
      #  item['location']=location
      #  item['req'] = req
    
    except Exception:

        print(Exception)
        pass

if __name__ == "__main__" :
    if os.path.exists(r'./data') is False:
        os.mkdir(r'./data')
    for i in range(1,61):
       url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,{i}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
       urls = get_url(url,i)
      #print(
       with Pool(10) as p:
           p.map(get_data,urls)
