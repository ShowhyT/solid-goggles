import discord
import os
import asyncio


from discord.ext import commands
# from dotenv import load_dotenv


"""
Это для систем где есть файл .env Если на хостинге то закоментируем его
"""
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)


# Присваиваем переменную боту
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# Это @bot.event. Это главный запуск и проверка бота на работоспособность
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Работаю на 24/7"))
    await load()
    await bot.tree.sync()
    print(f"{len(bot.guilds)} servers, {len(bot.users)} users \nБот запущен!" )
# Метод load нужен для быстрой загрузки файлов из папки cogs
async def load():
    path_to_file = os.path.join("/discord/cogs")
    for filename in os.listdir(path_to_file):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

# И запуск бота с использованием .env
bot.run(os.getenv("TOKEN"))
