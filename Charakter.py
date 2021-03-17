from discord.ext import commands
class Charakter(object):
    def __init__(self, name, minAtk, maxAtk, hp,speed,dodge, level, preis):
        self.name = name
        self.minAtk = minAtk
        self.maxAtk = maxAtk
        self.hp = hp
        self.speed = speed
        self.dodge = dodge
        self.level = level
        self.preis = preis

    def ausgabe(self):
        return ("Name: " + self.name + "\n" + "MinAtk: " + self.minAtk + "\n" + "MaxAtk: " + self.maxAtk + "\n" + "HP: " + self.hp + "\n" +
                "Speed: " + self.speed + "\n" + "Dodgechance: " + self.dodge + "\n" + "Level: " + self.level + "\n" + "Preis: " + self.preis + "\n")
        print("Name: " + self.name)
        print("MinAtk: " + self.minAtk)
        print("MaxAtk: " + str(self.maxAtk))
        print("HP: " + str(self.hp))
        print("Level: " + str(self.level))
        print("Preis: " + str(self.preis))

