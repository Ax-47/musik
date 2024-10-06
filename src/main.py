from nextcord.ext import commands
from tasks.tonton420 import tonton
import os,nextcord
from database import CLINENT,GUILD,TONTON,chack_database
from dotenv import load_dotenv
import asyncio
async def main():
    load_dotenv()
    bot = commands.AutoShardedBot(command_prefix='ax!', intents=nextcord.Intents.all())
    chack_database(CLINENT)
    # tonton(os.getenv("YOUTUBE_KEY"),TONTON,GUILD,bot)
    @bot.event
    async def on_ready():
        print('Ready!')
    bot.load_extension("cogs.music")
    bot.load_extension("cogs.test")
    bot.load_extension("cogs.setup")
    bot.load_extension("cogs.events")
    await bot.start(os.getenv("DISCORD_TOKEN"), reconnect=True)
if __name__ == "__main__":
   asyncio.run(main())
    
