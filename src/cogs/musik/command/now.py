import nextcord, lavalink
async def slash_now(self, Inter):
        
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)

        emed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await Inter.send(embed=emed)

        position = lavalink.utils.format_time(player.position)
        if player.current.stream:
            duration = '🔴 ไลฟ์'
        else:
            duration = lavalink.utils.format_time(player.current.duration)

        embed = nextcord.Embed(color=0xff470b,
                              title='▶️ กำลังเล่นเพลง')
        embed.add_field(name='ชื่อเพลง',value=f'[{player.current.title}]({player.current.uri})',inline=False)
        embed.add_field(name='ศิลปิน',value=f'{player.current.author}',inline=False)
        embed.add_field(name='ระยะเวลา',value=f'{position} / {duration}',inline=False)
        embed.add_field(name='ผู้ขอเพลง',value=f'<@{player.current.requester}>',inline=False)
        embed.set_thumbnail(url="https://img.youtube.com/vi/{}/default.jpg".format(player.current.identifier))
        await Inter.send(embed=embed)
async def prefix_now(self, ctx):
        
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        emed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await ctx.send(embed=emed)

        position = lavalink.utils.format_time(player.position)
        if player.current.stream:
            duration = '🔴 ไลฟ์'
        else:
            duration = lavalink.utils.format_time(player.current.duration)

        embed = nextcord.Embed(color=0xff470b,
                              title='▶️ กำลังเล่นเพลง')
        embed.add_field(name='ชื่อเพลง',value=f'[{player.current.title}]({player.current.uri})',inline=False)
        embed.add_field(name='ศิลปิน',value=f'{player.current.author}',inline=False)
        embed.add_field(name='ระยะเวลา',value=f'{position} / {duration}',inline=False)
        embed.add_field(name='ผู้ขอเพลง',value=f'<@{player.current.requester}>',inline=False)
        embed.set_thumbnail(url="https://img.youtube.com/vi/{}/default.jpg".format(player.current.identifier))
        await ctx.send(embed=embed)