import curses
from curses import wrapper
from time import sleep

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    stdscr.clear()
    stdscr.addstr(4, 5, "Welcome to the Typing Speed Test!", curses.color_pair(0))
    stdscr.addstr(5, 5, "Lets see how fast you can type! PRESS ANY KEY TO CONTINUE", curses.color_pair(0))
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)