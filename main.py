from curses import wrapper
import curses
import random

def read_data(color_data):
    with open('.color_data') as file:
        for idx,lines in enumerate(file):
            line = lines.split() 
            for i in range(1,len(line)):
                color_data[line[0]].append(int(line[i]))             
    return color_data

def print_data(stdscr):
    color_data = {'JAN': [], 'FEB':[], 'MAR':[], 'APR':[], 'MAY':[], 'JUN':[],
                'JUL':[], 'AUG':[], 'SEP':[], 'OCT':[], 'NOV':[], 'DEC':[] }
    color_data = read_data(color_data)
    print(color_data)
    i = 0
    for month,days in color_data.items():
        stdscr.addstr(0,i,month, curses.color_pair(4))
        i=i+4
        j = 31
        for day in days:
            stdscr.addstr(32-j,i-4,'■■■', curses.color_pair(day))
            j = j-1
        while j != 0:
            stdscr.addstr(32-j,i-4,'■■■', curses.color_pair(random.randint(1,3)))
            j = j-1
    stdscr.refresh()

def main(stdscr):
    stdscr.clear()
    curses.init_color(curses.COLOR_GREEN, 0, 1000, 0)
    curses.init_color(curses.COLOR_RED, 1000, 0, 0)
    curses.init_color(curses.COLOR_YELLOW, 1000, 1000, 0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    print_data(stdscr)
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

