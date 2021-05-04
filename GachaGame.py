import os
import random
from Charakter import Charakter
from quest import Quest
from time import sleep
from _thread import start_new_thread
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
from random import randint
import json

import datetime
import locale
# def __init__(self, name, minAtk, maxAtk, hp, level):
Jan1 = Charakter ("Jan, der Cheater", "1","150","3050","80","95","1","400005000")
Robin1 = Charakter("Robin, der Salzlord", "20","50","150","4","2","1","45000")
Robin2 = Charakter("Robin, der Diskutierfreudige", "5","20","500","7","3","1","33000")
Kevin1 = Charakter("Kevin, der Gegnerfinder", "5","20","100","9","0","1","5000")
Kevin2 = Charakter("Kevin, der Clown", "10","40","200","12","5","1","35973")
Kevin3 = Charakter("Kevin, der Hentai", "20","80","700","17","6","1","85293")
Steven1 = Charakter("Steven, der Affe", "15","40","600","8","10","1","44444")
Steven2 = Charakter("Steven, die alte Dame", "25","60","350","20","2","1","66464")
Steven3 = Charakter("Steven, das Uwuli","40","50","750","20","15","1","186464")
Keyz1 = Charakter("Keyz, der CEO", "25","50","450","5","5","1","50000")
Keyz2 = Charakter("Keyz, der Geschichtenerzähler", "125","250","650","12","4","1","250000")
Gunnar1 = Charakter("Gunnar, Rüdiger Senior", "1","3","1500","2","4","1","35000")
Gunnar2 = Charakter("Gunnar, das Uwuchu", "60","110","50","10","8","1","37000")
Enes1 = Charakter("Enes, der Gachaking", "5","20","100","3","1","1","5000")
Niko1 = Charakter("Niko, der Tangierte", "3","6","666","1","2","1","150000")
Marina1 = Charakter("Marina, die uwukatze", "50","80","200","5","30","1","75000")
Marina2 = Charakter("Marina, der Yordle", "10","30","250","10","30","1","35221")
Minh1 = Charakter("Minh, das Schnitzel", "30","80","200","7","22","1","75000")
Minh2 = Charakter("Minh, das Pferd", "5","25","273","35","5","1","97200")
Phong1 = Charakter("Phong, der Ragequitter", "100","200","1","11","11","1","15000")
Flo1 = Charakter("Flo, der Lustmolch", "5","20","100","9","0","1","7500")
Matties1 = Charakter("Matties, der Prophet", "25","100","150","3","15","1","42500")
Matties2 = Charakter("Matties, der Riese", "25","40","1500","3","0","1","82500")

atkkosten = {
1 : 200,
2 : 500,
3 : 2000,
4 : 5000,
5 : 7000,
6 : 10000,
7 : 12500,
8 : 15000,
9 : 20000,
10 : 25000,
11 : 30000,
12 : 35000,
13 : 45000,
14 : 50000,
15 : 100000,
}

hpkosten = {
1 : 200,
2 : 500,
3 : 2000,
4 : 5000,
5 : 7000,
6 : 10000,
7 : 12500,
8 : 15000,
9 : 20000,
10 : 25000,
11 : 30000,
12 : 35000,
13 : 45000,
14 : 50000,
15 : 100000,
}

speedkosten = {
1 : 2000,
2 : 5000,
3 : 20000,
4 : 50000,
5 : 70000,
6 : 100000,
7 : 125000,
8 : 150000,
9 : 200000,
10 : 250000,
11 : 300000,
12 : 350000,
13 : 450000,
14 : 500000,
15 : 1000000,
}

dodgekosten = {
1 : 4000,
2 : 10000,
3 : 40000,
4 : 100000,
5 : 140000,
6 : 200000,
7 : 250000,
8 : 300000,
9 : 400000,
10 : 500000,
11 : 600000,
12 : 700000,
13 : 900000,
14 : 1000000,
15 : 2000000,
}

