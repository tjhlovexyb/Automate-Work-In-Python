
"""
测试文件
"""

import os
# 获取创新文件夹名
def getDirNames(path):
    dirNames =[]
    for root ,dirs ,files in os.walk(path):
        for file in files:

            if os.path.splitext(file)[-1] =='.pdf':
                dirNames.append(file)

def main():
    base_path = 'G:/WeChatDownload/码农有道 - pdf'
    testName = "2018-10-28 【数据结构与算法】一些常用的算法技巧总结.pdf"#目标获得【】中的文字
    testBadName = "[码农有道] - 2018-11-26 完全整理 - 365篇高质技术文章目录整理，每天一点收获.pdf"

    #dirName=testBadName.split('【')[1].split('】')[0]
    res = 1 if '【' in testBadName and '】' in testBadName else 0
    print(res)

if __name__ == '__main__':
    main()