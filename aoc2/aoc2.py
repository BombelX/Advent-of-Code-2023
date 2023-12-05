import re
sum = 0
with open ('aocinp2.txt','r') as file:
    lines = file.readlines()
    for line in lines :
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
                if "red" in iter and int(res[0])>12 :
                    ok = False
                if "green" in iter and int(res[0])>13 :
                    ok = False
                if "blue" in iter and int(res[0])>14 :
                    ok = False
        if ok:
            sum += int(line.split(":")[0].split(" ")[1])
    print(sum)


