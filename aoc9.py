sum = 0
with open("aocinput.txt", 'r') as file:
    lines = file.readlines()
for line in lines:
    linederivative = [line.split()]
    index = 0
    while len(linederivative[-1]) != linederivative[-1].count(0):
        tmp = []
        for i in range(0, len(linederivative[-1])-1):
            tmp.append(int(linederivative[-1][i+1]
                           ) - int(linederivative[-1][i]))
        linederivative.append(tmp)
    tempsum = 0
    for i in linederivative:
        tempsum += int(i[-1])
    print(tempsum)
    sum += tempsum
print(sum)
