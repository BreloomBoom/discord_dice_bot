import re
import random
import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.tree.command(name='r', description='Rolls one or more dice')
@discord.app_commands.describe(rolls='What rolls would you like? e.g. "6 20 4" rolls a d6, d20 then d4')
async def r(interaction: discord.Interaction, rolls: str):
    response = []
    summary = []
    for roll in rolls.strip().split():
        if re.match('^\d+$', roll) is None or int(roll) == 0:
            response.append(f'{interaction.user.display_name},  "{roll}" is not a positive integer')
        else:
            rolled = random.randint(1, int(roll))
            response.append(f'{interaction.user.display_name} rolled a `{rolled}` using a `d{roll}`')
            summary.append(str(rolled))

    if len(summary) > 1:
        response.append(f'Roll Summary: `{" ".join(summary)}`')
    await interaction.response.send_message('\n'.join(response))

bot.run(TOKEN)