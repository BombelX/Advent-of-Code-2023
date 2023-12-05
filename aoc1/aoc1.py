import re
sum = 0
with open("aoc1input.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line) 
        temp = re.findall(r'\d+', line)
        res = list(map(int, temp))
        tempint = res[0]*10+res[-1]
        sum+=tempint
print(sum)