__author__ = 'tmaclean'


import json


class Character(object):
    def __init__(self, name):
        self.name = name


class CrisisCharacter(Character):
    def __init__(self, name, p, g, w, hp):
        Character.__init__(self, name)
        self.p = p
        self.g = g
        self.w = w
        self.hp = hp


class PlayerCharacter(CrisisCharacter):
    def __init__(self, name, p, g, w, hp):
        CrisisCharacter.__init__(self, name, p, g, w, hp)

        def createCharacter(fileName):
            with open(fileName + ".json", "w") as l:
                l.write(json.dumps({"name": fileName, "attributes": {"p": p, "g": g, "w": w, "hp": hp}, "history": {},
                                    "items": {}, "wyrd": {}}))

        def update(stat, value, name):
            with open(name + ".json", "w") as l:
                l[stat].write(json.dumps(value))


        createCharacter(name)


# MAKE WORK OR JUST CRY

Dave = PlayerCharacter("DavidTyrant", 1, 1, 1, 1)


def update(stat, value, name):
    with open(name + ".json", "w") as l:
        l[stat].write(json.dumps(value))

update("name", "choc", "DavidTyrant")

#
# impact = {"new": "hurray"}
# print(impact)
# with open("TestStates.json", "r") as l:
#     playerData = json.load(l)
# print(playerData)
# playerData.update(impact)
# print(playerData)
# with open("TestStates2.json", "w") as k:
#         k.write(json.dumps(playerData))
