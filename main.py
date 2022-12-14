import curses
from curses import wrapper
import time
import random

# Displays text to welcome the player and start the game.
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Speed Test! Lets see how fast you can type!", curses.color_pair(0))
    stdscr.addstr(4, 0, "PRESS ANY KEY TO CONTINUE", curses.color_pair(0))
    stdscr.refresh()
    stdscr.getkey()


# Display the currently typed text on top of the target text, also display the WPM / Score.
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM: {wpm}")
    stdscr.addstr(4,0, "PRESS ESC TO EXIT")
    stdscr.addstr(0,0, "")

    for i, char in enumerate(current):
        correct_char = target[i]
        textcolor = curses.color_pair(1) # Green text       
        if char != correct_char:            
            textcolor = curses.color_pair(2) # Red text
        
        stdscr.addstr(0, i, char, textcolor)
            
# Returns a random sentence from the text files
def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


# Typing game functionality
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
        
    # Each time a key is entered, evaluate and display it. At the end calculate the score/speed.
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60) ) / 5)
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        # Break to end game when text match exactly.
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        
        # Full sentence typed, end game / break
        # if len(current_text) == len(target_text):
        #     stdscr.nodelay(False)
        #     break
        
        # Wait for input       
        try:
            key = stdscr.getkey()
        except:
            continue
        
        # Escape to exit. 
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
    
    while True:
        wpm_test(stdscr)
        stdscr.nodelay(False)
        stdscr.addstr(2,0, "You completed the text! Press any key to continue. . .")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)