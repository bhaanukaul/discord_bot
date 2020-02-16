import discord
from discord.ext import commands
import random
import json
import re
from config.config import bot
from config import emoji

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
def roll_multi_dice(dice):
    dice = dice.strip()
    try:
        roll, limit = map(int, dice.split('d'))
    except Exception:
        return 'Format has to be in NdN! e.x 1d6, 2d8, 3d4' 
    rolls = [random.randint(1, limit) for r in range(roll)]
    return rolls
