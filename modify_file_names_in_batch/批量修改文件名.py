#本次实践批量修改某个文件夹的文件名
#命名格式为 文件上一级目录+文件名

import os
path=input('请输入文件路径(结尾加上\)：')

#获取目录名
listName = path.split('\\')[-2]
print(listName)
#批量命名
#获取该目录下所有文件，存入列表中

index = 0
f=os.listdir(path)

for file in f:
    #获取旧的文件路径+文件名（注意必须是全路径名哦！）
    oldName = path+f[index]

    #如果要按需修改，只要修改此部分的逻辑判断就行了

    #设定新的文件名，这里也要完全绝对路径，而不是单一的文件名命名
    #因为os.rename(oldName,newName)方法要求的就是全路径名的互换
    #初学者容易误会就是oldName,newName只是文件名，其实这里必须就是全路径才行。
    if '_' in oldName.split('\\')[-1]:
        newName =path+listName+'_'+oldName.split('_')[-1]
    else:
        newName =path+''+listName+'_'+f[index]
    #print(newName+'\n')
    os.rename(oldName,newName)
    index += 1

#中间无异常，输出成功
print('SUCCESS!')