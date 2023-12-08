poz = []

with open('aoc8input.txt','r') as file:
    lines = file.readlines()

moveset = lines[0].replace('\n','').strip()
moveset = moveset.replace('R','1')
moveset = moveset.replace('L','0')

navigationtable = []
for x in range(2,len(lines)):
    line = lines[x]
    line = line.split('=')
    line[1] = (line[1].replace(')',''))
    line[1] = (line[1].replace('(',''))
    line[1] = (line[1].replace(' ',''))
    line[1] = (line[1].replace('\n',''))


    navigationtable.append([line[0].strip(),line[1].split(',')])
# print(navigationtable)

for i in navigationtable:
    if i[0][-1] == 'A':
        poz.append(i[0])

print(poz)
index = 0
while True:
    for p in poz:
        for i in navigationtable:
            if i[0] == p:
                # if index > len(moveset):
                idx = index%len(moveset)
                poz[poz.index(p)] = i[1][int(moveset[idx])]
                break
    index+=1
    cnt = 0
    for i in poz:
        if i[-1] == 'Z':
            cnt+=1
    if cnt == len(poz):
        break
    # print("\r" + str(index) + "/", end="", flush=True)
print(index)

