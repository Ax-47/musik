import nextcord,asyncio
async def volume(self, ctx, volume: int = None):
        """ Changes the player's volume (0-1000). """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if player is None:
            emed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=emed)
            return
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await ctx.send(embed=emed)
        if volume == None:
            emed.title = f'> 🔈 | ความดังอยู่ในระดับ {player.volume}% คะ'
            return await ctx.send(embed=emed)
        asyncio.create_task(player.set_volume(volume))
        emed.title =f'> 🔈 | คุณได้ปรับระดับควมดังอยู่ที่ {player.volume}% ค๋ะ'
        await ctx.send(embed=emed)