from .TAG import *
from random import randint

separator = "******************************************************************"
hours = 10
food = 3
days = 0
events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12]

# Display an exit message when exiting the game
def exitgame():
    print(separator)
    print("See you next time!")
    quit()

# Display the time of the day
def givetime():
    global hours
    print(separator)
    if hours < 12:
        print(f"It's {hours} AM")
    else:
        print(f"It's {hours - 12} PM")
        
# Display the food of the player
def givefood():
    print(f"Food: {food}")

