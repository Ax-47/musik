import nextcord
from nextcord import Interaction
from nextcord.member import Member
from typing import  List
timeout= nextcord.embeds.Embed(title='⏱ หมดเวลาแล้วนะคะหนูขอตัวไปก่อนนะคะ' ,description ='ถ้ามีอะไรใช้คำสั่งax!hนะคะ')
class _btn(nextcord.ui.View):
        def __init__(self,memberlen,starter):
            super().__init__(timeout=60)
            self.page=1
            self.MemberInVc= memberlen
            self.MemberVoted:List[Member]=[]
            self.MemberVotedNot:List[Member]=[]
            self.vote:bool = True
            self.MemberVoted.append(starter)
            
            
        def set_message(self,message:nextcord.Message):
            self.message=message
        @nextcord.ui.button(label='vote', style=nextcord.ButtonStyle.green ,custom_id='v')
        async def bt1(self,button: nextcord.ui.Button, interaction: nextcord.Interaction ):
            self.MemberVoted.append(interaction.user)
            end = nextcord.embeds.Embed(color=0xdc4700,title=f"vote {len(self.MemberVoted)}/{self.MemberInVc}")
            end.set_author(name='Ax46 No.1')
            await interaction.response.edit_message(embed = end)
            
        @nextcord.ui.button(label='not', style=nextcord.ButtonStyle.danger ,custom_id='n')
        async def bt2(self,button: nextcord.ui.Button, interaction: nextcord.Interaction ):
            self.MemberVotedNot.append(interaction.user)
            end = nextcord.embeds.Embed(color=0xdc4700,title=f"vote {len(self.MemberVoted)}/{self.MemberVotedNot}")
            end.set_author(name='Ax46 No.1')
            await interaction.response.edit_message(embed = end)
        async def on_timeout(self):
            await self.message.edit(embed=timeout, view=None)
        async def interaction_check(self,interaction: nextcord.Interaction):
            if interaction.user in self.MemberVoted or interaction.user in self.MemberVotedNot:
                await interaction.send(f'{interaction.user.mention}vote แล้วนิ',ephemeral=True)
            else:
                if self.MemberInVc <= len(self.MemberVoted):
                    self.stop()
                    self.vote=False
                elif self.MemberInVc <= len(self.MemberVotedNot):
                    self.stop()
                return True

async def vote(Inter:Interaction)->bool:
    user=[]
    for i,k in Inter.user.voice.channel.voice_states.items():
        if k.channel and k.channel.id == Inter.user.voice.channel.id:
            member = Inter.user.voice.channel.guild.get_member(i)
            if member is not None and not member.bot:
                user.append(member)
    real_member_in_vc=len(user)//2
    embed=nextcord.Embed(color=0xff470b)
    if real_member_in_vc <=1:
        return False
    if real_member_in_vc >=20:
        real_member_in_vc=20
    embed.title=f"vote 1/{real_member_in_vc}"
    vote_view=_btn(real_member_in_vc,Inter.user)
    a=await Inter.send(embed=embed,view=vote_view)
    vote_view.set_message(a)
    await vote_view.wait()
    return vote_view.vote
    