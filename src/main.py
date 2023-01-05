from nextcord.ext import commands
import os,nextcord,asyncio
from database import clinent,chack_database
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    bot = commands.AutoShardedBot(command_prefix='ax!', intents=nextcord.Intents.all())
    chack_database(clinent)
    @bot.event
    async def on_ready():
        print('Ready!')
    bot.load_extension("cogs.music")
    bot.load_extension("cogs.test")
    bot.load_extension("cogs.setup")
    bot.run(os.getenv("DISCORD_TOKEN"), reconnect=True)
