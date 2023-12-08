from collections import Counter

value = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 1,
    'T' : 10,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
}

with open ('aoc7.txt',"r") as file:
    lines = file.readlines()
index = 0
reslist = {}

for line in lines:
    
    cards = line.split()[0]
    jocker = cards.count('J')
    cards = list(cards)
    for x in range(len(cards)):
        cards[x] = value[cards[x]]
    cads = cards
    cards = Counter(cards)
    najczesciej = max(cards,key=cards.get)
    cnt = cards[najczesciej]
    if jocker != 5:
        print(cards.most_common()[1][1])
        if najczesciej == 1:
            cnt = cards.most_common()[1][1]+jocker
        else:
            cnt += jocker
    print (cnt)
    if cnt != 3 and cnt !=2:
        reslist[f"{index}"] = [najczesciej,cnt,0,cards.most_common()[0][1],line.split()[1],cads]
    else:
        reslist[f"{index}"] = [najczesciej,cnt,cards.most_common()[1][0],cards.most_common()[1][1],line.split()[1],cads]
    index+=1

sortedlist= {}
for set in range(len(reslist)):
    set = str(set)
    if len(sortedlist) != 0:
        temp = True
        for i in range(len(sortedlist)):
            i = str(i)
            if int(sortedlist[i][1]) < int(reslist[set][1]):
                sortedlist = dict(sorted(sortedlist.items()))
                temp = False
                for x in reversed(range(int(i),len(sortedlist))):
                    sortedlist[f"{x+1}"] = sortedlist[f"{x}"]
                if len(sortedlist) != 1:
                    sortedlist[f"{i}"] = reslist[set]
                    break
                else:
                    sortedlist[f"{int(i)-1}"] = reslist[set]
        if temp:
            sortedlist[f"{len(sortedlist)}"] = reslist[set]

    else:
        sortedlist[f"{len(sortedlist)}"] = reslist[set] 
    
sortedlist = dict(sorted(sortedlist.items()))
print (len(sortedlist))
max = sortedlist['1'][1]
list1 =[]
list2 = []
list3 = []
list4 = []
list5 = []
house = []
twopairs=[]
for i in sortedlist:
    # if not sortedlist[i][0].isnumeric():
    #     sortedlist[i][0] = value[sortedlist[i][0]]
    # else:
    #     sortedlist[i][0] = int(sortedlist[i][0])
    match sortedlist[i][1]:
        case 1:
            list1.append(sortedlist[i])
        case 2:
            if sortedlist[i][3] == 2:
                twopairs.append(sortedlist[i])
            else:
                list2.append(sortedlist[i])
        case 3:
            # print(sortedlist[i][3])
            if sortedlist[i][3] == 2:
                house.append(sortedlist[i])
            else:
                list3.append(sortedlist[i])
        case 4:
            list4.append(sortedlist[i])
        case 5:
            list5.append(sortedlist[i])



list1 = sorted(list1, key=lambda x: x[-1])
list2 = sorted(list2, key=lambda x: x[-1])
list3 = sorted(list3, key=lambda x: x[-1])
list4 = sorted(list4, key=lambda x: x[-1])
list5 = sorted(list5, key=lambda x: x[-1])
house = sorted(house, key=lambda x: x[-1])
twopairs = sorted(twopairs, key=lambda x: x[-1])
# house.reverse()

# list1.reverse()
# list2.reverse()
# list3.reverse()
# list4.reverse()
# list5.reverse()

endlist = list1 + list2 + twopairs + list3 + house + list4 + list5
print(list1)
print(list2)
print(list3)
print(house)
print(list4)
print(list5)
endlist.reverse()
sum = 0
index = len(endlist)
for i in range(len(endlist)):
    print (endlist[i])
    sum += int(endlist[i][4]) * index
    index -=1
print(sum,len(endlist))