# -*- coding: utf-8 -*-
import nltk
#nltk.download()
import nltk
newfile = open('.//news.txt')
text = newfile.read()  #读取文件
tokens = nltk.word_tokenize(text)  #分词
tagged = nltk.pos_tag(tokens)  #词性标注
entities = nltk.chunk.ne_chunk(tagged)  #命名实体识别
a1=str(entities) #将文件转换为字符串
file_object = open('.//out.txt', 'w')  
file_object.write(a1)   #写入到文件中
file_object.close( )
print(entities)

"""
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
"""