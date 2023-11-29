# AUTHOR: ServerLite
# Date: 11/29/2023 - 2:45 PM
# Description: Just a bouncing ball in the terminal

# IMPORTED CLASSES
from os import system # Used for clearing the screen
from time import sleep # Used for stepping the program
from random import choice # Used for making decisions on where the ball should go

# Holds the functions to operate the window
class Window:
    def __init__(self, size_x:int=8, size_y:int=8, screen_filler:chr=' '):
        self.__x = size_x # Size x of screen
        self.__y = size_y # Size y of screen
        self.__screen_filler = screen_filler # Empty space for screen

        self.__screen = self.__CreateWindow()

    # Creates the window which is lists within a single list
    def __CreateWindow(self):
        return [[self.__screen_filler for x in range(self.__x)] for y in range(self.__y)]
    
    # Display the window to the terminal
    # - Already clearing the window
    # - Displaying window with proper format
    def DisplayWindow(self):
        system("cls")
        for y in self.__screen:
            [print(x, end=" ") for x in y]
            print("")
            
    # Gets the screen
    # - DOES NOT modify the window if modified the RETURNED screen
    def GetScreen(self):
        return self.__screen

    # Modifies a single point in the screen
    def ModifyPoint(self, x:int=0, y:int=0, point:chr='N'):
        self.__screen[y][x] = point
        
    # Gets a point from the screen
    def GetPoint(self, x:int=0, y:int=0):
        return self.__screen[y][x]
    
    # Moves a point from one location to another on the screen
    def MovePoint(self, start_x:int, start_y:int, end_x:int, end_y:int):
        point = self.GetPoint(start_x, start_y)
        self.ModifyPoint(start_x, start_y, self.__screen_filler)
        self.ModifyPoint(end_x, end_y, point)

# Window Settings
screen_x, screen_y = 16, 8
screen_filler = ' '
barrier_icon = '#'
step = 0.03

# Icon Settings
icon_position_x, icon_position_y = 1, 4
icon_point = '0'

# Creating the window buffer
_WINDOW = Window(screen_x, screen_y, screen_filler)

# Creating the barrier around the screen
for idy, y in enumerate(_WINDOW.GetScreen()):
    for idx, x in enumerate(y):
        if idx == 0 or idy == 0 or idx == screen_x-1 or idy == screen_y-1:
            _WINDOW.ModifyPoint(idx, idy, barrier_icon)

# Draw player onto screen
_WINDOW.ModifyPoint(icon_position_x, icon_position_y, icon_point)

# ACTION_1 = 0
# ACTION_2 = 1
# ACTION_3 = 2
# ACTION_4 = 3
action = 0

action_retake = [
    [2,3], # BOTTOM RIGHT - 0
    [2,3], # BOTTOM LEFT - 1
    [0,1], # TOP RIGHT - 2
    [0,1]  # TOP LEFT - 3
    ]
            
# This is the main window loop
while True:
    # Refresh the screen
    sleep(step)

    # Ball going BOTTOM RIGHT
    if action == 0:
        if _WINDOW.GetPoint(icon_position_x+1, icon_position_y+1) != barrier_icon:
            _WINDOW.MovePoint(icon_position_x, icon_position_y, icon_position_x+1, icon_position_y+1)
            icon_position_x += 1
            icon_position_y += 1
        else:
            action = choice(action_retake[0])
            
    # Ball going BOTTOM LEFT
    elif action == 1:
        if _WINDOW.GetPoint(icon_position_x-1, icon_position_y+1) != barrier_icon:
            _WINDOW.MovePoint(icon_position_x, icon_position_y, icon_position_x-1, icon_position_y+1)
            icon_position_x -= 1
            icon_position_y += 1
        else:
            action = choice(action_retake[1])
            
    # Ball going TOP RIGHT
    elif action == 2:
        if _WINDOW.GetPoint(icon_position_x+1, icon_position_y-1) != barrier_icon:
            _WINDOW.MovePoint(icon_position_x, icon_position_y, icon_position_x+1, icon_position_y-1)
            icon_position_x += 1
            icon_position_y -= 1
        else:
            action = choice(action_retake[2])
            
    # Ball going TOP LEFT
    elif action == 3:
        if _WINDOW.GetPoint(icon_position_x-1, icon_position_y-1) != barrier_icon:
            _WINDOW.MovePoint(icon_position_x, icon_position_y, icon_position_x-1, icon_position_y-1)
            icon_position_x -= 1
            icon_position_y -= 1
        else:
            action = choice(action_retake[3])

    # Displaying the screen
    _WINDOW.DisplayWindow()
