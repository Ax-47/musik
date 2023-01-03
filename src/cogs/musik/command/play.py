from nextcord import Interaction
from nextcord.ext.commands.context import Context
import lavalink,nextcord,re
URL_RX = re.compile(r'https?://(?:www\.)?.+')
async def play(self, Inter:Interaction|Context, query: str):
        await self.join_to_channel(Inter)
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(Inter.guild.id)
        query = query.strip('<>')
        embed = nextcord.Embed(color=0xdc4700)
        if not URL_RX.match(query):
            query = f'ytsearch:{query}'
        # https://www.youtube.com/watch?v=QjQliDFIsnk&list=RDQjQliDFIsnk&index=2
        # https://www.youtube.com/playlist?list=RDQjQliDFIsnk&playnext=1
        # https://www.youtube.com/watch?v=QjQliDFIsnk&list=RDQjQliDFIsnk
        else:
            if "playlist" in query:
                a=query.replace("www.",'').replace("https://youtube.com/playlist?list=",'').replace("&playnext=1","").replace("RD",'')
                query=f"https://www.youtube.com/watch?v={a}&list=RD{a}"
        results = await player.node.get_tracks(query)
        embed.title = 'หาเพลงไม่เจอค่ะ'
        if not results or not results['tracks']:
            return await Inter.send(embed=embed)

        # 
        if results['loadType'] == 'PLAYLIST_LOADED':
            tracks = results['tracks']
            for track in tracks:
                player.add(requester=Inter.user.id, track=track)
            embed.title = f'💿เพลลิสเพลงถูกเพิ่มแล้ว'
            embed.description = f'{results["playlistInfo"]["name"]} - {len(tracks)} tracks'
            embed.add_field(name="ผู้ขอเพลง",value=str(Inter.user.mention))
        else:
            track = results['tracks'][0]
            embed.title = '💿แทร็กถูกเพิ่มแล้ว'
            embed.add_field(name="ชื่อเพลง",value= f'[{track["info"]["title"]}]({track["info"]["uri"]})',inline=False)
            embed.add_field(name="ศิลปิน",value=track["info"]["author"],inline=False)
            embed.add_field(name="เพลงมาจาก",value=f' {track["info"]["source_name"]}',inline=False)
            if track["info"]["source_name"] == 'youtube':
                embed.set_thumbnail(url="https://img.youtube.com/vi/{}/maxresdefault.jpg".format(track["info"]["identifier"]))
            embed.add_field(name="ผู้ขอเพลง",value=str(Inter.user.mention))
            player.add(requester=Inter.user.id, track=track)
        await Inter.send(embed=embed)
        if not player.is_playing:    
            await player.play()