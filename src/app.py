import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

import asyncio

# Set up discord bot
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

@bot.command(name="reload")
@commands.is_owner()
async def reload(ctx, extension: str = '.'):
    await unload(ctx, extension)
    await load(ctx, extension)


@bot.command(name="load")
@commands.is_owner()
async def load(ctx, extension: str = '.'):
    if extension == '.':
        for filename in os.listdir("/home/ubuntu/project-dc/src/cogs"):
            if filename.endswith(".py"):
                if not f"cogs.{extension}" in bot.extensions:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    await ctx.send(f"Loaded {filename[:-3]}")
                    print(f"Loaded {filename[:-3]}")
    else:
        if not f"cogs.{extension}" in bot.extensions:
            await bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"Loaded {extension}")
            print(f"Loaded {extension}")

@bot.command(name="unload")
@commands.is_owner()
async def unload(ctx, extension: str = '.'):
    if extension == '.':
        for filename in os.listdir("/home/ubuntu/project-dc/src/cogs"):
            if filename.endswith(".py"):
                if f"cogs.{filename[:-3]}" in bot.extensions:
                    await bot.unload_extension(f"cogs.{filename[:-3]}")
                    await ctx.send(f"Unloaded {filename[:-3]}")
                    print(f"Unloaded {filename[:-3]}")
    else:
        if f"cogs.{extension}" in bot.extensions:
            await bot.unload_extension(f"cogs.{extension}")
            await ctx.send(f"Unloaded {extension}")
            print(f"Unloaded {extension}.")

# @bot.command(name="shutdown")
# @commands.is_owner()
# async def shutdown(ctx):
#     await ctx.channel.purge()
#     await ctx.send("Goodbye... 👋", delete_after=5)
#     await asyncio.sleep(5)
#     await bot.close()

if( __name__ == "__main__" ) :

    load_dotenv()

    TOKEN = os.getenv("DISCORD_TOKEN")
    if TOKEN is None:
        raise ValueError("DISCORD_TOKEN is not set in the .env file.")

    RUN_MODE = os.getenv("RUN_MODE")
    if RUN_MODE is None:
        RUN_MODE = "PROD"
        
    bot.run(TOKEN)
