import random

def createData():
    data = []
    for i in range(40):
        data.append(random.randint(10,69))
    return data

def findBiggestNumber(data):
    temp = data[0]
    for i in data:
        if (i >= temp):
            temp = i
    return temp

def findSmallestNumber(data):
    temp = data[0]
    for i in data:
        if (i <= temp):
            temp = i
    return temp

def sortList(data):
    list = []
    for i in range (10, 69, 10): # 도수 범위 나누는 for문
        temp = 0
        for j in range(40):
            if (data[j] >= i and data[j] <= i+9):
                temp += 1
        list.append(temp)
    return list

def drawTable(data):
    biggestNum = findBiggestNumber(data)  # 자료 중 가장 큰 수
    smallestNum = findSmallestNumber(data)  # 자료 중 가장 작은 수

    gapOfClass = 10  #계급 간격  ->  그냥 10으로 고정하자...!!    // (biggestNum - smallestNum) / len(data)
    bottomOfClass = 9.5  #  계급의 하한  ->  그냥 9.5로 고정하자??  // smallestNum - 0.5

    numberBetweenEachGap = sortList(data)

    print('-------------------------------------------------------')

    print("{0:^9} | {1:^9} | {2:^9} | {3:^7} |{4:^10}".format("계급 범위","도수의 갯수","그냥 뭐시기","누적 뭐시기","계급값"))  #출력
    temp = 0
    accumulate = 0
    for i in range(gapOfClass, biggestNum, gapOfClass):  # 10,68쯔음,10씩증가
        accumulate += numberBetweenEachGap[temp]/40
        print(f"{i-0.5:^5} ~ {i+gapOfClass-0.5:^5} | {numberBetweenEachGap[temp]:^14} | {numberBetweenEachGap[temp]/40:^14.3f} | {accumulate:^12.3f} |    {i+(gapOfClass/2)-0.5}")
        temp += 1
    return 0

def drawHistogram(data):
    numberBetweenEachGap = sortList(data)
    drawHistographElement = []
    biggestNumber = findBiggestNumber(numberBetweenEachGap)
    row = 0
    for i in range(10,70,10):
        print("{0}({1}) : {2}".format(i+4.5, numberBetweenEachGap[i//10-1],'* '*numberBetweenEachGap[i//10-1]))
        templist = []
        temp = 0
    for i in range(6):
        for j in range(biggestNumber-numberBetweenEachGap[i]):
            templist.append(" ")
        for j in range(numberBetweenEachGap[i]):
            templist.append("*")
        drawHistographElement.append(templist)
        templist = []
    for i in range(6):
        print(drawHistographElement[i])
    
    print('-------------------------------------------------------')
    print("")

    for i in range(biggestNumber):
        for j in range(6):
            print(f"{drawHistographElement[j][i]:^1}", end="   ")
        print("")
    for i in range(6):
        print(f"({numberBetweenEachGap[i]:^1})",end=" ")
    return 0

# -----------출력장---------------
#print(findBiggestNumber(data))
#print(findSmallestNumber(data))


data = []
numberOfClass = 5  # 계급의 갯수
data = createData()
print(data)
drawTable(data)
print('-------------------------------------------------------')
drawHistogram(data)