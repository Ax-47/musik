import nextcord
async def slash_shuffle(self, Inter):
       
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await Inter.send(embed=emed)
        emed.title = f'**🔀 | สุ่มเพลง :' + ('เปิดใช้งาน' if player.shuffle else 'ปิดใช้งาาน'+'**')
        player.shuffle = not player.shuffle
        await Inter.send(embed=emed)
async def prefix_shuffle(self, ctx):
       
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await ctx.send(embed=emed)
        emed.title = f'**🔀 | สุ่มเพลง :' + ('เปิดใช้งาน' if player.shuffle else 'ปิดใช้งาาน'+'**')
        player.shuffle = not player.shuffle
        await ctx.send(embed=emed)