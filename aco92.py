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
    start = True
    for i in reversed((range(0, len(linederivative)-2))):
        a = int(linederivative[i+1][0])
        b = int(linederivative[i][0])
        if start:
            tempsum = b-a
            start = False
        else:
            tempsum = b-tempsum
    sum += tempsum
print(sum)
