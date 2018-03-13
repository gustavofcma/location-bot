# guga-test-bot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import telepot
import sqlite3
import os

path = os.environ['PKM_BOT_HOME']+'/database.db'
d_bot = os.environ['PKM_BOT_TELEGRAM_KEY']
t_bot = telepot.Bot(os.environ['PKM_BOT_DISCORD_KEY'])

t_chat_id = -273888005

@bot.event
async def on_ready():
    print("Ready when you are")
    print("I am running on " + bot.user.name)
    print("With the ID: " + bot.user.id)

async def logOnDB(_message, _path):
    conn = sqlite3.connect(_path)
    cursor = conn.cursor()
    _embed = _message.embeds
    if (_message.embeds):
        _texto = str(_embed[0]['description'])
        _iv = _texto[_texto.find('IVs:'):_texto.find(')')+1]
        _localtitulo = str(_embed[0]['title'])
    else:
        _iv = str(_message.content)
        _localtitulo = str(_message.channel)
    #_texto = str(_embed[0])
    _autor = str(_message.author)[:str(_message.author).find('#')-1]
    
    cursor.execute("""INSERT INTO TESTE (AUTOR, LOCALTITULO, TEXTO) VALUES (?,?,?)""", (_autor, _localtitulo, _iv))
    conn.commit()
    conn.close()
    await asyncio.sleep(1)
    
@bot.event
async def on_message(message, timeout=10,):
    #print("[SERVER LOG] :: {} SAYS {} ON {}/{}".format(str(message.author),str(message.content),str(message.server),str(message.channel)))
    #await bot.send_message(discord.Object(id='408978663183351813'),message.content)
    await logOnDB(message, path)
    #await logOnDB("CONCAT", "{} {} {} {}".format(str(message.author),str(message.content),str(message.server),str(message.channel)), path)
    print("Logged")
    #await t_bot.sendMessage(t_chat_id,'{} / {}'.format(str(message.server),str(message.channel)))
    #await logOnDB(message,path)
    await bot.process_commands(message)

bot.run(d_bot, bot=False)

# server neoscan 310074992509583372
