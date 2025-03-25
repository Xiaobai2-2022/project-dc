import os
from dotenv import load_dotenv

from discord.ext import commands
from dbms.user_manager import UserManager as UM

class UMCommands(commands.Cog):
    def __init__(self, bot, db_config):
        self.bot = bot
        self.um = UM(db_config)

    @commands.command(name="register")
    async def register(self, ctx, display_name: str | None):
    
        discord_id = ctx.author.id
        discord_name = ctx.author.name
        result = self.um.reg_user(discord_id, discord_name, display_name)
        print(result)
        await ctx.send(result)

    @commands.command(name="namechannel")
    async def namechannel(self, ctx, channel_name: str | None):

        discord_id = ctx.author.id
        result = self.um.set_channel_name(discord_id, channel_name)
        print(result)
        await ctx.send(result)

async def setup(bot):

    load_dotenv()

    db_config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }
    
    await bot.add_cog(UMCommands(bot, db_config))
