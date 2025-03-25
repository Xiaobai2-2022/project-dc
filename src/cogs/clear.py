import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear", aliases=["purge", "deleteall"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = None):
        if amount is None:
            await ctx.channel.purge()
            await ctx.send("✅ All messages are deleted!", delete_after=3)
        else:
            await ctx.channel.purge(limit=amount + 1)  # +1 to remove the command message too
            await ctx.send(f"✅ Deleted {amount} messages!", delete_after=3)

async def setup(bot):
    await bot.add_cog(Clear(bot))
