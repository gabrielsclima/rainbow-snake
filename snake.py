import random
from time import sleep

# Colors
red = "\033[0;31m█"
yellow = "\033[1;33m█"
green = "\033[0;32m█"
cyan = "\033[0;36m█"
purple = "\033[0;35m█"
end_color = "\033[0m"

# Rainbow settings
direction = -1, 1 # -1 for Left, 1 for Right
color_sequence = (red, yellow, green, cyan, purple)
minimum_position = 0
maximum_position = int(input("How much can the snake slide on your screen: "))
current_position = maximum_position // 2
rainbow_width = 5

# Start
while True:
    direction_choice = random.choice(direction)
    
    for distance in range(5):
        print(" " * current_position, end="")

        for width_position in range(rainbow_width):
            print(color_sequence[(current_position + width_position) % 5], end="")
        print(end_color)
        
        current_position += direction_choice
        if current_position > maximum_position or current_position < minimum_position:
            current_position -= direction_choice
        sleep(0.02)
