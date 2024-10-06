import nextcord
from commands.setupa import *
from database import CAPTCHA, GUILD
from nextcord import Interaction, message_command, slash_command
from nextcord.ext import application_checks
from nextcord.ext.commands import AutoShardedBot, Cog

from events.join_leave import JOIN_LEAVE


class setup_commands(Cog):
    def __init__(self, bot: AutoShardedBot) -> None:
        self.bot = bot

    @slash_command(force_global=True)
    @application_checks.has_permissions(administrator=True)
    async def setup(self, inter: nextcord.Interaction): ...
    @setup.subcommand()
    async def create(self, inter: nextcord.Interaction): ...
    @setup.subcommand()
    async def test(self, inter: nextcord.Interaction): ...
    @setup.subcommand()
    async def custom(self, inter: nextcord.Interaction): ...
    @create.subcommand(name="role-dj", description="Asdasd")
    async def create_Dj(
        self,
        inter: Interaction,
        role: nextcord.Role = nextcord.SlashOption(name="role", default=None),
    ) -> None:
        await create_DJ(inter, role, GUILD)

    @setup.subcommand(name="join", description="Asdasd")
    async def set_join(
        self,
        inter: Interaction,
        channel: nextcord.TextChannel = nextcord.SlashOption(
            name="channel", default=None
        ),
    ) -> None:
        await set_room("join", inter, channel, GUILD)

    @custom.subcommand(name="join", description="Asdasd")
    async def customjoin(
        self,
        inter: Interaction,
        contain: str = nextcord.SlashOption(
            name="contain",
            choices=[
                "title",
                "descript",
                "color",
                "image",
                "thumbnail",
                "auth_icon",
                "auth_text",
                "footer_icon",
                "footer_text",
            ],
        ),
        volume: str = nextcord.SlashOption(name="volume"),
    ) -> None:
        await custom(inter, "join", contain, volume, GUILD)

    @custom.subcommand(name="leave", description="Asdasd")
    async def customleave(
        self,
        inter: Interaction,
        contain: str = nextcord.SlashOption(
            name="contain",
            choices=[
                "title",
                "descript",
                "color",
                "image",
                "thumbnail",
                "auth_icon",
                "auth_text",
                "footer_icon",
                "footer_text",
            ],
        ),
        volume: str = nextcord.SlashOption(name="volume"),
    ) -> None:
        await custom(inter, "leave", contain, volume, GUILD)

    @setup.subcommand(name="leave", description="Asdasd")
    async def set_leave(
        self,
        inter: Interaction,
        channel: nextcord.TextChannel = nextcord.SlashOption(
            name="channel", default=None
        ),
    ) -> None:
        await set_room("leave", inter, channel, GUILD)

    @setup.subcommand(name="captcha", description="Asdasd")
    async def set_captcha(
        self,
        inter: Interaction,
        channel: nextcord.TextChannel = nextcord.SlashOption(
            name="channel", default=None
        ),
    ) -> None:
        await set_captcha("captcha", inter, channel, CAPTCHA, GUILD)

    @custom.subcommand(name="upload-image-join", description="Asdasd")
    async def upload_image(
        self,
        inter: Interaction,
        contain: str = nextcord.SlashOption(
            name="contain",
            choices=[
                "image",
                "thumbnail",
                "auth_icon",
                "footer_icon",
            ],
        ),
        volume: nextcord.Attachment = nextcord.SlashOption(name="image"),
    ) -> None:
        await download(inter, "join", contain, volume, GUILD)

    @custom.subcommand(name="upload-image-leave", description="Asdasd")
    async def upload_image(
        self,
        inter: Interaction,
        contain: str = nextcord.SlashOption(
            name="contain",
            choices=[
                "image",
                "thumbnail",
                "auth_icon",
                "footer_icon",
            ],
        ),
        volume: nextcord.Attachment = nextcord.SlashOption(name="image"),
    ) -> None:
        await download(inter, "leave", contain, volume, GUILD)

    @setup.subcommand(name="report", description="Asdasd")
    async def set_report(
        self,
        inter: Interaction,
        channel: nextcord.TextChannel = nextcord.SlashOption(
            name="channel", default=None
        ),
    ) -> None:
        await set_room("report", inter, channel, GUILD)

    @test.subcommand(name="sudo-join", description="Asdasd")
    async def sudo_join(self, inter: Interaction) -> None:
        await JOIN_LEAVE("join", GUILD, inter.user)
        await inter.send(embed=nextcord.Embed(color=0xDC4700, title="request ไปแล้วจ้า"))

    @test.subcommand(name="sudo-leave", description="Asdasd")
    async def sudo_leave(self, inter: Interaction) -> None:
        await JOIN_LEAVE("leave", GUILD, inter.user)
        await inter.send(embed=nextcord.Embed(color=0xDC4700, title="request ไปแล้วจ้า"))

    @message_command(name="report", force_global=True)
    async def report(self, inter: Interaction, message: nextcord.Message) -> None:
        await report(self, inter, message, GUILD)

    @setup.subcommand(
        name="tonton",
        description="Be the first!!!! to receive vedio about tonton",
        description_localizations={"th": "ได้ชมคลิปที่คุณภาพก่อนใครจาก tonton210"},
    )
    async def set_2tonton420(
        self,
        inter: Interaction,
        channel: nextcord.TextChannel = nextcord.SlashOption(
            name="channel", default=None
        ),
    ) -> None:
        await set_room("2tonton420", inter, channel, GUILD)


def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(setup_commands(bot))
