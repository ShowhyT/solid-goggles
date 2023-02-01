import discord
import asyncio

from discord.ext import commands
from discord import app_commands


class Services(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="reboot", description="Перезапуск бота")
    @commands.has_permissions(administrator=True)
    async def restart(self, inter: discord.Interaction):
        await inter.response.send_message(f"Бот перезапускается Через 5 секунд")
        await asyncio.sleep(5)
        await self.bot.reload_extension("cogs.commands")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx):
        await ctx.send(f"Бот выключается Через 5 секунд")
        print(5)
        await asyncio.sleep(1)
        print(4)
        await asyncio.sleep(1)
        print(3)
        await asyncio.sleep(1)
        print(2)
        await asyncio.sleep(1)
        print(1)
        await asyncio.sleep(1)
        exit()


async def setup(bot):
    await bot.add_cog(Services(bot))
    print(f">Extension {__name__} is ready")