# MaoyanMovies
crawler for maoyan movies

本项目主要是应用requests库来爬取猫眼电影的信息。

项目流程如下：

1.用requests访问并解析网页

2.用正则表达式找出源码中的重要内容，并以字典的形式返回

3.将字典转换为json字符串，保存到文本中

4.创建线程池，提升爬虫的效率
