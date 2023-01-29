import discord
import os
import dotenv
import asyncio


from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


"""
Это для систем где есть файл .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)    
"""

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    #await load()
    await bot.tree.sync()
    print(f"{len(bot.guilds)} servers, {len(bot.users)} users \nБот запущен!" )

async def load():
    path_to_file = os.path.join("~/discord/cogs")
    for filename in os.listdir(path_to_file):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

@bot.tree.command(name="reboot", description="Перезапуск бота")
@commands.has_permissions(administrator=True)
async def restart(inter:discord.Interaction):
    await inter.response.send_message(f"Бот перезапускается Через 5 секунд")
    await asyncio.sleep(5)
    await bot.reload_extension("cogs.commands")


@bot.tree.command(name="shutdown", description="Экстренное выключение бота")
@commands.has_permissions(administrator=True)
async def restart(inter:discord.Interaction):
    await inter.response.send_message(f"Бот выключается Через 5 секунд")
    await asyncio.sleep(5)
    await exit()

    
bot.run(os.getenv("TOKEN"))
