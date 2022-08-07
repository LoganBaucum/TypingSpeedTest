import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 0, "Welcome to the Typing Speed Test! Lets see how fast you can type!", curses.color_pair(0))
    stdscr.addstr(4, 0, "PRESS ANY KEY TO CONTINUE", curses.color_pair(0))
    stdscr.refresh()
    stdscr.getkey()
    
def wpm_test(stdscr):
    target_text = "Hello world this is test text!"
    current_text = []
    
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()
    
    

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
   
    start_screen(stdscr)
    wpm_test(stdscr)
    
wrapper(main)