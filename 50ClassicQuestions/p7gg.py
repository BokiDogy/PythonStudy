
count=0
temp=str=""
strs=[]
while str!="q":
    str=input(f"请输入第{count + 1}个单词(输入q结束)： ")
    strs.append(str)
    count+=1
print(f"排序前的结果为： {strs}")
print("-"*20+"\n")
for index,value in strs:
    print(f"index:{index}")
    print(f"value:{value}")