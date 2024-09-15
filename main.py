import random

def createData(number):  # 데이터 만드는 함수 기본값(개수:40)
    data = []
    if (number == 0):
        for i in range(40):
            data.append(random.randint(10,70))
    else:
        for i in range(number):
            data.append(random.randint(10,70))
    return data

def findBiggestNumber(data):  # 데이터 중 가장 큰 수 찾는 함수
    return max(data)

def findSmallestNumber(data):  # 데이터 중 가장 작은 수 찾는 함수
    return min(data)

def findGapOfClass(bigNumber, smallNumber, numberOfClass):
    return round((( bigNumber+1 - smallNumber) / numberOfClass)+0.5)

def sortList(data, numberOfClass, bigNumber, smallNumber):  # 각 계급 간격 사이 개수로 나눠주는 함수 , 계급의 수만큼 나눠줌
    list = []
    classGap = []
    #print(f"가장 작은 수 : {smallNumber}")  
    #print(f"가장 큰 수 : {bigNumber}") 
    gapOfClass = findGapOfClass(bigNumber, smallNumber, numberOfClass) 
    for i in range (numberOfClass): # 도수 범위 나누는 for문
        temp = 0
        for j in range(len(data)):           
            if (data[j] >= smallNumber and data[j] < smallNumber+gapOfClass):
                temp += 1
        #print(smallNumber, end=" ")
        list.append(temp)
        classGap.append(smallNumber)        
        smallNumber += gapOfClass
    #print("")
            
    #print(f"도수 간격: {gapOfClass}")
    #print(f"계급 갯수: {numberOfClass}")
    #print(f"계급 간격: {classGap}")
    #print(f"도수 갯수: {sum(list)}")
    print(f"리스트 보기: {list}")
    return list, classGap

def drawTable(data, numberOfClass):  # 도수분포표 작성해주는 함수
    biggestNumber = findBiggestNumber(data)
    smallestNumber = findSmallestNumber(data)
    gapOfClass = findGapOfClass(biggestNumber, smallestNumber, numberOfClass) #계급 간격
    numberBetweenEachGap, classGap = sortList(data, numberOfClass, biggestNumber, smallestNumber)  #각 계급의 도수의 갯수가 저장
    #print(numberBetweenEachGap)  #도수저장

    print("{0:^6} | {1:^8} | {2} | {3} | {4} | {5} | {6}".format("계 급","계급간격","도수","상대도수","누적도수","누적상대도수",'계급값'))  #출력
    temp = 0  #누적도수
    accumulate = 0  #누적상대도수
    for i in range(numberOfClass): #계급의 갯수만큼 반복
        accumulate += numberBetweenEachGap[i]/len(data)  #누적상대도수 증가
        temp += numberBetweenEachGap[i]  #누적도수 증가
        print(f"제{i+1:2}계급 | {classGap[i]-0.5:^5}~ {(classGap[i]+gapOfClass)-0.5:^5} | {numberBetweenEachGap[i]:^5}| {numberBetweenEachGap[i]/len(data):^8.3f} | {temp:^8} | {accumulate:^12.3f} |  {((classGap[i])+gapOfClass/2)-0.5:^4}")
    print("{0:^6} |              | {1:^4} | {2:^8.3f} |".format("합 계",temp,accumulate))
    return 0

def drawHistogram(data, numberOfClass):
    biggestNumber = findBiggestNumber(data)
    smallestNumber = findSmallestNumber(data)
    gapOfClass = round(((biggestNumber - smallestNumber) / numberOfClass)+0.5) #계급 간격
    numberBetweenEachGap, dummy = sortList(data, numberOfClass, biggestNumber, smallestNumber)
    drawHistographElement = []
    count = findBiggestNumber(numberBetweenEachGap)  # 몇번 반복할지 저장

    #print(numberBetweenEachGap)

    for i in range(len(dummy)):  # 가장 도수가 큰 계급값 기준 값이 있으면 * 없으면 --
        templist = []
        for j in range(count-numberBetweenEachGap[i]):
            templist.append("-------")
        for j in range(numberBetweenEachGap[i]):
            templist.append(" * ----")
        drawHistographElement.append(templist)
    templist = []

    for i in range(count):  # 가장 도수가 큰 계급값 기준 숫자 맵핑
        templist.append(count-i)
    drawHistographElement.append(templist)

    #print(drawHistographElement)

    for i in range(count):  # 히스토그램 본론 출력
        for j in range(len(dummy)):
            print(f"{drawHistographElement[j][i]:^5}", end="")
        print(f"--{drawHistographElement[j+1][i]:^5}", end="  ")
        print("")

    for i in range(len(dummy)):  # 가장 밑에 있는 계급값 출력
        print(f"{((dummy[i])+gapOfClass/2)-0.5}",end=" | ")
    return 0

#-------------------------------------------------------------------
data = []
print("랜덤생성 : 1   하드코딩 : 2")
selectDataType = input("데이터 타입을 선택하세요 : ")
if(selectDataType == '2'):
    selectNumberOfClass = int(input("계급의 갯수을 선택하세요(0입력시 추천값 적용) : "))
    data = [41,32,30,23,24,32,11,39,24,46,50,18,41,14,33,50,38,25,32,16,43,19,35,22,46,43,10,22,17,47,66,48,25,43,28,31,12,25,12,48,41,32,30,23,24,32,11,9,24,46,50,18,41,14,33,50,38,25,32,16,43,19,35,22,46,43,10,22,17,47,66,48,25,43,28,31,12,25,12,48]     # 수동입력
    selectNumberOfClass = round(len(data)**(1/2)) if(selectNumberOfClass == 0) else selectNumberOfClass
else:
    selectNumberOfClass = int(input("계급의 갯수을 선택하세요(0입력시 추천값 적용) : "))
    numberOfData = int(input("도수 갯수를 적어주세요(0입력시 생략, 기본값(40)) : "))
    data = createData(numberOfData)   # 자동입력1
    
    selectNumberOfClass = round(len(data)**(1/2)) if(selectNumberOfClass == 0) else selectNumberOfClass
    
    
print('------------------------<데이터 원본>-----------------------\n')
print(data)
print(selectNumberOfClass)
print('\n------------------------<도수분포표>-----------------------\n')
drawTable(data,selectNumberOfClass)
print('\n------------------------<상대도수 히스토그램>-----------------------\n')
drawHistogram(data, selectNumberOfClass)