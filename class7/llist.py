list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

biglist = [list1,list2,list3]
for li in biglist:
    print(li)


#sum
sum = 0
for row in range(3):
    for col in range(3):
        # print(biglist[row][col])
        sum = sum + biglist[row][col]
print(sum)