incomekosten = {
1 : 4000,
2 : 10000,
3 : 40000,
4 : 100000,
5 : 140000,
6 : 200000,
7 : 250000,
8 : 300000,
9 : 400000,
10 : 500000,
11 : 600000,
12 : 700000,
13 : 900000,
14 : 1000000,
15 : 2000000,
}

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
#"Marina, die υωυkatze","Minh, der Schnelle","Flo, der Lustmolch","Matties, der Prophet","Steven, die alte Dame","Kevin, der Clown","Minh, das Schnitzel"]

#Monster
Monster1 = Charakter("Caesar, der Eroberer", "4","6","350","20","25","1","0")
Monster2 = Charakter("Beelzebub, der Innere Dämon", "6","12","650","25","15","1","0")
Monster3 = Charakter("Artamiel, der Erzengel", "10","18","1050","25","25","1","0")

#def __init__(self, name, beschreibung, level, belohnung, monster):
Quest1 = Quest("Der Weg nach Rom", "Du gehst einen Weg entlang, dieser führt nach Rom.", 1, 100, Monster1,"30 Sekunden")
Quest2 = Quest("Back to the roots", "Du versuchst dich durch Meditation selbst zu finden.", 2, 1000, Monster2,"30 Minuten")
Quest3 = Quest("Ascending to Heaven", "Du versuchst zum Himmel aufzusteigen", 3, 1900, Monster3,"50 Minuten")

allquests = [Quest1,Quest2,Quest3]

client = commands.Bot(command_prefix="!")


Charaktere = [Robin1,Robin2,Kevin1,Kevin2,Kevin3,Steven1,Steven2,Steven3,Keyz1,Keyz2,Gunnar1,Gunnar2,Enes1,Niko1,Marina1,Marina2,Minh1,Phong1,Flo1,Matties1,Matties2]
shop = []
player2 = ""
einladung = False

def passive_income():
    for user in os.listdir('./players/'):
        f = open ("./players/" + user,"r")
        data = f.read()
        f.close()
        f = open("./stats/" + user, "r")
        stats = f.readlines()
        f.close()
        income = stats[4]
        print (data)
        new_money = int(data) + 10 + 50 * int(income)
        f = open ("./players/" + user,"w")
        f.write(str(new_money))
        f.close()
    sleep(300)
    passive_income()


@client.event
async def on_ready():
    global shop
    print("Flawy meldet sich zum Start!")
    shop = random.sample(Charaktere,3)
    print (shop)
 #   for i in range(0,3):
      #  shop.append(random.choice(Charaktere))
    start_new_thread(passive_income,())

def wettspiel (ctx):
    glückszahl = randint(0,1)
    """
    if str(ctx.message.author) == "Evil Prophet#2080":
        glückszahl = 1
        
    if str(ctx.message.author) == "Devastate#3369":
        glückszahl = 1
    """
    if glückszahl == 0:
        return True
    else:
        return False



