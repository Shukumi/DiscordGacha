import os
import random

import discord

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
from random import choices
nicksn = ["Niko, vom Okusho-Clan", "Niko-Biko", "Ich bin ein Troll", "Niko-Rokushoo, der Zweite", "Nikobärchi"]
nicksr = ["Suche ELOBOOST | PN ME MIT PREIS", "Ich bin cool, KAPPA" , "BIETE Nachhilfe im Boosted-Sein", "Iron-Scrub"]

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

client = commands.Bot(command_prefix="!")


async def passive_income():
    server = client.get_server('283389299645480982')
    robin = server.get_member('266240845437599760')
    print (robin.nick)
    await robin.edit(nick = "Kann mir jemand LoL beibringen")
    print(robin.nick)
    sleep(20)
    passive_income()


@client.event
async def on_ready():
    print("Flawy meldet sich zum Start!")
    #await start_new_thread(passive_income,())
    while True:
        server = client.get_guild(283389299645480982)
        robin = server.get_member(266240845437599760)
        niko = server.get_member(484033543518027806)
        try:
            print(robin.nick)
            await discord.kick(robin)
            nickr = random.choice(nicksr)
            await robin.edit(nick=nickr)
            sleep(50)
        except:
            print ("Robin ist nicht aufm Discord")
        #if robin.nick != "Suche ELOBOOST | PN ME MIT PREIS":

        nickn = random.choice(nicksn)
        #await niko.edit(nick=nickn)
        sleep(50)

client.run("NDg3OTg3ODE1ODgwMzI3MTg4.XrCF-w.GAdKlbqj4gu1xnUVBWdaKdTsBLg")