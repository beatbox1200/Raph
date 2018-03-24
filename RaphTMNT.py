import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='R!')

@bot.event
async def on_ready():
    print ("Lets kick some Discord Butt!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Do you really think I want to play Ping Pong right now?")
    print ("user has attempted to ping")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("This is not my typical job, but since Leo is acting neutral, I guess I can help you with this:")
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.kick(user)
    await bot.say(":boot: Thats what you get, Krang face!".format(user.name))

@bot.command(pass_context=True)
async def raphstory(ctx):
    await bot.say("I had many past experiences with people and my brothers that make me upset. I started to develop this feeling in my body where I get upset over the most childish things. Not alot of people understand how I feel, and they just make it worse by trying to stop it. It's my personality, and they should understand that by now.")

@bot.command(pass_context=True)
async def tease_raph(ctx):
    await bot.say(":rage: Shut up, and stop trying to make me more upset than I already am! :rage:")

@bot.command(pass_context=True)
async def hey(ctx):
    await bot.say("Whats up. I am kinda in a bad mood right now.")

@bot.command(pass_context=True)
async def bye(ctx):
    await bot.say(":triumph: Bye. See you later... I guess. :triumph:")

bot.run(os.getenv('TOKEN'))