async def kämpfen(p1,p2,char1,char2,ctx):
    i = 0
    ktxt =  ""
    f = open("./stats/" + p1 + ".txt", "r")
    stats = f.readlines()
    f.close()
    atku = int(stats[0])
    hpu = int(stats[1])
    spdu = int(stats[2])
    dodgeu = int(stats[3])
    f = open("./stats/" + p2 + ".txt", "r")
    stats = f.readlines()
    f.close()
    atku2 = int(stats[0])
    hpu2 = int(stats[1])
    spdu2 = int(stats[2])
    dodgeu2 = int(stats[3])
    ch1spd = int(char1.speed) + 2 * spdu
    ch2spd = int(char2.speed) +2 * spdu2
    hp1 = int(char1.hp) + 100 * hpu
    hp2 = int(char2.hp) + 100 * hpu2
    while True:
        i+=1
        #await ctx.send("Turn: " + str(i))
        if len(ktxt) >= 1600:
            await ctx.send(ktxt)
            ktxt = ""
        ktxt += "Turn: " + str(i) +"\n"
        if hp1 <= 0:
            ktxt += char1.name + " hatte noch " + str(hp1) + " HP übrig! \n"
            ktxt += char2.name + " hatte noch " + str(hp2) + " HP übrig! \n"
            await ctx.send(ktxt)
            return 0
        if hp2 <=0:
            ktxt += char1.name + " hatte noch " + str(hp1) + " HP übrig! \n"
            ktxt += char2.name + " hatte noch " + str(hp2) + " HP übrig! \n"
            await ctx.send(ktxt)
            return 1


        if ch1spd >= ch2spd:
            angriff = randint(int(char1.minAtk),int(char1.maxAtk)) + 3 * atku
            ch1spd = ch1spd - ch2spd # 7 #11 #12 #10
            dod = randint(1,100)

            if int(char2.dodge) + dodgeu2 >= dod:
                #await ctx.send(char2.name + " ist gedodged!")
                ktxt += char2.name + " ist gedodged! \n"
            else:
                hp2 = hp2 - angriff
                #await ctx.send(char1.name + " hat " + char2.name + " " + str(angriff) + " Schaden gemacht!")
                #await ctx.send(char2.name + " hat jetzt noch " + str(hp2) + " HP übrig!")
                ktxt += char1.name + " hat " + char2.name + " " + str(angriff) + " Schaden gemacht! \n"
                ktxt += char2.name + " hat jetzt noch " + str(hp2) + " HP übrig! \n"

            if ch2spd > ch1spd:
                ktxt += "------------------- \n"
                i += 1
                ktxt += "Turn: " + str(i) + "\n"
                angriff = randint(int(char2.minAtk), int(char2.maxAtk))  + 3 * atku2
                ch1spd = int(char1.speed) + 2 *spdu
                dod = randint(1, 100)
                if int(char1.dodge) + dodgeu >= dod:
                    #  await ctx.send(char1.name + " ist gedodged!")
                    ktxt += char1.name + " ist gedodged! \n"
                else:
                    hp1 = hp1 - angriff
                    # await ctx.send(char2.name + " hat " + char1.name + " " + str(angriff) + " Schaden gemacht!")
                    # await ctx.send(char1.name + " hat jetzt noch " + str(hp1) + " HP übrig!")
                    ktxt += char2.name + " hat " + char1.name + " " + str(angriff) + " Schaden gemacht! \n"
                    ktxt += char1.name + " hat jetzt noch " + str(hp1) + " HP übrig! \n"

        elif ch2spd > ch1spd:
            angriff = randint(int(char2.minAtk), int(char2.maxAtk))  + 3 * atku2
            ch2spd = ch2spd - ch1spd
            dod = randint(1, 100)
            if int(char1.dodge) + dodgeu >= dod:
              #  await ctx.send(char1.name + " ist gedodged!")
                ktxt += char1.name + " ist gedodged! \n"
            else:
                hp1 = hp1 - angriff
                #await ctx.send(char2.name + " hat " + char1.name + " " + str(angriff) + " Schaden gemacht!")
                #await ctx.send(char1.name + " hat jetzt noch " + str(hp1) + " HP übrig!")
                ktxt += char2.name + " hat " + char1.name + " " + str(angriff) + " Schaden gemacht! \n"
                ktxt += char1.name + " hat jetzt noch " + str(hp1) + " HP übrig! \n"
            if ch1spd >= ch2spd:
                ktxt += "------------------- \n"
                i += 1
                ktxt += "Turn: " + str(i) + "\n"
                angriff = randint(int(char1.minAtk), int(char1.maxAtk))  + 3 * atku
                ch2spd = int(char2.speed) + 2 * spdu2
                dod = randint(1, 100)

                if int(char2.dodge) + dodgeu2 >= dod:
                    # await ctx.send(char2.name + " ist gedodged!")
                    ktxt += char2.name + " ist gedodged! \n"
                else:
                    hp2 = hp2 - angriff
                    # await ctx.send(char1.name + " hat " + char2.name + " " + str(angriff) + " Schaden gemacht!")
                    # await ctx.send(char2.name + " hat jetzt noch " + str(hp2) + " HP übrig!")
                    ktxt += char1.name + " hat " + char2.name + " " + str(angriff) + " Schaden gemacht! \n"
                    ktxt += char2.name + " hat jetzt noch " + str(hp2) + " HP übrig! \n"

        #await ctx.send("-------------------")
        ktxt += "------------------- \n"
        #sleep(1)



