import curses
from curses import wrapper

# Displays text to welcome the player and start the game.
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Speed Test! Lets see how fast you can type!", curses.color_pair(0))
    stdscr.addstr(4, 0, "PRESS ANY KEY TO CONTINUE", curses.color_pair(0))
    stdscr.refresh()
    stdscr.getkey()

# Display the current typed text on top of the target text.
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)

    for i, char in enumerate(current):
        correct_char = target[i]
        textcolor = curses.color_pair(1) # Green text       
        if char != correct_char:            
            textcolor = curses.color_pair(2) # Red text
        
        stdscr.addstr(0, i, char, textcolor)
            

# Typging game functionality
def wpm_test(stdscr):
    target_text = "Hello world this is test text!"
    current_text = []
        
    # Each time a key is entered, evalutate and display it. At the end calculate the score/speed.
    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()
        
        key = stdscr.getkey()
        # Exit if Escape is pressed. 
        if ord(key) == 27: 
            break
        # Backspace functionality
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):  
            if len(current_text) > 0:
                current_text.pop()
        
        # Stops the player from entering more text than needed for the sentence.
        elif len(current_text) < len(target_text): 
            current_text.append(key)


def main(stdscr):
    # Text color presets
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
   
    start_screen(stdscr)
    wpm_test(stdscr)
    
wrapper(main)