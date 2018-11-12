# list
a = ["hello,word"]
print(a[0])
a[0] = 2
print(a)

# tuple 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
b = ("my","world")
print(b[0])

# dictionary
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
print(dict)
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(tinydict)

for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j), end=" ")
    print()

for i in range(1,10):
    for j in range(1,10-i+1):
        print(str(10-i)+"*"+str(j)+"="+str((10-i)*j),end=" ")
    print()