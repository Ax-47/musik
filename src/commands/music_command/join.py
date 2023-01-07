import nextcord
from musik import player as pyer
from nextcord import Interaction
from nextcord.ext.commands.context import Context
async def join(self,ctx:Interaction|Context,typ:bool=False)->bool|int:
    
    embed=nextcord.Embed(color=0xdc4700)
    if ctx.guild is  None:
        embed.title="ใช้ในserverเท่านั้น"
        ctx.send(embed=embed)
        return False,1
    player = self.bot.lavalink.player_manager.create(ctx.guild.id)
    typeofctx=type(ctx) is Interaction
    author = ctx.user if typeofctx else ctx.author
    if not author.voice or not author.voice.channel:
        embed.title="เข้าห้องก่อนสิ"
        ctx.send(embed=embed)
        return False,2
    v_client =  ctx.guild.voice_client if ctx.guild.voice_client else None if typeofctx else ctx.voice_client 
    if not v_client:
        permissions = author.voice.channel.permissions_for((ctx.guild.me if ctx.guild is not None else self.bot.user)if typeofctx else ctx.me )
        if not permissions.connect or not permissions.speak:  # Check user limit too?
            embed.title="เข้าไม่ได้โว้ยยยยย ยศอะยศ"
            ctx.send(embed=embed)
            return False,3
        player.store('channel', ctx.channel.id)
        ca=await author.voice.channel.connect(cls=pyer)
        await ctx.channel.guild.change_voice_state(channel=ca.channel, self_deaf=True)
        if typ:
            embed.title="มาละจ้า"
            ctx.send(embed=embed)
        return True
    else:
        if v_client.channel.id != author.voice.channel.id:
            embed.title="เข้าห้องเดียวกันสิ"
            ctx.send(embed=embed)
            return False,4