def abbuchen(spieler,geld):
    f = open("./players/" + spieler + ".txt", "r")
    data = f.read()
    f.close()
    newgeld = int(data) - int(geld)
    f = open("./players/" + spieler + ".txt", "w")
    f.write(str(newgeld))
    f.close()


def zubuchen(spieler,geld):
    f = open("./players/" + spieler + ".txt", "r")
    data = f.read()
    f.close()
    newgeld = int(data) + int(geld)
    f = open("./players/" + spieler + ".txt", "w")
    f.write(str(newgeld))
    f.close()

@client.command(pass_context=True)
async def quest(ctx, arg):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        #DD = datetime.timedelta(seconds=0)
        player = str(ctx.message.author)
        if int(arg) == 1:
            aktquest = Quest1
            DD = datetime.timedelta(seconds=30)
        elif int(arg) ==2:
            aktquest = Quest2
            DD = datetime.timedelta(minutes=30)
        elif int(arg) ==3:
            aktquest = Quest3
            DD = datetime.timedelta(minutes=50)
        else:
            await ctx.send("Das ist keine gültige Quest!")
            return
        f = open("./cooldown/"+ player + ".txt", "r")
        cd = datetime.datetime.strptime(f.read().rstrip(), '%d %m %Y %H %M %S')
        f.close()
        if datetime.datetime.today() >= cd:
            print("yes!")
            f = open("./characters/" + player + ".txt", "r")
            aktchar = str(f.read())
            f.close()
            for char in Charaktere:
                if char.name == aktchar:
                    aktchar = char
            if aktchar == "Jan, der Cheater":
                aktchar = Jan1
            if await kämpfen(player,"Flawy#1450",aktchar,aktquest.monster,ctx) == 1:
                jz = datetime.datetime.now() + DD
                jz = jz.strftime('%d %m %Y %H %M %S')
                f = open("./cooldown/" + player + ".txt", "w")
                f.write(str(jz) + "\n")
                f.close()
                await ctx.send("Du hast die Quest erfolgreich abgeschlossen!")
                zubuchen(player, int(aktquest.belohnung))
            else:
                jz = datetime.datetime.now() + DD
                jz = jz.strftime('%d %m %Y %H %M %S')
                f = open("./cooldown/" + player + ".txt", "w")
                f.write(str(jz) + "\n")
                f.close()
                await ctx.send("Du hast die Quest leider nicht geschafft :(")
        else:
            await ctx.send("Du hast Coooooooooooooooooooooooldoooooooooown, bro.")



@client.command(pass_context=True)
async def fight(ctx, arg):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        global einladung
        global player2
        player = str(ctx.message.author)
        player2= str(arg)
        einladung = True
        await ctx.send(player2 + " - Du wurdest herausgefordert! Wenn du annehmen willst schreibe !accept GELDEINSATZ")
        player2 = player

@client.command(pass_context=True)
async def accept(ctx, arg):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        global einladung
        global player2
        if einladung == True:
            player = str(ctx.message.author)
            einladung = False
            f = open("./characters/" + player + ".txt", "r")
            aktchar = str(f.read())
            f.close()
            f = open("./characters/" + player2 + ".txt", "r")
            aktchar2 = str(f.read())
            f.close()

            if int(arg) <= 0:
                await ctx.send("Wo ist deine Ehre bro???")
                return
            if aktchar == "None" or aktchar2 == "None":
                await ctx.send("Ihr müsst beide Charaktere besitzen!")
                return
            for char in Charaktere:
                if char.name == aktchar:
                    aktchar = char
                if char.name == aktchar2:
                    aktchar2 = char
            if aktchar == "Jan, der Cheater":
                aktchar = Jan1
            elif aktchar2 == "Jan, der Cheater":
                aktchar2 = Jan1
            print (aktchar)
            print (aktchar2)

            if await kämpfen(player,player2,aktchar,aktchar2,ctx) == 1:
                zubuchen(player, arg)
                abbuchen(player2, arg)
                await ctx.send(player + " hat gewonnen!")
            else:
                zubuchen(player2, arg)
                abbuchen(player,arg)
                await ctx.send(player2 + " hat gewonnen!")
        else:
            await ctx.send("Du hast keine offene Einladung!")





