# job-java
  爬取了前程无忧网站的 Java 相关职位信息,并进行了数据分析 
  
**数据截止到2021年1月20日**  

  爬取了60页数据,每页50条,一共3000条职位信息  
    
## 职位  

    Java开发工程师       1071  
    Java高级开发工程师    346  
    Java中级开发工程师    105  
    Java工程师           88      
    Java架构师           29  
    Java初级开发工程师    23  
    Java资深开发工程师    21  
    JAVA软件工程师       33  
    Java开发经理         16  
    Java软件开发工程师    15  
    Java开发主管         13  
    Java后台开发工程师    13  
   
   对前20的职位进行统计,并将相似职位进行合并(如忽略java大小写的区别,高级java开发工程师和java高级开发工程师)    
可以看到,对开发工程师的需求最大,高级开发工程师第二,中级第三,但考虑到开发工程师比较笼统,所以参考性不大.  
但是除去开发工程师,根据细分的职位,还是可以看出,中高级开发工程师是主要需求,主管,经理和构架师较少.  
## 职位要求  

**排在前列的中文词语**  

    熟悉
    开发
    经验
    技术
    数据库
    设计
    框架
    优先
    能力
    工作
    负责
    熟练
    系统
    项目
    文档
    以上学历
    相关
    精通
    团队
    编写
    熟练掌握
    良好
    代码
    岗位职责
    使用
    架构
    编程
    沟通
    优化
    模块
    参与
    多线程
    开源
    设计模式
    本科
    计算机相关
    专业
    产品
    分析
    主流
    分布式
    架构设计
    
可以看出 对于技术修饰词有 `熟悉` `熟练` `精通` `熟练掌握` (感觉精通可以忽略), 就是要求 熟,上手就能干活.  
一些常见的硬件要求有: `经验` (要有项目经验)  `技术`(有一定技术)    `以上学历``本科`(学历要求) `编写` `代码``编程`(代码能力)  
`能力` `负责` `团队`  `沟通``参与`则是对工作上的要求,可见团队协作能力很重要  
技术相关的有: `数据库``设计``框架``系统``文档``构架``优化``多线程``设计模式``开源``分布式``架构设计`  
![词云](https://github.com/black-ck/job-java/blob/main/data/f50_chinese.png?raw=true)  

**排在前列的英文词语**  

大多数为技术名词  

    Spring,1873
    JAVA,904
    SQL,886
    Oracle,791
    MySQL,716
    Redis,676
    Linux,623
    J2EE,588
    spring,563
    Web,444
    Mybatis,438
    SpringMVC,435
    MyBatis,429
    HTML,424
    Tomcat,402
    SpringBoot,387
    CSS,384
    Mysql,383
    redis,367
    mysql,367
    Hibernate,356
    JVM,324
    MVC,315
    JavaScript,298
    web,286
    Cloud,265
    SpringCloud,255
    mybatis,254
    linux,248
    Boot,243
    Struts,218
    Maven,205
    oracle,199
    Dubbo,196
    MongoDB,192
    Nginx,190
    Ajax,189
    sql,185
    C,174
    Kafka,173
    IO,161
    JSP,159
    MQ,158
    WEB,158
    Git,155
    Server,154
    Javascript,152
    MySql,149
    Vue,147
    springboot,147
    
   ![英文词云](https://raw.githubusercontent.com/black-ck/job-java/main/data/f50_english.png)




