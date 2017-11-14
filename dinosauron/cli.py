import curses
from dinosauron import dino_nmap
from time import sleep

class Chui:
    """ character based UI """

    def __init__(self):
        self.stdscr = curses.initscr()
        #self.stdscr.border(1)

    def scan(self, targets, options):
        results = dino_nmap.scan_many(targets, options)
        return results

    def draw(self, contents=[]):
        self.stdscr.clear()
        curses.start_color()
        self.stdscr.addstr("dinosauron " + "=" * (curses.COLS - 11))
        for text in contents:
            self.stdscr.addstr(str(text))
        self.stdscr.refresh()

    def run(self):
        self.draw()
        results = self.scan(["scanme.nmap.org"], "-sV")
        self.draw([results])
        while True:
            c = self.stdscr.getch()
            if c == ord('q'):
                break

        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()


