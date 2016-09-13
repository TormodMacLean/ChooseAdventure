__author__ = 'tmaclean'

import WindowManager


def launchCC():
    print("character creation placeholder")


def launchLastSave():
    print("resume placeholder")


def launchLoadScreen():
    print("load screen placeholder")


def pto():
    wtf = WindowManager.UILabel("What do you know", 3, 3)
    WindowManager.root.mainloop()

house = WindowManager.UILabel("Tyrant Slayer: Children of the Fall", 0, 1)
new = WindowManager.UIButton(launchCC, "New Game", 1, 0)
resume = WindowManager.UIButton(launchLastSave, "Resume", 1, 1)
next = WindowManager.UIButton(pto, "practice", 1, 2)
load = WindowManager.UIButton(launchLoadScreen, "Load", 1, 3)


WindowManager.root.mainloop()