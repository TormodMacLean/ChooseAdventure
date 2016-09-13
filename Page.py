__author__ = 'tmaclean'

import json
import WindowManager


json_data = open("TestMessage.json").read()
data = json.loads(json_data)


def nextMessage(msg):
        box = Message("chapter1", msg)
        print("new class")


# TODO fix all this shit after you resolve the start screen and character creation stuff

class Message(object):
    def __init__(self, chapter, identifier, title=None, body=None, choices=None):
        self.chapter = chapter
        self.identifier = identifier
        self.title = title
        self.body = body
        self.choices = choices
        title = WindowManager.UILabel(data[chapter][identifier]["title"], 0, 0)
        body = WindowManager.UILabel(data[chapter][identifier]["body"], 1, 0)
        choices = data[chapter][identifier]["choices"]
        global decisionCounter
        decisionCounter = 2
        # def nextMessage(msg):
        #     nonlocal identifier
        #     identifier = str(msg)
        #     title.config(title="title")
        for option in choices:
            WindowManager.UIButton(buttonCommand=lambda: nextMessage(option), widgetText=option, widgetRow=decisionCounter, widgetColumn=0)
            decisionCounter += 1
        WindowManager.root.mainloop()
        print("classend")


damera = Message("chapter1", "right")

