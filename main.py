import curses
from curses import wrapper

# Displays text to welcome the player and start the game.
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Speed Test! Lets see how fast you can type!", curses.color_pair(0))
    stdscr.addstr(4, 0, "PRESS ANY KEY TO CONTINUE", curses.color_pair(0))
    stdscr.refresh()
    stdscr.getkey()

# Typging game functionality
def wpm_test(stdscr):
    target_text = "Hello world this is test text!"
    current_text = []
        
    # Each time a key is entered, evalutate and display it. At the end calculate the score/speed.
    while True:
        key = stdscr.getkey()
        
        #Exit if Escape is pressed.
        if ord(key) == 27:
            break
                
        current_text.append(key)
        stdscr.clear()
        
        stdscr.addstr(target_text)
    
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        
        stdscr.refresh()


def main(stdscr):
    # Text color presets
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
   
    start_screen(stdscr)
    wpm_test(stdscr)
    
wrapper(main)