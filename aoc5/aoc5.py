import re
low = 9999999999999
sections = []
for i in range (0,8):
    sections.append([])
with open ('aoc5input.txt','r')as file:
    lines = file.readlines()
    index = 0
    for line in lines:
        if line == "\n":
            index +=1
        if line != '':
            sections[index].append(line.replace('\n',''))
for i in range (1,8):
    sections[i].pop(0)
newseeds = []
seeds = str(sections[0][0])
seeds = seeds.split()
tmpranges = []
for i in range (1,len(seeds),2):
    tmp = [seeds[i],seeds[i+1]]
    tmpranges.append(tmp)

for i in range(1,99999999999):
    seed = i
    for section in reversed(range(1,len(sections))):
        converted = False
        for io in range (1,len(sections[section])):
            operations = sections[section][io].split()
            chng = (int(operations[1])-int(operations[0]))
            if seed in range(int(operations[0]),int(operations[0])+int(operations[2])):
                seed = seed+chng
                converted = True
                break
        if converted == False:
            continue
    print("\r" + str(seed) + "/" + "9999999999" + "=============" + str(i) + "/" + "9999999999", end="", flush=True)
    for x in tmpranges:
        if seed in range(int(x[0]),int(x[0])+int(x[1])):
            low = seed
            print(low)
            exit()
            
      
