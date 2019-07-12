

def readFile(file_path,mode):
    return open(file_path,mode)

def getSetAndList(file_readed,fileName):
    #获取project 和 sql的去重结果
    num = 0
    targetSet=set()
    for line in file_readed:
        li = line.split("|")
        boldResult = li[1]+"|"+li[2]
        num +=1
        if num == 1 :
            continue
        else:
            targetSet.add(boldResult)
    print("targetSet"+fileName+"len is :",len(targetSet))

    #store Set result to List
    targetList =[]
    while(len(targetSet)!=0):
        pas = targetSet.pop()
        targetList.append(pas)
    print("tagetList "+fileName+"len is :",len(targetList))

    file_readed.close()
    return targetList


def getShimSet(file_readed,filename):
    targetSet=set()
    for line in file_readed:

        linesList = line.split("|")
        project = linesList[1]
        targetSet.add(project)
    print("targetShimSet "+filename+"len is :",len(targetSet))
    file_readed.close()
    return targetSet

def finalFile(shimSet,targetList,finalFile):


    rowNum=0
    while(len(shimSet) !=0 ):
        p = shimSet.pop()
        for i in targetList:
            if i.split("|")[0] == p:
                #print("match"+p+" "+ i)
                rowNum+=1
                fin = str(rowNum)+"|"+i
                finalFile.write(fin)
                if rowNum%100 == 0:
                    print("now is writing the ",rowNum,"!")

    finalFile.close()
    print("work is done!")


def main():
    Tmp_Csv_File ="/Users/tengting.xu/Documents/Codes/Files/tmp.csv"
    finalCSV = "/Users/tengting.xu/Documents/Codes/Files/Final.csv"

    tmp=readFile(Tmp_Csv_File,'r')
    finalPath = readFile(finalCSV,'a')

    pseList = getSetAndList(tmp,"Tmp_Csv_File")

    tmp = readFile(Tmp_Csv_File, 'r')
    pSet = getShimSet(tmp,"Tmp_Csv_File")

    finalFile(pSet,pseList,finalPath)



if __name__ == '__main__':
    main()






