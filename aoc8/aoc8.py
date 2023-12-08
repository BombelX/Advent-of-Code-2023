poz = 'AAA'

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
print(navigationtable)
index = 0
while poz != "ZZZ":
    for i in navigationtable:
        if i[0] == poz:
            # if index > len(moveset):
            idx = index%len(moveset)
            poz = i[1][int(moveset[idx])]
            break
    index+=1
print(index)

