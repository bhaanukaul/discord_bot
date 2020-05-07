import discord
from discord.ext import commands
import random
import json
import re
from config import emoji
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.command()
async def roll(ctx,*, dice=None):
    """Rolls a dice in NdN format."""
    print(f"dice: {dice}")
    if dice is None:
        roll = random.randint(1, 20)
        if roll == 1:
            result = f"F's in chat for {ctx.author.mention}. They rolled a 1."
        elif roll == 20:
            result =  f"{emoji.emojis['PogChamp']} for {ctx.author.mention}. They rolled a nat 20!"
        else:
            result = f"{ctx.author.mention} rolled 1d20: {roll}"
        await ctx.send(result)
        return
    else:
        dice = dice.split("+")
        if len(dice) == 1:
            rolls = roll_multi_dice(dice[0])
            result = f"{ctx.author.mention} rolled {dice} => {rolls} with sum: {sum(rolls)}"
        elif dice[1].strip().isnumeric():
            to_add = int(dice[1].strip())
            rolls = roll_multi_dice(dice[0].strip())
            result = f"{ctx.author.mention} rolled {dice} => {rolls} with sum: {sum(rolls)+to_add}"
        else:
            roll_sum = 0
            all_rolls = []
            for i_roll in dice:
                roll_result = roll_multi_dice(i_roll)
                all_rolls.append(roll_result)
                roll_sum += sum(roll_result)
            result = f"{ctx.author.mention} rolled {dice} => {all_rolls} with sum: {roll_sum}"
        await ctx.send(result)
        return

@bot.command()
async def test_emoji(ctx):
    await ctx.send("<:PogChamp:673744590670397493>")


def roll_multi_dice(dice):
    dice = dice.strip()
    try:
        roll, limit = map(int, dice.split('d'))
    except Exception:
        return 'Format has to be in NdN! e.x 1d6, 2d8, 3d4' 
    rolls = [random.randint(1, limit) for r in range(roll)]
    return rolls

def roll_and_add(dice, to_add):
    rolls, dice_sum = do_roll(dice)
    dice_sum = (dice_sum+to_add)
    return (rolls, dice_sum)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


with open("config/auth.json") as auth_token:
    token = json.load(auth_token)
bot.run(token["token"])
