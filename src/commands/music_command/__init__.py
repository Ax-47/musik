import re

from nextcord import Interaction, slash_command
from nextcord.ext import commands
from nextcord.ext.commands import AutoShardedBot

import lavalink
from database import SPOTIFY_ID, SPOTIFY_SECRET
from musik import player as pyer
from spotify import *

from .auto_play import *
from .clean import *
from .disconnect import *
from .filter_equalizer import *
from .info_filter import *
from .join import *
from .karaoke import *
from .now import *
from .pause import *
from .play import *
from .queue_ import *
from .remove import *
from .repeat import *
from .Rotation import *
from .seek import *
from .shuffle import *
from .skip import *
from .smoothing import *
from .stop import *
from .timescale import *
from .TV import *
from .volume import *
from .vote import *

URL_RX = re.compile(r"https?://(?:www\.)?.+")


class Musik:
    def __init__(self, bot: AutoShardedBot, guild_coll) -> None:
        self.bot = bot
        self.cache = None
        self.spotify_client: Client
        self.guild = guild_coll
        if not hasattr(bot, "lavalink"):
            self.bot.lavalink = lavalink.Client(896217686630101002)
            # Host, Port, Password, Region, Name
            self.bot.lavalink.add_node(
                "localhost", 2333, "youshallnotpass", "sg", "default-node"
            )

            self.spotify_client = Client(SPOTIFY_ID, SPOTIFY_SECRET)
        self.lavalink = self.bot.lavalink

    @lavalink.listener(lavalink.events.TrackStartEvent)
    async def TrackEndEvent_hook(self, event: lavalink.events.TrackStartEvent):
        if event.player.auto_play:
            return await auto_play(self, event.player)
        guild = self.bot.get_guild(event.player.guild_id)
        if guild.voice_client is not None and not event.player.queue:
            return await guild.voice_client.disconnect(force=True)

    @lavalink.listener(lavalink.events.QueueEndEvent)
    async def track_hook(self, event: lavalink.events.QueueEndEvent):
        guild = self.bot.get_guild(event.player.guild_id)
        if guild.voice_client is not None:
            return await guild.voice_client.disconnect(force=True)

    def unload(self):
        self.bot.lavalink._event_hooks.clear()

    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

    async def join_to_channel(
        self, Inter: Interaction | commands.context.Context, type: bool = False
    ) -> bool:
        return await join(self, Inter, type)

    async def disconnect(self, Inter: Interaction | commands.context.Context):
        await disconnect(self, Inter)

    async def play(self, Inter: Interaction | commands.context.Context, query: str):
        await play(self, Inter, query)

    async def skip(self, Inter: Interaction | commands.context.Context):
        await skip(self, Inter)

    async def stop(self, Inter: Interaction | commands.context.Context):
        await stop(self, Inter)

    async def pause(self, Inter: Interaction | commands.context.Context):
        await pause(self, Inter)

    async def now(self, Inter: Interaction | commands.context.Context):
        await now(self, Inter)

    async def remove(self, ctx: Interaction | commands.context.Context, index: int):
        await remove(self, ctx, index)

    async def repeat(self, Inter: Interaction | commands.context.Context, type: int):
        await repeat(self, Inter, type)

    async def shuffle(self, Inter: Interaction | commands.context.Context):
        await shuffle(self, Inter)

    async def seek(self, Inter: Interaction | commands.context.Context, sec: int):
        await seek(self, Inter, sec)

    async def volume(self, Inter: Interaction | commands.context.Context, _volume: int):
        await volume(self, Inter, _volume)

    async def queue(self, Inter: Interaction | commands.context.Context):
        await queue(self, Inter)

    async def info_filters(self, Inter: Interaction | commands.context.Context):
        await check(self, Inter)

    async def bb(
        self,
        Inter: Interaction | commands.context.Context,
        brond: int | str,
        gain: float,
    ):
        await equalizer(self, Inter, brond, gain)

    async def timescale(
        self,
        Inter: Interaction | commands.context.Context,
        speed: float,
        pitch: float,
        rate: float,
    ):
        await timescale(self, Inter, speed, pitch, rate)

    async def karaoke(
        self,
        Inter: Interaction | commands.context.Context,
        level: float,
        monoLevel: float,
        filterBand: float,
        filterWidth: float,
    ):
        await karaoke(self, Inter, level, monoLevel, filterBand, filterWidth)

    async def kalevel(
        self, Inter: Interaction | commands.context.Context, ty: str, level: float
    ):
        await custon_karaoke(self, Inter, ty, level)

    async def rotation(
        self, Inter: Interaction | commands.context.Context, rotation_hz: float
    ):
        await rotation(self, Inter, rotation_hz)

    async def smoothing(
        self, Inter: Interaction | commands.context.Context, low: float
    ):
        await smoothing(self, Inter, low)

    async def Vibrato(
        self,
        Inter: Interaction | commands.context.Context,
        depth: float,
        frequency: float,
    ):
        await Vibrato(self, Inter, depth, frequency)

    async def Tremolo(
        self,
        Inter: Interaction | commands.context.Context,
        depth: float,
        frequency: float,
    ):
        await Tremolo(self, Inter, depth, frequency)

    async def depth(
        self, Inter: Interaction | commands.context.Context, depth: float, ty: str
    ):
        await depth_(self, Inter, depth, ty)

    async def frequency(
        self, Inter: Interaction | commands.context.Context, frequency: float, ty: str
    ):
        await frequency_(self, Inter, frequency, ty)

    async def clean(self, Inter: Interaction | commands.context.Context, op: str):
        await clear(self, Inter, op)

    async def set_auto_play(self, player):
        await set_auto_play(self, player)

    async def auto_play(self, Inter: Interaction | commands.context.Context, player):
        await auto_play(Inter, player)

    async def vote_(self, Inter: Interaction | commands.context.Context):
        return await vote(Inter, self.guild)
