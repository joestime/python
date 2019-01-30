import jieba

segtence="银河帝国是阿西莫夫的科幻巨作，是科幻小说的巅峰之作"

#全模式
print("--全模式--")
w1=jieba.cut(segtence,cut_all=True)
for item in w1:
    print(item)

print("--精准模式--")
#精准模式
w2=jieba.cut(segtence,cut_all=False)
for item in w2:
    print(item)

#搜索引擎模式
print("--搜索引擎模式--")
w3=jieba.cut_for_search(segtence)
for item in w3:
    print(item)

#默认使用精准模式
print("--默认使用精准模式--")
w4=jieba.cut_for_search(segtence)
for item in w4:
    print(item)

#词性标注
print("--词性标注--")
import jieba.posseg
w5=jieba.posseg.cut(segtence)
for item in w5:
    print(item.word+'---'+item.flag)
#http://qinwenfeng.com/jiebaR/

#自定义词典加载
#jieba.load_userdict("D:/python/dic1.txt")

#更改词频 只能调高词频，不能调低词频
segtence="我喜欢上海东方明珠"
w7 = jieba.cut(segtence)
for item in w7:
    print(item)
print("----")
jieba.suggest_freq("上海东方",True)
w8 = jieba.cut(segtence)
for item in w8:
    print(item)

'''----------------------------'''
import jieba.analyse
segtence="我喜欢上海东方明珠电视塔"
segtence2="阿西莫夫是二十世纪最伟大的科幻小说作家"
segtence3="航拍北方农村大集，上万摊位如蛛网，网友：这才是年味"
#提取关键词
print("提取关键词")
tag=jieba.analyse.extract_tags(segtence,3)
tag2=jieba.analyse.extract_tags(segtence2,2)
tag3=jieba.analyse.extract_tags(segtence3,3)

print(tag)
print(tag2)
print(tag3)
#返回词语的位置
w9=jieba.tokenize(segtence)
for item in w9:
    print(item)
print("-----")
w10=jieba.tokenize(segtence,mode="search")
for item in w10:
    print(item)

#分析《基地》的词频
data=open("C:/Users/joe/PycharmProjects/GetHotspot/jidi.txt").read()
tag=jieba.analyse.extract_tags(data,10)
print(tag)

data2=open("C:/Users/joe/PycharmProjects/GetHotspot/jidi3.txt").read()
tag2=jieba.analyse.extract_tags(data2,10)
print(tag2)

data3=open("C:/Users/joe/PycharmProjects/GetHotspot/santi3.txt").read()
tag3=jieba.analyse.extract_tags(data3,10)
print(tag3)

data4=open("C:/Users/joe/PycharmProjects/GetHotspot/quanji.txt").read()
tag4=jieba.analyse.extract_tags(data4,10)
print(tag4)