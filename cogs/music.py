import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class MusicPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = asyncio.Queue()
        self.voice_client = None
        self.current_song = None

    async def connect(self, ctx):
        if not ctx.author.voice:
            await ctx.send("Você não está em um canal de voz.")
            return
        if self.voice_client:
            await self.voice_client.move_to(ctx.author.voice.channel)
        else:
            self.voice_client = await ctx.author.voice.channel.connect()

    async def play_next(self, ctx):
        if self.queue.empty():
            return
        song_url = await self.queue.get()
        self.current_song = song_url
        async with ctx.typing():
            info = ytdl.extract_info(song_url, download=False)
            url = info['formats'][0]['url']
            self.voice_client.stop()
            self.voice_client.play(discord.FFmpegPCMAudio(url, **ffmpeg_options))
            await ctx.send(f"Tocando {info['title']}")

    @commands.command(name='play')
    async def play(self, ctx, url):
        await self.connect(ctx)
        await self.queue.put(url)
        if not self.voice_client.is_playing():
            await self.play_next(ctx)

    @commands.command(name='pause')
    async def pause(self, ctx):
        if self.voice_client.is_playing():
            self.voice_client.pause()
            await ctx.send("Música pausada.")

    @commands.command(name='resume')
    async def resume(self, ctx):
        if self.voice_client.is_paused():
            self.voice_client.resume()
            await ctx.send("Música retomada.")

    @commands.command(name='stop')
    async def stop(self, ctx):
        if self.voice_client.is_playing():
            self.voice_client.stop()
            await ctx.send("Música parada.")
        await self.queue.queue.clear()
        self.current_song = None

async def setup(bot):
    await bot.add_cog(MusicPlayer(bot))
