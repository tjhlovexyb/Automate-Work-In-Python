
##Originnal_File :  表示需要处理的原文件全路径
##target_File ：表示最终生成的目标文件全路径
##splitStr    :    表示分割符号

def generateTmpFile(Originnal_File,target_File,splitStr):

    #表示当前的处理到第几列
    rownum = 0

    with open(Originnal_File) as csvFile:
        for line in csvFile:
            linesList = line.split(splitStr)
            project = linesList[1]  #自定义需要的列
            sql = linesList[3]      #自定义需要的列

            rownum+=1
            ans=str(rownum)+splitStr+project+splitStr+sql+"\n"
            target_File.write(ans)
            if rownum % 100 ==0:#每一列都打印不现实，但是可以设计每隔100列
                print("now is write ",str(rownum))
        target_File.close()
        print("Work is done!")


def main():
    Original_Csv_File = "/Users/Documents/Codes/Files/original.csv"
    Tmp_Csv_File = "/Users/Documents/Codes/Files/tmp.csv"


    Originnal_File=Original_Csv_File
    target_File=open(Tmp_Csv_File,'a')
    #生成临时文件，作为进一步处理的需要
    generateTmpFile(Originnal_File,target_File,"|")



if __name__ == '__main__':
    main()