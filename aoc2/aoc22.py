import re
sum = 0

with open ('aocinp2.txt','r') as file:
    lines = file.readlines()
    for line in lines :
        maxred,maxblue,maxgreen=0,0,0
        splitedline = line.split(';')
        first = True
        ok = True
        for i in splitedline:
            if first:
                i = (i.split(":")[1])
            i = i.split(",")
            first = False
            for iter in i:
                temp = re.findall(r'\d+', iter)
                res = list(map(int, temp))
                print (f'{iter},  {res[0]}')  
                if "red" in iter :
                    if int(res[0])>maxred:
                        maxred=int(res[0])
                if "green" in iter  :
                    if int(res[0])>maxgreen:
                        maxgreen=int(res[0])
                if "blue" in iter  :
                    if int(res[0])>maxblue:
                        maxblue=int(res[0])  
        print(f"{maxblue} * {maxred} * {maxgreen} = {maxblue*maxgreen*maxred} ")
        sum += maxblue*maxgreen*maxred
    print(sum)


