list1=[]
list2=[1,2,3,4]
list3=[1,2,3,"a","b","c",True]
list4=[1,2,3,"a",["h","e","l"]]





# print(list4[4][0])
# print(list2[0:2])
# print(list2[0:])
# print(list2[0:-1])
print("---------------------------")

# for  i in list2:
#     print(i)
#
#
# for  i in  enumerate(list2):		#输出列表的索引和值
#     print(i)
# print(len(list2))                                    #[不知道结果]
# list2.insert(0,'老大')  #插入
# print(list2)
# list2.append(5)  #追加
# print(list2)
# list2.extend(list3)  # list2 和 list3拼接
# print(list2)
# list5=list2
# print(id(list5),id(list2))		#id值一样
# list6=list2.copy();
# print(id(list6),id(list2))		#id值不一样
# list7=[1,2,3,4]
# list7[2]=33
# print(list7)
# set1={1,"a",("a","b")}
# # set2={1,"2",[1,2,3]} 非法
# set2={1,"a","b",3}
# print(set2)
# set2.discard("A")
# set2.clear()
# print(set2)
set2={1,"a","b",1}
set2.add("a")
print(set2)

# a=1
# print(a)
# print(type(a));

a2="我"
a3="想你"
# 问题：不换行
print(a2,end="")
print(a3)

# print(a2,a3)