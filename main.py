  GNU nano 3.2                                    main.py                                              

from curses import wrapper
import curses
import random
import os
import sys
import datetime

def read_data(color_data):
    if not os.path.isfile('.color_data'):
        stri = "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n"
        with open('.color_data','w+') as file:
            for month in color_data:
                file.write(month+' '+stri)

    with open('.color_data') as file:
        for idx,lines in enumerate(file):
            line = lines.split()
            for i in range(1,len(line)):
                color_data[line[0]].append(int(line[i]))
    return color_data

def write_data(point):
    with open('.color_data', 'r+') as file:
        now = datetime.datetime.now()
        file.seek(now.day*2+2+(66*(now.month-1)))
        file.write(point)


def print_data(stdscr, color_data):
    i = 0
    for month,days in color_data.items():
        stdscr.addstr(0,i,month, curses.color_pair(4))
        i=i+4
        j = 31
        for day in days:
            stdscr.addstr(32-j,i-4,'■■■', curses.color_pair(day))
            j = j-1
    stdscr.refresh()

def main(stdscr):
    stdscr.clear()
    curses.init_color(curses.COLOR_GREEN, 0, 1000, 0)
    curses.init_color(curses.COLOR_RED, 1000, 0, 0)
    curses.init_color(curses.COLOR_YELLOW, 1000, 1000, 0)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    color_data = {'JAN': [], 'FEB':[], 'MAR':[], 'APR':[], 'MAY':[], 'JUN':[],
                'JUL':[], 'AUG':[], 'SEP':[], 'OCT':[], 'NOV':[], 'DEC':[] }
    color_data = read_data(color_data)
    if len(sys.argv) is 2:
        write_data(sys.argv[1])
    print_data(stdscr, color_data)
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