@client.command(pass_context=True)
async def wetten(ctx, arg):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        f = open("./players/" + player + ".txt", "r")
        data = f.read()
        f.close()
        print(data)
        if int(data) < int(arg):
            await ctx.send("Du bist zu arm, Scrub!")
            return
        if int(arg) == 0:
            await ctx.send("Troll nicht...")
            return
        if int(arg) < 0:
            await ctx.send("Disclaimer: Cheaten versaut den Spielspaß anderer, don't be this person.")
            return
        bla = wettspiel(ctx)
        if bla:
            new_money = int(data) - int(arg)
            await ctx.send("Du hast leider verloren!")
        else:
            new_money = int(data) + int(arg)
            await ctx.send("Du hast gewonnen!")
        f = open("./players/" + player + ".txt", "w")
        f.write(str(new_money))
        f.close()

@client.command(pass_context=True)
async def würfeln(ctx, arg,arg2):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        f = open("./players/" + player + ".txt", "r")
        data = f.read()
        f.close()
        print(data)
        if int(data) < int(arg2):
            await ctx.send("Du bist zu arm, Scrub!")
            return
        if int(arg2) == 0:
            await ctx.send("Troll nicht...")
            return
        if int(arg2) < 0:
            await ctx.send("Disclaimer: Cheaten versaut den Spielspaß anderer, don't be this person.")
            return
        bla = randint(1,6)
        if bla == int(arg):
            new_money = int(data) + int(arg2) + int(arg2) + int(arg2) + int(arg2) + int(arg2) + int(arg2) + int(arg2)
            await ctx.send("Du hast eine " + str(bla) + " gewürfelt! Bist du ein Magier?")
        else:
            new_money = int(data) - 1*(int(arg2))
            await ctx.send("Du hast eine " + str(bla) + " gewürfelt! Das kannst du doch wohl besser...")
        f = open("./players/" + player + ".txt", "w")
        f.write(str(new_money))
        f.close()


