import discord
from discord.ext import commands
import yaml

with open('config.yml') as f:
    config = yaml.safe_load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
bot.run(config['token'])
