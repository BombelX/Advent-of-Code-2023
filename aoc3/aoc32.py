import re
acs = 0
sum = 0
def findnum(i,index,lines):
    global acs
    iter = 0
    num = ""
    while True:
        iter -= 1
        if not lines[i][index+iter].isnumeric():
            iter +=1
            break
    while True :
        # print(lines[i][index+iter])
        if lines[i][index+iter].isnumeric():
            num += lines[i][index+iter]
        else:
            break
        iter +=1
        
    print (f"{i}   __  num:{num}")
    acs +=1
    return int(num)
with open ('aoc3input.txt', 'r')as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        patern = "([*])"
        indexes = [x.start() for x in re.finditer(patern, line)]
        tmpiloczyn = 1
        if len(indexes) !=0: 
            for index in indexes:
                
                if line[index-1].isnumeric():
                    tmpiloczyn *= findnum(i,index-1,lines) 
                if line[index+1].isnumeric():
                    tmpiloczyn *= findnum(i,index+1,lines)
                if i != 0:
                    ok = True
                    if lines[i-1][index-1].isnumeric() and lines[i-1][index].isnumeric() and lines[i-1][index+1].isnumeric():
                        tmpiloczyn *= findnum(i-1,index,lines)
                        ok = False
                    if lines[i-1][index-1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i-1,index-1,lines)
                    if lines[i-1][index].isnumeric() and not lines[i-1][index-1].isnumeric() and not lines[i-1][index+1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i-1,index,lines)
                    if lines[i-1][index+1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i-1,index+1,lines)

                    ok = True

                    if lines[i+1][index-1].isnumeric() and lines[i+1][index].isnumeric() and lines[i+1][index+1].isnumeric():
                        tmpiloczyn *= findnum(i+1,index,lines)
                        ok = False
                    # print (f"{lines[i+1][index].isnumeric()} -- {lines[i+1][index-1].isnumeric()} -- {lines[i+1][index+1].isnumeric() ")
                    if lines[i+1][index].isnumeric() and not lines[i+1][index-1].isnumeric() and not lines[i+1][index+1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i+1,index,lines)
                    if lines[i+1][index-1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i+1,index-1,lines)
                    if lines[i+1][index+1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i+1,index+1,lines)
                else:
                    ok = True
                    
                    if lines[i+1][index-1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i-1,index-1,lines)
                    if lines[i+1][index].isnumeric() and not lines[i+1][index-1].isnumeric() and not lines[i+1][index+1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i-1,index,lines)
                    if lines[i+1][index+1].isnumeric() and ok:
                        tmpiloczyn *= findnum(i-1,index+1,lines)
                if tmpiloczyn != 1 and acs == 2 :
                    print(tmpiloczyn)
                    sum += tmpiloczyn
                tmpiloczyn = 1
                acs = 0
        i +=1
    print(sum)