@client.command(pass_context=True)
async def konto(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        f = open("./players/" + player + ".txt", "r")
        await ctx.send("Du hast momentan " + f.read() + " Ohana-Dollar auf deinem Konto!")


@client.command(pass_context=True, help="Show Arena Ranking")
async def aranking(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        d = {}
        highscore = []
        highscore2 = []
        i= 0
        for user in os.listdir('./arena/'):
            f = open("./arena/" + user, "r")
            data = str(f.read())
            data = int(data)
            data2 = user.replace(".txt"," ")
            f.close()
            d[data2] = data

            highscore.append(data2)
            highscore2.append(data)
            """
            await ctx.send(data2)
            await ctx.send(data)
            """
        highscore.sort(reverse=True)
        print (highscore)
        print (d)
        a = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for item in a:
            await ctx.send(str(i+1) + ". " + str(item[i][1]) + " Arena-Punkte - " + str(item[i][2]))
            i += 1
        """
        for i in range (1,len(highscore)-1):
            if str(highscore[i-1]) == "Flawless Desire#1525 " or str(highscore[i-1]) == "Flawy#1450 ":
                print (str(highscore[i-1]))
                del d[highscore[i-1]]
                highscore.pop(i-1)
                highscore.sort(reverse=True)
            await ctx.send(str(i) + ". " + str(highscore[i-1]) + " Arena-Punkte - " +  str(d[highscore[i-1]]))
        """
@client.command(pass_context=True)
async def ranking(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        d = {}
        highscore = []
        for user in os.listdir('./players/'):
            f = open("./players/" + user, "r")
            data = str(f.read())
            data = int(data)
            data2 = user.replace(".txt"," ")
            f.close()
            d[data] = data2

            highscore.append(data)
            """
            await ctx.send(data2)
            await ctx.send(data)
            """
        highscore.sort(reverse=True)
        print (highscore)
        for i in range (1,len(highscore)-1):
            if str(d[highscore[i-1]]) == "Flawless Desire#1525 " or str(d[highscore[i-1]]) == "Flawy#1450 ":
                print (str(d[highscore[i-1]]))
                del d[highscore[i-1]]
                highscore.pop(i-1)
                highscore.sort(reverse=True)
            await ctx.send(str(i) + ". " + str(highscore[i-1]) + " Ohana-Dollar - " +  d[highscore[i-1]])

        """
        print(dict(sorted(d.items())))
        print (json.dumps(d, sort_keys=True))
        """

@client.command(pass_context=True)
async def add(ctx, arg, arg2):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        if str(ctx.message.author) != "Flawless Desire#1525":
            print (ctx.message.author)
            await ctx.send("Du kommst hier nicht vorbei!")
            return
        elif str(ctx.message.author) == "Flawless Desire#1525":
            f = open("./players/" + arg + ".txt", "r")
            geldnow = f.read()
            f.close()
            geld = int(geldnow) + int(arg2)
            f = open("./players/" + arg + ".txt", "w")
            f.write(str(geld))
            f.close()
            await ctx.send("Du hast erfolgreich " + arg2 + " Ohana-Dollar an " + arg + " verschenkt!")

@client.command(pass_context=True)
async def send(ctx, arg, arg2):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        f = open("./players/" + player + ".txt", "r")
        geld = f.read()
        f.close()
        if int(arg2) > int(geld):
            await ctx.send("Bro, you ain't got no money")
            return
        if int(arg2) < 0:
            await ctx.send("Nanana, wer will denn hier cheaten?")
            return
        if os.path.isfile(("./players/" + arg + ".txt")):
            f = open("./players/" + player + ".txt", "r")
            print (player)
            geldnow = f.read()
            geld = int(geldnow) - int(arg2)
            f.close()
            f = open("./players/" + player + ".txt", "w")
            f.write(str(geld))
            f.close()
            f = open("./players/" + arg + ".txt", "r")
            geldnow = f.read()
            f.close()
            geld = int(geldnow) + int(arg2)
            f = open("./players/" + arg + ".txt", "w")
            f.write(str(geld))
            f.close()
            await ctx.send("Du hast erfolgreich " + arg2 + " Ohana-Dollar an " + arg + " überwiesen!")
        else:
            await ctx.send("Den User gibt's nicht, du willst doch dein Geld nicht wegwerfen, oder?")
            return



@client.command(pass_context=True)
async def shop(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        global shop
        await ctx.send("Im Shop sind momentan folgende Charaktere: ")
        print (shop)
        await ctx.send(shop[0].name)
        await ctx.send(shop[1].name)
        await ctx.send(shop[2].name)

@client.command(pass_context=True, help="Refresh the shop for 10k")
async def refresh(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        global shop
        player = str(ctx.message.author)
        f = open("./players/" + player + ".txt", "r")
        geld = int(f.read())
        f.close()
        if 10000 > geld:
            await ctx.send("Erst zahlen, dann gibt's die Abkühlung.")
            return
        else:
            newGeld = geld - 10000
            f = open("./players/" + player + ".txt", "w")
            f.write(str(newGeld))
            f.close()
        shop = random.sample(Charaktere, 3)
        await ctx.send("Erfolgreich refresht!")

@client.command(pass_context=True)
async def sug(ctx, *args):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        f = open("./suggestions.txt", "a")
        for arg in args:
            f.write(arg)
            f.write(" ")
        f.write("\n")
        f.close()

@client.command(pass_context=True, help="Show the stats of a champion in the shop")
async def stats(ctx, arg):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        if int(arg) > 3:
            await ctx.send("Kann da jemand nicht bis 3 zählen?")
            return
        await ctx.send(shop[int(arg)-1].ausgabe())

@client.command(pass_context=True, help="Show the stats of your champion")
async def cstats(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        f = open("./characters/" + player + ".txt", "r")
        aktchar = str(f.read())
        f.close()
        if aktchar == "Jan, der Cheater":
            await ctx.send(Jan1.ausgabe())
            return
        print (aktchar)
        for char in Charaktere:
            if str(char.name) == aktchar:
                aktchar = char
        await ctx.send(aktchar.ausgabe())

@client.command(pass_context=True, help="Show the cost of all upgrades")
async def upgrades(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        ups = ""
        await ctx.send("Angriffsupgrades: ")
        for i in range(1,16):
            ups += ("Level: " + str(i) + " - " + str(atkkosten[i]) + " Ohana-Dollar! \n")
        await ctx.send(ups)
        ups = ""
        await ctx.send("HP-Upgrades: ")
        for i in range(1, 16):
            ups += ("Level: " + str(i) + " - " + str(hpkosten[i]) + " Ohana-Dollar! \n")
        await ctx.send(ups)
        ups = ""
        await ctx.send("Speed-Upgrades: ")
        for i in range(1, 16):
            ups += ("Level: " + str(i) + " - " + str(speedkosten[i]) + " Ohana-Dollar! \n")
        await ctx.send(ups)
        ups = ""
        await ctx.send("Dodge-Upgrades: ")
        for i in range(1, 16):
            ups += ("Level: " + str(i) + " - " + str(dodgekosten[i]) + " Ohana-Dollar! \n")
        await ctx.send(ups)
        ups = ""
        await ctx.send("Income-Upgrades: ")
        for i in range(1, 16):
            ups += ("Level: " + str(i) + " - " + str(incomekosten[i]) + " Ohana-Dollar! \n")
        await ctx.send(ups)
        ups = ""


@client.command(pass_context=True, help="Zeigt deinen aktuellen Charakter!")
async def char(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        f = open("./characters/" + player + ".txt", "r")
        aktchar = str(f.read())
        f.close()
        await ctx.send("Dein aktueller Charakter ist: "  + aktchar)

@client.command(pass_context=True, help="Zeigt alle Charaktere!")
async def chars(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        for char in Charaktere:
            await ctx.send(char.ausgabe())
            await ctx.send("-----------------------")

@client.command(pass_context=True, help="Zeigt alle Quests!")
async def quests(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        for q in allquests:
            await ctx.send(q.ausgabe())
            await ctx.send("-----------------------")

@client.command(pass_context=True)
async def buy(ctx, arg):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        if int(arg) > 3:
            await ctx.send("Kann da jemand nicht bis 3 zählen?")
            return
        player = str(ctx.message.author)
        f = open("./players/" + player + ".txt", "r")
        geld = int(f.read())
        f.close()
        if int(shop[int(arg)-1].preis) > geld:
            await ctx.send("Die Würde des Menschen ist unantastbar.")
            return
        else:
            newGeld = geld - int(shop[int(arg)-1].preis)
            f = open("./players/" + player + ".txt", "w")
            f.write(str(newGeld))
            f.close()
            f=open("./characters/" + player + ".txt", "w")
            f.write(shop[int(arg)-1].name)
            f.close()
            await ctx.send("Glückwunsch du hast erfolgreich: " + shop[int(arg) - 1].name + " gekauft!")


@client.command(pass_context=True)
async def upgrade(ctx, arg):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        if int(arg) > 5:
            await ctx.send("Kann da jemand nicht bis 5 zählen??")
            return
        player = str(ctx.message.author)
        f = open("./players/" + player + ".txt", "r")
        geld = int(f.read())
        f.close()
        f = open("./stats/" + player + ".txt", "r")
        stats = f.readlines()
        f.close()
        atk = stats[0]
        hp = stats[1]
        spd = stats[2]
        dodge = stats[3]
        income = stats[4]
        if int(arg) == 1:
            print (atkkosten[int(atk)+1])
            if geld < atkkosten[int(atk)+1]:
                await ctx.send("Money, Money, Money - hast du nicht.")
                return
            else:
                abbuchen(player, atkkosten[int(atk)+1])
                stats[0] = str(int(atk)+1) +"\n"
                f = open("./stats/" + player + ".txt", "w")
                f.writelines(stats)
                f.close()
                await ctx.send("Du hast dein Angriff erfolgreich auf " + str(int(atk)+1) + " geupgradet!")
                return

        elif int(arg) == 2:
            print (hpkosten[int(hp)+1])
            if geld < hpkosten[int(hp)+1]:
                await ctx.send("Money, Money, Money - hast du nicht.")
                return
            else:
                abbuchen(player, hpkosten[int(hp)+1])
                stats[1] = str(int(hp)+1) +"\n"
                f = open("./stats/" + player + ".txt", "w")
                f.writelines(stats)
                f.close()
                await ctx.send("Du hast deine HP erfolgreich auf " + str(int(hp)+1) + " geupgradet!")
                return
        elif int(arg) == 3:
            print (speedkosten[int(spd)+1])
            if geld < speedkosten[int(spd)+1]:
                await ctx.send("Money, Money, Money - hast du nicht.")
                return
            else:
                abbuchen(player, speedkosten[int(spd)+1])
                stats[2] = str(int(spd)+1) +"\n"
                f = open("./stats/" + player + ".txt", "w")
                f.writelines(stats)
                f.close()
                await ctx.send("Du hast dein Speed erfolgreich auf " + str(int(spd)+1) + " geupgradet!")
                return
        elif int(arg) == 4:
            print (dodgekosten[int(dodge)+1])
            if geld < dodgekosten[int(dodge)+1]:
                await ctx.send("Money, Money, Money - hast du nicht.")
                return
            else:
                abbuchen(player, dodgekosten[int(dodge)+1])
                stats[3] = str(int(dodge)+1) +"\n"
                f = open("./stats/" + player + ".txt", "w")
                f.writelines(stats)
                f.close()
                await ctx.send("Du hast deine Dodgechance erfolgreich auf " + str(int(dodge)+1) + " geupgradet!")
                return
        elif int(arg) == 5:
            print (incomekosten[int(income)+1])
            if geld < incomekosten[int(income)+1]:
                await ctx.send("Money, Money, Money - hast du nicht.")
                return
            else:
                abbuchen(player, incomekosten[int(income)+1])
                stats[4] = str(int(income)+1) +"\n"
                f = open("./stats/" + player + ".txt", "w")
                f.writelines(stats)
                f.close()
                await ctx.send("Du hast dein Income erfolgreich auf " + str(int(income)+1) + " geupgradet!")
                return


@client.command(pass_context=True)
async def ups(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        f = open("./stats/" + player + ".txt", "r")
        stats = f.readlines()
        f.close()
        atk = stats[0]
        hp = stats[1]
        spd = stats[2]
        dodge = stats[3]
        income = stats[4]
        upsss = "Dein Angriff ist auf Stufe " + atk
        upsss += "Deine HP sind auf Stufe " + hp
        upsss += "Dein Speed ist auf Stufe " + spd
        upsss += "Dein Dodge ist auf Stufe " + dodge
        upsss += "Dein Income ist auf Stufe " + income
        await ctx.send(upsss)

@client.command(pass_context=True)
async def reg(ctx):
    if ctx.message.author == client.user:
        print ("wrong!")
        return
    else:
        player = str(ctx.message.author)
        print (player)
        print ("leggo")
        if os.path.isfile(("./players/" + player + ".txt")):
            print("evryth")
            await ctx.send("Du bist bereits registriert!")
        else:
            print("smth")
            f = open("./players/" + player + ".txt", "w")
            f.write("50")
            f.close()
            f=open("./characters/" + player + ".txt", "w")
            f.write("None")
            f.close()
            f = open("./stats/" + player + ".txt", "w")
            f.write("0" +"\n" + "0" +"\n" + "0" +"\n" + "0"+"\n" + "0")
            f.close()
            f = open("./cooldown/" + player + ".txt", "w")
            jz = datetime.datetime.now().strftime('%d %m %Y %H %M %S')
            f.write(str(jz) + "\n")
            f.close()
            await ctx.send("Du hast dich nun registriert!")

        """
        for user in os.listdir('./players'):
            if player + ".txt" == user:
                print ("smth")
                await ctx.send("Du hast dich bereits registriert!")
            else:
                print ("evryth")
                await ctx.send("Du bist nun registriert!")


"""

@client.event
async def on_message(message):
    if message.content.startswith("+poll") or message.content.startswith("+Poll"):
        messageContent = message.clean_content
        await message.add_reaction('👍')
        await message.add_reaction('👎')
    if message.content == '!stop':
        #await client.logout()
        pass
    await client.process_commands(message)

with open('token.txt') as tokenfile:
    TOKEN = tokenfile.readline()


client.run(TOKEN)