import discord
from discord.ext import commands
import random

from discord.ext.commands import bot

import conf

client_on = commands.Bot(command_prefix='-')


# .help

@client_on.event
async def on_ready():
    print('bot_start')

@client_on.command(pass_context=True)
async def T(ctx):
    try:
     import datetime
     now = datetime.datetime.today()
     NY = datetime.datetime(2021, 11, 30)
     d = NY - now
     mm, ss = divmod(d.seconds, 60)
     hh, mm = divmod(mm, 60)

     await ctx.send('До возвращения Тимика:  {} дней {} часа и {} минут'.format(d.days, hh,mm))
    except:
     await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')


@client_on.command(pass_context=True)
async def W(ctx):
    #try:
     import requests
     from bs4 import BeautifulSoup

     url = 'https://www.meteonova.ru/frc/27612.htm'
     response = requests.get(url)
     soup = BeautifulSoup(response.text, 'lxml')
     quotes = soup.find_all('td', class_='temper')
     pogoda_now = str(quotes[1]).replace('<td class="temper">', '').replace('</td>', '')
     await ctx.send("Погода сейчас: " + str(pogoda_now))
    #except:
     #await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')



@client_on.command(pass_context=True)

async def G(ctx):
    try:
     edit_file = []
     read_massive = open('Game.txt')
     for line in read_massive:
        edit_file.append(str(line))
     vibor = random.randint(1, len(edit_file))
     await ctx.send("Бот выбрал игру: " + str(edit_file[vibor - 1]))
    except:
     await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')

@client_on.command(pass_context=True)
async def S(ctx,arg):
    if str(arg) == 'вояка':
        await ctx.send(':voyaka: ')

@client_on.command(pass_context=True)
async def Gadd(ctx, arg):
  try:
    edit_file = []
    read_massive = open('Game.txt')
    for line in read_massive:
        edit_file.append(str(line).replace("\n",""))
    edit_file.append(str(arg))
    read_massive.close()
    file = open('Game.txt','w')
    i = 0
    while i < len(edit_file):
        file.write(edit_file[i] + "\n")
        i = i + 1
    file.close()
    await ctx.send('Игра добавлена, теперь список такой: ' + str(edit_file))
  except:
      await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')

@client_on.command(pass_context=True)
async def Gdel(ctx, arg):
  try:
    edit_file = []
    read_massive = open('Game.txt')
    for line in read_massive:
        edit_file.append(str(line).replace("\n", ""))
    var = [x for x, y in enumerate(edit_file) if y.split()[0] == arg]
    del edit_file[var[0]]
    read_massive.close()
    file = open('Game.txt', 'w')
    i = 0
    while i < len(edit_file):
        file.write(edit_file[i] + "\n")
        i = i + 1
    file.close()
    await ctx.send('Игра удалена, теперь список такой: ' + str(edit_file))
  except:
      await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')

@client_on.command(pass_context=True)
async def Gview(ctx):
  try:
    edit_file = []
    read_massive = open('Game.txt')
    for line in read_massive:
        edit_file.append(str(line).replace("\n", ""))
    read_massive.close()
    await ctx.send('Ваш список игр: ' + str(edit_file))
  except:
      await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')

@client_on.command(pass_context=True)
async def G_cb(ctx):
  try:
    edit_file = ['Enlisted','DOTA2','WARFARE','RainBowSix','StarWars_Battlefront2','GTA5']
    file = open('Game.txt', 'w')
    i = 0
    while i < len(edit_file):
        file.write(edit_file[i] + "\n")
        i = i + 1
    file.close()
    await ctx.send('Игры восстановлены к заводским параметрам: ' + str(edit_file))
  except:
      await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')

@client_on.command(pass_context=True)
async def Grm(ctx, arg):
  try:
    edit_file = []
    read_massive = open('Game.txt')
    for line in read_massive:
        edit_file.append(str(line).replace("\n", ""))
    del edit_file[int(arg) - 1]
    read_massive.close()
    file = open('Game.txt', 'w')
    i = 0
    while i < len(edit_file):
        file.write(edit_file[i] + "\n")
        i = i + 1
    file.close()
    await ctx.send('Игра удалена, теперь список такой: ' + str(edit_file))
  except:
      await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')

@client_on.command(pass_context=True)
async def Gid(ctx, arg):
        test_num = []
        edit_file = []
        games=[]
        read_massive = open('Game.txt')
        for line in read_massive:
            edit_file.append(str(line).replace("\n", ""))
        read_massive.close()

        for num in list(arg):
            print(num)
            num = int(num)- 1 # id
            games.append(edit_file[num])
            #random_id.append(edit_file[num])
        i = 0

        #выше код для сортировки ввода
        print('123        ' + str(len(str(set(games)))))
        vibor = random.randint(0, len(games) - 1 )

        await ctx.send('Из игр: '+str(set(games))+ ' я выбрал : ' + str(games[vibor]))



@client_on.command(pass_context=True)
async def ADMIN_COMMAND_INFO(ctx, arg):
  try:
    if str(arg)== 'TOKEN':
        await ctx.send(str(conf.TOKEN))
    if str(arg)== 'ID_CHANEL':
        await ctx.send(str(conf.DISCORD_ID_CHANEL))
    if str(arg)== 'MESSAGE_ID':
        await ctx.send(str(conf.MESSAGE_ID))
    if str(arg)== 'PICTURE':
        await ctx.send(file=discord.File('1.jpg'))
    if str(arg)== 'GIF':
        await ctx.send(file=discord.File('1.gif'))
    if str(arg) == 'SCREEN':

         from PIL import ImageGrab
         img = ImageGrab.grab()
         img.save("2.PNG", "PNG")
         await ctx.send('Пошёл нахуй чертила :D')
         #await ctx.send(file=discord.File('2.PNG'))
  except:
            await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')








# connect
token = conf.TOKEN
client_on.run(token)
