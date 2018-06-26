#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses
#start
stdscr = curses.initscr()
# Keine Anzeige gedrückter Tasten
curses.noecho()
# Kein line-buffer
curses.cbreak()
# Escape-Sequenzen aktivieren
stdscr.keypad(1)

# Farben
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

# Fenster und Hintergrundfarben
stdscr.bkgd(curses.color_pair(1))
stdscr.refresh()

win = curses.newwin(5, 20, 5, 5)
win.bkgd(curses.color_pair(2))
win.box()
win.addstr(2, 2, "Hallo, Welt!")
win.refresh()

# Warten auf Tastendruck
c = stdscr.getch()

# Ende
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
