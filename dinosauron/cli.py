import curses
from dinosauron import dino_nmap
from time import sleep

class Chui:
    """ character based UI """

    def __init__(self):
        pass

    def run(self):
        stdscr = curses.initscr()
        curses.start_color()
        stdscr.addstr("dinosauron " + "=" * (curses.COLS - 11))

        while True:
            c = stdscr.getch()
            if c == ord('q'):
                break

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


