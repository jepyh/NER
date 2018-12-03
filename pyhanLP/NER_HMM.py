#目前本系统默认支持人名（nr），地名（ns），机构名（nt）三种命名实体的识别
#基于HMM角色标注的命名实体识别（速度快）
#    中国人名识别、音译人名识别、日本人名识别、地名识别、实体机构名识别

from pyhanlp import *

ChineseNameSentences = [
        "签约仪式前，秦光荣、李纪恒、仇和等一同会见了参加签约的企业家。",
        "武大靖创世界纪录夺冠，中国代表团平昌首金",
        "区长庄木弟新年致辞",
        "朱立伦：两岸都希望共创双赢 习朱历史会晤在即",
        "陕西首富吴一坚被带走 与令计划妻子有交集",
        "据美国之音电台网站4月28日报道，8岁的凯瑟琳·克罗尔（凤甫娟）和很多华裔美国小朋友一样，小小年纪就开始学小提琴了。她的妈妈是位虎妈么？",
        "凯瑟琳和露西（庐瑞媛），跟她们的哥哥们有一些不同。",
        "王国强、高峰、汪洋、张朝阳光着头、韩寒、小四",
        "张浩和胡健康复员回家了",
        "王总和小丽结婚了",
        "编剧邵钧林和稽道青说",
        "这里有关天培的有关事迹",
        "龚学平等领导说,邓颖超生前杜绝超生",]

TranslatedNameSentences = [
     "一桶冰水当头倒下，微软的比尔盖茨、Facebook的扎克伯格跟桑德博格、亚马逊的贝索斯、苹果的库克全都不惜湿身入镜，这些硅谷的科技人，飞蛾扑火似地牺牲演出，其实全为了慈善。",
     "世界上最长的姓名是简森·乔伊·亚历山大·比基·卡利斯勒·达夫·埃利奥特·福克斯·伊维鲁莫·马尔尼·梅尔斯·帕特森·汤普森·华莱士·普雷斯顿。",]

JeoaneseNameSentences = [
        "北川景子参演了林诣彬导演的《速度与激情3》",
        "林志玲亮相网友:确定不是波多野结衣？",
        "龟山千广和近藤公园在龟山公园里喝酒赏花",]

PlaceSentences = ["蓝翔给宁夏固原市彭阳县红河镇黑牛沟村捐赠了挖掘机"]

OrganizationSentences = [
        "我在上海林原科技有限公司兼职工作，",
        "我经常在台川喜宴餐厅吃饭，",
        "偶尔去开元地中海影城看电影。",]

def demo_chinese_name_recognition(sentences):
    segment = HanLP.newSegment().enableNameRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)

def demo_translated_name_recognition(sentences): 
    segment = HanLP.newSegment().enableTranslatedNameRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)

def demo_japanese_name_recognition(sentences):
    segment = HanLP.newSegment().enableJapaneseNameRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)

def demo_place_recognition(sentences):
    segment = HanLP.newSegment().enablePlaceRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)

def demo_organization_recognition(sentences):
    segment = HanLP.newSegment().enableOrganizationRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)

if __name__ == "__main__":
    print("中国人名识别")
    demo_chinese_name_recognition(ChineseNameSentences)
    print("音译人名识别")
    demo_translated_name_recognition(TranslatedNameSentences)
    print("日本人名识别")
    demo_japanese_name_recognition(JeoaneseNameSentences)
    print("地名识别")
    demo_place_recognition(PlaceSentences)
    print("机构名识别")
    demo_organization_recognition(OrganizationSentences)
