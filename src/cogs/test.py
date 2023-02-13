from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from database import FEEDBACK
import nextcord
timeout= nextcord.embeds.Embed(title='⏱ หมดเวลาแล้วนะคะหนูขอตัวไปก่อนนะคะ' ,description ='ถ้ามีอะไรใช้คำสั่งax!hนะคะ')
class _btn(nextcord.ui.View):
    def __init__(self,interaction):
        super().__init__(timeout=300)
        self.ch=ChooseView(interaction)
        self.add_item(self.ch)
    def set_message(self,message):
        self.message=message
    async def on_timeout(self):
        await self.message.edit(embed=timeout, view=None)
class ChooseView(nextcord.ui.Select):
    def __init__(self, interaction: nextcord.Interaction):
        options=[
                    nextcord.SelectOption(label='Index',
                                              description='หน้าแรก',
                                              ),
                    nextcord.SelectOption(label='music basic',
                                              description='คำสั่งพื้นฐานเกี่ยวกับเพลง'
                                              ),
                    nextcord.SelectOption(label='music filter',
                                              description='คำสั่งfilter',
                                              ),
                    nextcord.SelectOption(label='setup',
                                              description='คำสั่งsetupเฉพาะadmin'
                                              ),
                    nextcord.SelectOption(label='massage commands',
                                              description='คำสั่งข้อความ'
                                              )]
        super().__init__(placeholder='Choose',min_values=1,max_values=1, options=options)
    async def callback(self, interaction: nextcord.Interaction):
        help_embed=nextcord.Embed(color=0xdc4700)
        match self.values[0]:
            case 'Index':
                help_embed.title="Index"
                help_embed.description="hey, menya zovut Misha\nดีจ้าเรียกฉันว่ามิช่า"
            case 'music basic':
                help_embed.title="music basic"
                help_embed.description="คำสั่งพื้นฐานเกี่ยวกับเพลง"
                help_embed.add_field(name="`/play` {{link-query}}",value="เล่นเพลงจากurl หรือ ชื่อเพลง",inline=False)
                help_embed.add_field(name="`/skip` ",value="ข้ามเพลง",inline=False)
                help_embed.add_field(name="`/stop` ",value="หยุดเพลง",inline=False)
                help_embed.add_field(name="`/pause`",value="พักเพลง",inline=False)
                help_embed.add_field(name="`/now` ",value="ดูข้อมูลเพลง",inline=False)
                help_embed.add_field(name="`/queue` ",value="ดูqueue",inline=False)
                help_embed.add_field(name="`/remove` {{queue}}",value="ลบเพลงออกจากqueue",inline=False)
                help_embed.add_field(name="`/repeat` {{type loop}}",value="loopเพลง โดย\n\t1none คือ ยกเลิกloop\n\t2single คือ loopเพลงเดียว\n\t3queue คือ ทั้งqueue",inline=False)
                help_embed.add_field(name="`/shuffle` {{on-off}}",value="สุ่มเพลง",inline=False)
                help_embed.add_field(name="`/seek` {{sec}}",value="กอเพลง",inline=False)
                help_embed.add_field(name="`/info_filters` ",value="ดูข้อมูลfilter",inline=False)
                help_embed.add_field(name="`/auto_play` {{on-off}}",value="สุ่มเพลงจากyoutubeเมื่อไม่มีเพลงเล่นต่อ",inline=False)
                help_embed.add_field(name="`/volume` {{1-1000}}",value="ปรับระดับเสียง",inline=False)
                help_embed.add_field(name="`/join` ",value="เชิญน้องมิช่าเข้าห้องเพลง",inline=False)
                help_embed.add_field(name="`/disconnect`",value="ไล่น้องมิช่าออกจากห้อง",inline=False)
            case 'music filter':
                help_embed.title="music filter"
                help_embed.description="คำสั่งfilter คำสั่งชุดนี้จะใช้ยากไปหน่อยน้าคะ"
                help_embed.add_field(name="`/filters bassboost` {{bands [0-14]}} {{gain [-0.25 - 1]}}",value="bassbost ปรับระดับeq",inline=False)
                help_embed.add_field(name="`/filters timescale` {{speed >1}} {{pitch >1}} {{rate >1}}",value="ความเร็วเพลง, ระดับเสียง, rate ",inline=False)
                help_embed.add_field(name="`/filters karaoke` {{level}} {{monolevel}} {{filterband}} {{filterwidth}}",value="ปรับfilter karaoke",inline=False)
                help_embed.add_field(name="`/filters tremolo` {{speed}} {{pitch}}",value="tremolo",inline=False)
                help_embed.add_field(name="`/filters vibrato` {{speed}} {{pitch}}",value="vibrato",inline=False)
                help_embed.add_field(name="`/filters smoothing` {{low}}",value="smoothing",inline=False)
                help_embed.add_field(name="`/filters rotation` {{rotation}}",value="rotation",inline=False)
                help_embed.add_field(name="`/filters clean` {{filter}}",value="ล้างfilter",inline=False)
            case 'setup':
                help_embed.title="setup"
                help_embed.description="คำสั่งsetupเฉพาะadminเท่านั้น"
                help_embed.add_field(name="`/setup create role-dj` {{role}}",value="สร้างยศDJ",inline=False)
                help_embed.add_field(name="`/setup join` {{channel}}",value="ทำห้องwelcome",inline=False)
                help_embed.add_field(name="`/setup leave` {{channel}}",value="ทำห้องleave",inline=False)
                help_embed.add_field(name="`/setup report` {{channel}}",value="ทำห้องรายงาน",inline=False)
                help_embed.add_field(name="`/setup tonton` {{channel}}",value="ทำห้องแจ้งเตือนข้อมูลสำคัญ",inline=False)
                help_embed.add_field(name="`/setup custom join` {{type}} {{text}}",value="customห้องwelcome",inline=False)
                help_embed.add_field(name="`/setup custom leave` {{type}} {{text}}",value="customห้องleave",inline=False)
                help_embed.add_field(name="`/setup custom upload-image-join` {{type}} {{image}}",value="custom ภาพห้องwelcome",inline=False)
                help_embed.add_field(name="`/setup custom upload-image-leave` {{type}} {{image}}",value="custom ภาพห้องleave",inline=False)
                help_embed.add_field(name="`/setup test sudo-join` ",value="ทดสอบคนเข้า",inline=False)
                help_embed.add_field(name="`/setup test sudo-leave` ",value="ทดสอบคนออก",inline=False)
            case 'massage commands':
                help_embed.title="massage commands"
                help_embed.description="คำสั่งข้อความ"
                help_embed.add_field(name="`play` ",value="เล่นเพลงจากyoutubeด้วยข้อความ",inline=False)
                help_embed.add_field(name="`report` ",value="รายงานข้อความไม่เหมาะสม",inline=False)
        await interaction.response.edit_message(embed = help_embed)
class Ping(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.help_embed=nextcord.Embed(color=0xdc4700)
    @slash_command(name="ping", description="A simple ping command.",force_global=True)
    async def ping(self, inter: Interaction) -> None:
        await inter.send(f"Pong! {self.bot.latency * 1000:.2f}ms")
    @slash_command(name="help", description="ยังไม่ได้ทำ",force_global=True)
    async def help(self, inter: Interaction) -> None:
        
        
        # หน้าแรก
        self.help_embed.title="Index"
        self.help_embed.description="hey, menya zovut Misha\nดีจ้าเรียกฉันว่ามิช่า"
        # basic
        # filter
        # setup
        # massage commands
        
        btn=_btn(inter)
        a=await inter.send(embed=self.help_embed,view=btn)
        btn.set_message(a)
    @slash_command(name="feedback", description="feedback",force_global=True)
    async def feedback(self, inter: Interaction,feedback:str=nextcord.SlashOption(name="feedback")) -> None:
        await FEEDBACK.insert_one({"name":inter.user.name,"feedback":feedback})
        await inter.send(f"help")
def setup(bot: Bot) -> None:
    bot.add_cog(Ping(bot))