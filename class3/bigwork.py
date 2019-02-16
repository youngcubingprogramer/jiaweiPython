import random

# 1. the value created by  random function need  format(), such as, the value is 899 , 0899
realValue = int(random.random()*10000)
# realValue = 4228
chance = 10
while(chance):

    inputValue = int(input(str('请输入一个四位数:')))
    # print(realValue,inputValue)
    print(realValue)
    rv1 = realValue%10
    rv2 = int((realValue%100)/10)
    rv3 = int((realValue%1000)/100)
    rv4 = int((realValue%10000)/1000)
    rvList = [rv4,rv3,rv2,rv1]

    iv1 = inputValue%10
    iv2 = int((inputValue%100)/10)
    iv3 = int((inputValue%1000)/100)
    iv4 = int((inputValue%10000)/1000)
    ivList = [iv4,iv3,iv2,iv1]

    aList = [0,0,0,0]
    for index in range(4):
        if(ivList[index]==rvList[index]):
            aList[index] = 1
        else:
            aList[index] = 0

    bList = [0,0,0,0]
    for index in range(4):
        for real in rvList:
            if(real == ivList[index]):
                bList[index] = 1
            else:
                bList[index] = 0

    # print(bList)


    for index in range(4):
        if(aList[index] ==1):
            bList[index] = 0

    sumA = 0
    for a in aList:
        sumA = sumA + a
    sumB = 0
    for b in bList:
        sumB =sumB + b

    print(sumA,"A",sumB,"B")
    chance = chance -1

print('感受绝望吧。。。')