from random import choice
from time import sleep

""" Colors """
R = "\033[0;31m█" #Red
Y = "\033[1;33m█" #Yellow
G = "\033[0;32m█" #Green
C = "\033[0;36m█" #Cyan
P = "\033[0;35m█" #Purple

""" Rainbow Management """
DIRE = -1, 1 #Direction (Left or Right)
RB = (R, Y, G, C, P) #Rainbow
spc = 5 #Determines the actual rainbow position inside the loop

def mod5(x):
    return x % 5

while True:
    f = choice(DIRE)
    for i in range(5):
        oldSpc = spc
        print(" " * spc, end="")
        spc += f

        for j in range(5):
            if spc > 50:
                spc -= 1

            elif spc < 0:
                spc += 1

            am = mod5(f * i+j)
            print(RB[am] if oldSpc > 0 and oldSpc < 50 else RB[j], end="")

        print()
        sleep(0.02)
