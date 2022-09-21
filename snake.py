from random import choice
from time import sleep

""" Colors """
R = "\033[0;31m█" #Red
Y = "\033[1;33m█" #Yellow
G = "\033[0;32m█" #Green
C = "\033[0;36m█" #Cyan
P = "\033[0;35m█" #Purple
END = "\033[0m" #End of color

""" Rainbow Management """
DIRE = -1, 1 # -1 for Left, 1 for Right
RB = (R, Y, G, C, P) #Rainbow
POS_MIN = 0 #Minimum position value
POS_MAX = int(input("How much the snake can slide on your screen: ")) #Maximum position value
currentPos = POS_MAX // 2 #Determines the current rainbow position inside the loop (with spaces)

while True:
    f = choice(DIRE)
    
    for i in range(5):
        print(" " * currentPos, end="")
        
        for j in range(20): #Rainbow size
            print(RB[(currentPos + j) % 5], end="")
        
        print(END)
        currentPos += f
        if currentPos > POS_MAX or currentPos < POS_MIN:
            currentPos -= f
        sleep(0.02)
