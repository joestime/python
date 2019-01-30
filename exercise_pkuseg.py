import pkuseg
from collections import Counter


content = []
with open("C:/Users/joe/PycharmProjects/GetHotspot/jidi.txt") as f:
    content = f.read()

seg=pkuseg.pkuseg()
text=seg.cut(content)

stopwords=[]

with open("C:/Users/joe/PycharmProjects/GetHotspot/stopkeywords.txt") as f:
    stopwords=f.read()

new_text=[]

for w in text:
    if w not in stopwords:
        new_text.append(w)

counter=Counter(new_text)
print(counter.most_common(20))