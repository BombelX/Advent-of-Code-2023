with open('aoc10inputfull.txt', 'r') as file:
    lines = file.readlines()
sindex = 0
# lenline = len(lines[0])
for inx, line in enumerate(lines):
    if 'S' in line:
        sindex = inx
print(sindex)
spoz = lines[sindex].index("S")
scoorditanes = [sindex, spoz]
print(lines[sindex][spoz])
looplen = 0
for i in range(0, 3):
    firts = True
    cnt = -1
    while True:
        cnt += 1
        if firts:
            if i == 0:
                poz = [scoorditanes[0]-1, scoorditanes[1], 'up']
            if i == 1:
                poz = [scoorditanes[0], scoorditanes[1]+1, 'right']
            if i == 2:
                poz = [scoorditanes[0]+1, scoorditanes[1], 'down']
            if i == 3:
                poz = [scoorditanes[0], scoorditanes[1]-1, 'left']
            firts = False
        match lines[poz[0]][poz[1]]:
            case '|':  # |to pionowa rura łącząca północ z południem.
                if (poz[2] == 'up' or poz[2] == 'down'):
                    if poz[2] == 'down':
                        poz = [poz[0]+1, poz[1], 'down']
                    else:
                        poz = [poz[0]-1, poz[1], 'up']
                else:
                    break
            case '-':  # -to pozioma rura łącząca wschód i zachód.
                if (poz[2] == 'right' or poz[2] == 'left'):
                    if poz[2] == 'right':
                        poz = [poz[0], poz[1]+1, 'right']
                    else:
                        poz = [poz[0], poz[1]-1, 'left']
                else:
                    break
            case 'L':  # Lto zakręt o 90 stopniach łączący północ i wschód.
                if (poz[2] == 'down' or poz[2] == 'left'):
                    if poz[2] == 'down':
                        poz = [poz[0], poz[1]+1, 'right']
                    else:
                        poz = [poz[0]-1, poz[1], 'up']
                else:
                    break
            case 'J':  # Jto zakręt o 90 stopniach łączący północ i zachód.
                if (poz[2] == 'down' or poz[2] == 'right'):
                    if poz[2] == 'right':
                        poz = [poz[0]-1, poz[1], 'up']
                    else:
                        poz = [poz[0], poz[1]-1, 'left']
                else:
                    break
            # 7to zakręt o kącie 90 stopni łączący południe i zachód..
            case '7':
                if (poz[2] == 'right' or poz[2] == 'up'):
                    if poz[2] == 'right':
                        poz = [poz[0]+1, poz[1], 'down']
                    else:
                        poz = [poz[0], poz[1]-1, 'left']
                else:
                    break
            case 'F':
                if (poz[2] == 'left' or poz[2] == 'up'):
                    if poz[2] == 'left':
                        poz = [poz[0]+1, poz[1], 'down']
                    else:
                        poz = [poz[0], poz[1]+1, 'right']
                else:
                    break
            case '.':
                break

            case 'S':
                if cnt > looplen:
                    looplen = cnt
                break
print((looplen+1)//2)
