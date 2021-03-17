class Quest(object):
    def __init__(self, name, beschreibung, level, belohnung, monster, cooldown):
        self.name = name
        self.beschreibung = beschreibung
        self.level = level
        self.belohnung = belohnung
        self.monster = monster
        self.cooldown = cooldown

    def ausgabe(self):
        return ("Name: " + self.name + "\n" +
                "Beschreibung: " + self.beschreibung + "\n" +
                "Level: " + str(self.level) + "\n" +
                "Belohnung: " + str(self.belohnung) + "\n" +
                "Gegner: " + str(self.monster.name) + "\n" +
                "Cooldown: " + str(self.cooldown))
        print("Name: " + self.name)
        print("Level: " + str(self.level))
