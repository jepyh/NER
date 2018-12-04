# DEMO来自于https://blog.csdn.net/babydx/article/details/77836810#commentBox
# Stanford Named Entity Recognizer (NER)是斯坦福大学自然语言研究小组发布的成果之一，主页是：
# http://nlp.stanford.edu/software/CRF-NER.shtml。Stanford NER 是一个Java实现的命名实体识别（以下简称NER）)程序。
# NER将文本中的实体按类标记出来，例如人名，公司名，地区，基因和蛋白质的名字等。
# NER基于一个训练而得的Model（模型可识别出 Time, Location, Organization, Person, Money, Percent, Date）七类属性，
# 其用于训练的数据即大量人工标记好的文本，理论上用于训练的数据量越大，NER的识别效果就越好。
# 因为原始的NER是基于java实现的，所以在使用Python编程之前，要确保自己电脑上已经安装了jar1.8的环境（否则会报关于Socket的错误）。
# 然后我们使用Pyner使用python语言实现命名实体识别。下载地址为：https://github.com/dat/pyner
# 安装Pyner:解压下载的Pyner，命令行中将工作目录切换到Pyner文件夹下， 输入命令 :python setup.py install 完成安装.
# 接下来，还需要下载StanfordNER工具包，下载地址为：http://nlp.stanford.edu/software/stanford-ner-2014-01-04.zip，
# 然后在解压后的目录打开cmd命令窗体，执行，
# java -mx1000m -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer -loadClassifier classifiers/english.muc.7class.distsim.crf.ser.gz -port 8080 -outputFormat inlineXML
# ，直到结果为：Loading classifier from classifiers/english.muc.7class.distsim.crf.ser.gz ... done [1.2 sec].
# 以上操作是因为斯坦福的命名实体识别是基于java的socket写的，所以必要保证有一个窗题与我们执行的命令通信。关于java的socket编程，
# 可以参考以下文章：http://www.cnblogs.com/rond/p/3565113.html

import ner
import sys
import nltk
import importlib
importlib.reload(sys)
newfile = open('.//news.txt')
text = newfile.read()

tagger = ner.SocketNER(host='localhost', port=8080)#socket编程

print(text)
#针对一些特别的地名敏感，词典较小
result = tagger.get_entities(text)   #stanford实现NER
print(2)
a1=str(result)
file_object = open('.//outfile.txt', 'w')
file_object.write(a1)
file_object.close( )
print(result)
