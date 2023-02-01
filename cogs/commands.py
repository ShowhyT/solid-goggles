import discord
import asyncio

from discord.ext import commands
from discord import app_commands

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Команда для проверки сервера")
    async def google(self, inter:discord.Interaction):
        await inter.response.send_message(f"Ping! `{int(self.bot.latency * 1000)}` ms ", ephemeral=True)
    
    @app_commands.command(name="ban", description="Команда для бана игрока")
    @commands.has_permissions(ban_members=True)
    async def ban(self, inter:discord.Interaction, member:discord.Member,time:int,  *, reason:str=None):
        await inter.guild.ban(member, reason=reason)
        await inter.response.send_message(f'{member.mention} был забанен по причине {reason}')
        await asyncio.sleep(time)
        await inter.guild.unban(member, reason=reason)
        await inter.response.send_message(f'{member} был разбанен')

    @app_commands.command(name="unban", description="Команда для разбана игрока")
    @commands.has_permissions(ban_members=True)
    async def unban(self, inter:discord.Interaction, member: discord.Member,reason:str=None):
        author = inter.author
        await inter.guild.unban(member, reason=reason)
        await inter.response.send_message(f'{member.mention} был разбанен {author.mention}')



async def setup(bot):
    await bot.add_cog(Command(bot))
    print(f">Extension {__name__} is ready")