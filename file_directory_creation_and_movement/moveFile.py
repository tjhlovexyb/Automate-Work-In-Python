
"""
实现内容：
将符合某个文件名的文件移动到对应的文件目录当中去
"""
import os
import shutil

#创建文件夹
def makeDir(base_path,fileName):

    path=base_path+'/'+fileName
    isExits=os.path.exists(path)
    if not isExits:
        os.makedirs(path)

#获得文件名
def getFileNamesInADir(path):
    names=[]
    for root,dirs,files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[-1] =='.pdf':
                names.append(file)
    return names

#获取创新文件夹名
def getDirNames(path):
    dirNames=set()
    for root,dirs,files in os.walk(path):
        for file in files:
            #判断要创建的文件名是否是在【】当中 此处可自定义修改
            res = 1 if '【' in file and '】' in file else 0
            if res == 1:
                dirName = file.split('【')[1].split('】')[0]
                dirNames.add(dirName)
            else:
                pass
    return dirNames


#移动文件
def moveFileToDir(filename,base_path,dirName):
    path = base_path+'/'+dirName
    srcFile = base_path+'/'+filename
    dstFile = base_path+'/'+dirName+'/'+filename
    res = 1 if os.path.exists(path) else 0
    if res == 1 :
        if dirName in filename:
            shutil.move(srcFile,dstFile)
            print("move %s -> %s" %(srcFile,dstFile))
        else:
            pass
    else:
        makeDir(base_path,filename)


def main():
    base_path = 'G:/WeChatDownload/码农有道 - pdf'

    #获取文件名
    filesNames = getFileNamesInADir(base_path)
    # print(names)

    #获取要创建的文件夹名
    dirNames = getDirNames(base_path)
    # print(dirNames)
    # print('创建文件夹开始。。。。。')
    # for name in dirNames:
    #     makeDir(base_path,name)
    # print('创建文件夹结束!')
    print("移动开始！")
    for filesName in filesNames:
        for dirName in dirNames:
            moveFileToDir(filesName,base_path,dirName)
    print("移动结束！")

if __name__ == '__main__':
    main()