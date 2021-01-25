import csv 
import jieba.analyse 
import re
from  wordcloud import WordCloud
from  matplotlib import pyplot as plt
import pandas as pd

jobs = []
wages = []
welfare = ''
req = ''

#生成单个处理文件
def data_deal():
    
    with open("./data/data.csv",'r') as f:
       reader =  csv.DictReader(f)
       for row in reader:
           jobs.append(row['job'][2:-2]) # 字符串分割是左闭右开,删除['']
           wages.append(row['wages'][2:-2])
           welfare =  welfare + ','+row['welfare'][2:-2]
           req = req + ','+row['req'][2:-2]
    with open("./data/jobs_deal.csv",'w') as f1:
        st = '\n'.join(jobs)
        f1.write(st)
    with open("./data/wages_deal.csv",'w') as f2:
        st = '\n'.join(wages)
        f2.write(st)
    with open("./data/welfare_deal.txt",'w') as f3:
        f3.write(welfare)
    with open("./data/req_deal.txt",'w') as f4:
        f4.write(req)

# 进行关键词提取 
def keyword(path):
    with open (path) as f:
      wordlist = f.read() 
      key = jieba.cut(wordlist)
     # with open('./data/keyword.csv','w') as kw:
     #     kw.write('\n'.join(key))
      jieba.analyse.set_stop_words('./data/english.txt')
      tags =  jieba.analyse.extract_tags(wordlist,topK=53)
     # print(tags)
      with open('./data/f53_chinese_keyword.csv','w') as kw:
          kw.write('\n'.join(tags))

#进行英文单词提取
def english_word(path):
    
    with  open (path,'r') as f:
      wordlist = f.read()
      re.sub(r'\xa0','',wordlist)
      pattern = re.compile('([a-zA-Z]+)')
      englishlist ='\n'.join( pattern.findall(wordlist))
      open('./data/english.txt','w').write(englishlist)

#生成词云
def wordcloud(path):
    with open(path,'r') as f:
        word = f.read()
        wc = WordCloud(max_words = 50,height=600, width=1200)
        wc.generate_from_text(word)
        plt.imshow(wc,interpolation = 'bilinear')
        plt.axis("off")
        wc.to_file('./data/f50_english.png')
#中文词云
def wordcloud(path):
    with open(path,'r') as f:
        word = f.read()
        wc = WordCloud(font_path ='/home/chikai/下载/SourceHanSansCN-Regular.otf', max_words = 50,height=600, width=1200)
        wc.generate_from_text(word)
        plt.imshow(wc,interpolation = 'bilinear')
        plt.axis("off")
        wc.to_file('./data/f50_english.png')
#
#词频排序
#def sort_word(path):
    
#    df = pd.read_csv(path)
# 生成统计图
def pic(path):
      
        my_file=pd.read_csv(path)
        
        plt.plot(my_file['w'],my_file['n'])
        plt.xlabel('saray(10k/month)')
        plt.ylabel('nums')
        plt.show()
        plt.savefig('./data/wages.png')
# 处理薪资
def saray_deal (path):
    with open('./data/wages_num.csv','w') as f:
        key = ['saray','num']
        wr = csv.DictWriter(f,key)
        wr.writeheader()

    with open(path,'r') as f:
        word = csv.DictReader(f,fieldnames=['saray','num'])
        for i in word:
            if '万/月' in i['saray']:
                saray_deal_month(i)
            elif '万/年' in i['saray']:
                saray_deal_year(i)
            elif '千/月' in i['saray']:
                saray_deal_qian(i)

def saray_deal_month (str):
  with open('./data/wages_num.csv','a+') as f:   
    
    pattern = re.compile('([0-9]\.?[0-9]?)')
    sar = pattern.findall(str['saray'])
    m = 0.5 * (float(sar[1]) - float(sar[0]) ) + float(sar[0])
    key = ['saray','num']
    wr = csv.DictWriter(f,key)
    wr.writerow({'saray':m,'num':str['num']})
#    rmb =  {m:str['num']}
#    print(rmb)

def saray_deal_year (str):

 with open('./data/wages_num.csv','a+') as f:
    pattern = re.compile('([0-9]+)')
    sar = pattern.findall(str['saray'])
    m = 0.5 * (float(sar[1]) - float(sar[0]) ) + float(sar[0])
    key = ['saray','num']
    wr = csv.DictWriter(f,key)
    wr.writerow({'saray':m/12,'num':str['num']})
 
def saray_deal_qian (str):

 with open('./data/wages_num.csv','a+') as f:
    pattern = re.compile('([0-9]+)')
    sar = pattern.findall(str['saray'])
    m = 0.5 * (float(sar[1]) - float(sar[0]) ) + float(sar[0])
    key = ['saray','num']
    wr = csv.DictWriter(f,key)
    wr.writerow({'saray':m/10,'num':str['num']})
 
if __name__ == "__main__":
#     saray_deal('./data/wages_count.csv') 
#     pic('./data/wages_over.csv')
#     data_deal()
#     keyword('./data/req_deal.txt')  # 生成前20的关键词
#     english_word('./data/req_deal.txt') #将所有的英文单词提取出来
   wordcloud('./data/f50_english_keyword.csv')

