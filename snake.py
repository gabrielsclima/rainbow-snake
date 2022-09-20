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
spc = 50 #Determines the current rainbow position inside the loop

def mod5(x):
    return x % 5

while True:
    f = choice(DIRE)
    
    for i in range(5):
        oldSpc = spc
        print(" " * spc, end="")
        spc += f
        
        for j in range(20): #Rainbow size

            if spc > 100: #For now, we have to change this value according to your terminal/prompt command size
                spc -= 1

            elif spc < 0:
                spc += 1

            print(RB[mod5(f * i+j)] if oldSpc > 0 and oldSpc < 50 else RB[mod5(j)], end="")
        
        print()
        sleep(0.02)
