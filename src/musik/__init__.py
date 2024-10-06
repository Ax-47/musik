import os

import nextcord
from dotenv import load_dotenv
from nextcord.ext.commands import Bot

import lavalink

load_dotenv()
# Retrieve environment variables
host = os.getenv("NODE_HOST")
port = os.getenv("NODE_PORT")
password = os.getenv("NODE_PASSWORD")
region = os.getenv("NODE_REGION")  # Fixed typo: "NODE_REGSION" to "NODE_REGION"
name = os.getenv("NODE_NAME")
app_id = os.getenv("APP_ID")

# Check if any of the environment variables are None
if None in (host, port, password, region, name, app_id):
    print("One or more environment variables are not set.")
    if host is None:
        print("NODE_HOST is not set.")
    if port is None:
        print("NODE_PORT is not set.")
    if password is None:
        print("NODE_PASSWORD is not set.")
    if region is None:
        print("NODE_REGION is not set.")
    if name is None:
        print("NODE_NAME is not set.")
    if app_id is None:
        print("APP_ID is not set.")

    sys.exit(1)


class player(nextcord.VoiceClient):
    def __init__(self, client: Bot, channel: nextcord.abc.Connectable) -> None:
        self.client = client
        self.channel = channel
        self.guild_id = channel.guild.id
        self._destroyed = False
        if not hasattr(self.client, "lavalink"):
            # Instantiate a client if one doesn't exist.
            # We store it in `self.client` so that it may persist across cog reloads,
            # however this is not mandatory.
            self.client.lavalink = lavalink.Client(app_id)
            self.client.lavalink.add_node(
                host,
                port,
                password,
                region,
                name,
            )

        # Create a shortcut to the Lavalink client here.
        self.lavalink = self.client.lavalink

    async def on_voice_server_update(self, data):
        # the data needs to be transformed before being handed down to
        # voice_update_handler
        lavalink_data = {"t": "VOICE_SERVER_UPDATE", "d": data}
        await self.lavalink.voice_update_handler(lavalink_data)

    async def on_voice_state_update(self, data):
        # the data needs to be transformed before being handed down to
        # voice_update_handler
        lavalink_data = {"t": "VOICE_STATE_UPDATE", "d": data}
        await self.lavalink.voice_update_handler(lavalink_data)

    async def connect(
        self,
        *,
        timeout: float,
        reconnect: bool,
        self_deaf: bool = False,
        self_mute: bool = False
    ) -> None:
        """
        Connect the bot to the voice channel and create a player_manager
        if it doesn't exist yet.
        """
        # ensure there is a player_manager when creating a new voice_client
        self.lavalink.player_manager.create(guild_id=self.channel.guild.id)
        await self.channel.guild.change_voice_state(
            channel=self.channel, self_mute=self_mute, self_deaf=self_deaf
        )

    async def disconnect(self, *, force: bool = False) -> None:
        """
        Handles the disconnect.
        Cleans up running player and leaves the voice client.
        """
        player = self.lavalink.player_manager.get(self.channel.guild.id)

        # no need to disconnect if we are not connected
        if not force and not player.is_connected:
            return

        # None means disconnect
        await self.channel.guild.change_voice_state(channel=None)

        # update the channel_id of the player to None
        # this must be done because the on_voice_state_update that would set channel_id
        # to None doesn't get dispatched after the disconnect
        player.channel_id = None
        self.cleanup()
