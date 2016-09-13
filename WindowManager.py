__author__ = 'tmaclean'


import tkinter



root = tkinter.Tk()
root.title("Tyrant Slayer")
# fix iconbitmap
root.iconbitmap("TS.ico")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("900x600")

class UIWidget(object):
    def __init__(self, widgetText, widgetRow, widgetColumn, widgetPosition="nsew"):
        self.text = widgetText
        self.row = widgetRow
        self.column = widgetColumn
        self.position = widgetPosition


class UIButton(UIWidget):
    def __init__(self, buttonCommand, widgetText=None, widgetRow=None, widgetColumn=None, widgetPosition="nsew"):
        super(UIButton, self).__init__(widgetText, widgetRow, widgetColumn, widgetPosition="nsew")
        self.buttonCommand = buttonCommand
        widget = tkinter.Button(root, text=widgetText, command=buttonCommand)
        widget.grid(row=widgetRow, column=widgetColumn, sticky=widgetPosition)


class UILabel(UIWidget):
    def __init__(self, widgetText=None, widgetRow=None, widgetColumn=None, widgetPosition="nsew"):
        super(UILabel, self).__init__(widgetText, widgetRow, widgetColumn, widgetPosition="nsew")
        widget = tkinter.Label(root, text=widgetText)
        widget.grid(row=widgetRow, column=widgetColumn, sticky=widgetPosition)

# Start Screen



