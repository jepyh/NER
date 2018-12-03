#基于线性模型的命名实体识别（精度高）
#   感知机命名实体识别、CRF命名实体识别


from pyhanlp import *

def demo_perceptron_lexical_analyzer():
    """ 基于感知机序列标注的词法分析器，默认模型训练自1998人民日报语料1月份。欢迎在更大的语料库上训练，以得到更好的效果。
        无论在何种语料上训练，都完全支持简繁全半角和大小写。
    >>> demo_perceptron_lexical_analyzer()
    [上海/ns 华安/nz 工业/n （/w 集团/n ）/w 公司/n]/nt 董事长/n 谭旭光/nr 和/c 秘书/n
        胡花蕊/nr 来到/v [美国/ns 纽约/ns 现代/t 艺术/n 博物馆/n]/ns 参观/v
    [微软/nt 公司/n]/nt 於/p 1975年/t 由/p 比爾·蓋茲/n 和/c 保羅·艾倫/nr 創立/v ，/w
        18年/t 啟動/v 以/p 智慧/n 雲端/n 、/w 前端/f 為/v 導向/n 的/u 大/a 改組/vn 。/w
    总统/n 普京/nr 与/c 特朗/b 普通/a 电话/n 讨论/v 太空/s 探索/vn 技术/n 公司/n
    总统/n 普京/nr 与/c 特朗普/nr 通/v 电话/n 讨论/v [太空/s 探索/vn 技术/n 公司/n]/nt
    主席/n 和/c 特朗普/nr 通/v 电话/n
    我/r 在/p 浙江/ns 金华/nr 出生/v
    我/r 在/p 四川/ns 金华/ns 出生/v ，/w 我/r 的/u 名字/n 叫/v 金华/nr
    空格 /d
    /v
    /n 统统/d 都/d 不要/d
    """
    PerceptronLexicalAnalyzer = JClass("com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer")
    analyzer = PerceptronLexicalAnalyzer()

    print(analyzer.analyze("上海华安工业（集团）公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观"))
    print(analyzer.analyze("微软公司於1975年由比爾·蓋茲和保羅·艾倫創立，18年啟動以智慧雲端、前端為導向的大改組。"))

    # 任何模型总会有失误，特别是98年这种陈旧的语料库
    print(analyzer.analyze("总统普京与特朗普通电话讨论太空探索技术公司"))
    # 支持在线学习
    analyzer.learn("与/c 特朗普/nr 通/v 电话/n 讨论/v [太空/s 探索/vn 技术/n 公司/n]/nt")
    # 学习到新知识
    print(analyzer.analyze("总统普京与特朗普通电话讨论太空探索技术公司"))
    # 还可以举一反三
    print(analyzer.analyze("主席和特朗普通电话"))

    # 知识的泛化不是死板的规则，而是比较灵活的统计信息
    print(analyzer.analyze("我在浙江金华出生"))
    analyzer.learn("在/p 浙江/ns 金华/ns 出生/v")
    print(analyzer.analyze("我在四川金华出生，我的名字叫金华"))

    # 请用户按需执行对空格制表符等的预处理，只有你最清楚自己的文本中都有些什么奇怪的东西
    print(analyzer.analyze("空格 \t\n\r\f&nbsp;统统都不要"
        .replace("\\s+", "")    # 去除所有空白符
        .replace("&nbsp;", "")  # 如果一些文本中含有html控制符
))

def demo_NLP_segment():
    """ NLP分词，更精准的中文分词、词性标注与命名实体识别
        标注集请查阅 https://github.com/hankcs/HanLP/blob/master/data/dictionary/other/TagPKU98.csv
        或者干脆调用 Sentence#translateLabels() 转为中文
    >>> demo_NLP_segment()
    [我/r, 新造/v, 一个/m, 词/n, 叫/v, 幻想乡/ns, 你/r, 能/v, 识别/v, 并/c, 正确/ad, 标注/v, 词性/n, 吗/y, ？/w]
    我/代词 的/助词 希望/名词 是/动词 希望/动词 张晚霞/人名 的/助词 背影/名词 被/介词 晚霞/名词 映/动词 红/形容词
    支援/v 臺灣/ns 正體/n 香港/ns 繁體/n ：/w [微软/nt 公司/n]/nt 於/p 1975年/t 由/p 比爾·蓋茲/n 和/c 保羅·艾倫/nr 創立/v 。/w
    """
    NLPTokenizer = JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")
    print(NLPTokenizer.segment("我新造一个词叫幻想乡你能识别并正确标注词性吗？"))  # “正确”是副形词。
    # 注意观察下面两个“希望”的词性、两个“晚霞”的词性
    print(NLPTokenizer.analyze("我的希望是希望张晚霞的背影被晚霞映红").translateLabels())
    print(NLPTokenizer.analyze("支援臺灣正體香港繁體：微软公司於1975年由比爾·蓋茲和保羅·艾倫創立。"))


if __name__ == "__main__":

    
    print("感知机命名实体识别")
    demo_perceptron_lexical_analyzer()
    print("CRF命名实体识别")
    demo_NLP_segment()
