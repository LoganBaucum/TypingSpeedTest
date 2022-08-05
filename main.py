import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hellow World!")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)