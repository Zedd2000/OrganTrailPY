import random
import sys
import time
from os import system, name

def clear(): # Clears the screen. Thanks Stackoverflow
        if name == 'nt':
            _ = system('cls') # for windows
        else:
            _ = system('clear') # for mac and linux

def rand_line(fname): #grabs random line of text file
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def SPrint(pause, string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(pause)
