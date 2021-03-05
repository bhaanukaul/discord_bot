import discord
from discord.ext import commands
import random
import json
import re
import requests
from ..utils import emoji
from ...config.auth import TENOR_TOKEN

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def boop(self, ctx,*,boopee=None):
        tenor_search_url = f"https://g.tenor.com/v1/search?q=anime+boop+nose&key={TENOR_TOKEN}"
        gif_request = requests.get(tenor_search_url)
        gif_results = gif_request.json()["results"]
        random_gif = random.choice(gif_results)
        gif_url = random_gif["media"][0]["mediumgif"]["url"]
        print(f"boopee: {boopee}")
        if boopee == None:
            await ctx.send(f"::: {ctx.author.mention} is booping ... no one?\n{gif_url}\n:::")
        else:
            await ctx.send(f"::: {ctx.author.mention} booped {boopee}?\n{gif_url}\n:::")
        return


def setup(bot):
    bot.add_cog(Fun(bot))