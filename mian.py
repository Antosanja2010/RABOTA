import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def helps(ctx):
    await ctx.send(f'Все команды: сложение:$add цифра цифра - складывает числа, $he - будет за вами повторять he сколько вы напишите, hello приветсвие с ботом')

bot.run("ваш токен")
