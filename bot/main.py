import discord
from discord.ext import commands
import random
import json
import re
from bot_commands import dnd
from config.auth import DISCORD_TOKEN


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)
bot.load_extension("bot_commands.dnd.dnd")
bot.load_extension("bot_commands.fun.fun")



@bot.command()
async def test_emoji(ctx):
    await ctx.send("<:PogChamp:673744590670397493>")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# with open("config/auth.json") as auth_token:
#     token = json.load(auth_token)
bot.run(DISCORD_TOKEN)
