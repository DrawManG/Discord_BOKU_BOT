import discord
from discord.ext import commands
import random

from discord.ext.commands import bot

import conf

'''
Создатель DrawManG : https://github.com/DrawManG/
Информация о боте в кратце....
В начале идёт подключение и включение бота. Если всё гуд то напишет bot_start!
Комманды, которые выполняет бот на данный момент:

"-T" - показывает сколько дней осталось до прибытия Тимика из армухи 
"-W" - показывает погоду на сегодняшний день 
“-G” - рандомно выбирает игру из списка
”-Gview” - показать список игр
“-Gadd“ - добавить игру (без пробелов «-Gadd CS1.6»)
“-Gdel“ - удалить игру (-Gdel DOTA2)
"-Grm" - удалить игру по ID (-Grm 1) [айди начинается с 1]
“-G_cb“ - восстановить массив игр прежним
"-Gid" - Берёт рандом из выбранных игр (пример: "-Gid 123" и из этих 3-ёх игр он делает рандом. Можно цифры повторять! (но шанс тогда выпода этого числа увеличивается)

'''

#подруб
client_on = commands.Bot(command_prefix='-')
@client_on.event
#если гуд подруб то пишет это
async def on_ready():
    print('bot_start')
#Команда возврата друга из армухи
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

# Парсер погоды в бот (лень было разбираться с библиотеками)
@client_on.command(pass_context=True)
async def W(ctx):
     import requests
     from bs4 import BeautifulSoup

     url = 'https://www.meteonova.ru/frc/27612.htm'
     response = requests.get(url)
     soup = BeautifulSoup(response.text, 'lxml')
     quotes = soup.find_all('td', class_='temper')
     pogoda_now = str(quotes[1]).replace('<td class="temper">', '').replace('</td>', '')
     await ctx.send("Погода сейчас: " + str(pogoda_now))

#Генератор игры в какую играть
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

#Тестовая тема, по идеи он должен был кидать стикер, но он другого мнения
@client_on.command(pass_context=True)
async def S(ctx,arg):
    if str(arg) == 'вояка':
        await ctx.send(':voyaka: ')

#Добавление игры в список
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

#Удаление игры из списка
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

#Показать все игры
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
#Не знаю зачем она нужна, так как по факту статического списка нет... Ну вообщем он возвращает список в такой вид
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
#Очищалка всех игр
@client_on.command(pass_context=True)
async def G_clear(ctx):
  try:
    edit_file = []
    file = open('Game.txt', 'w')
    i = 0
    while i < len(edit_file):
        file.write(edit_file[i] + "\n")
        i = i + 1
    file.close()
    await ctx.send('Игры восстановлены к заводским параметрам: ' + str(edit_file))
  except:
      await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')
#Удалить по айди игру из списка
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
#Зарандомить игру из выбранного списка (айдишек)
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
        i = 0
        #выше код для сортировки ввода
        print('123        ' + str(len(str(set(games)))))
        vibor = random.randint(0, len(games) - 1 )
        await ctx.send('Из игр: '+str(set(games))+ ' я выбрал : ' + str(games[vibor]))

#Админ комманды, но они пока не понадобятся...
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
         #await ctx.send(file=discord.File('2.PNG')) -- Если нужно выслать картинку рабочего стола.
  except:
            await ctx.send('Или ты чёт не так делаешь, или команда больше не работает')
token = conf.TOKEN
client_on.run(token)
'''
version 1.6
'''