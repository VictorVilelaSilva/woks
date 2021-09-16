# importa a libary do discord
import discord
from discord import player
from discord import member
from discord import guild
from discord import voice_client
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import Member
from discord.flags import Intents
from discord.ext.commands import has_permissions, MissingPermissions
from time import sleep
import json
import random
import os
import time


intents = discord.Intents.default()
intents.members = True

tempo = time.localtime()
bot = commands.Bot(command_prefix='#', intents=intents)


@bot.event
async def on_ready():
    print('To area putas {0.user}'.format(bot))


@bot.command()
async def oi(ctx):
    await ctx.send("SILÊNCIO!")


@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def silence(ctx, *args):

    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        author = ctx.author
        canal = author.voice.channel.members
        voice = await channel.connect()
        source = FFmpegPCMAudio('Global_Silence.mp3.mpeg')
        player = voice.play(source)
        
        #mutar geral
        for member in canal:  # porcorre os membros no canal
          if not member.bot:  # checar se o bot não é um membro
            await member.edit(mute=True)
            sleep(6)
            await member.edit(mute=False)
            await ctx.guild.voice_client.disconnect()
          
          else:
            # desmutar o bot
            await member.edit(mute=False)
            embed.clear_fields()
            botEmbed.set_author(
            name=f"desmutaos: {member.name}")
            await ctx.send(embed=botEmbed)
    else:
        await ctx.send("Vc tem que estar em uma sala primeiro animal")
      
# cadastra o token do bot
bot.run('ODg3NzY2NjA0Njk4NTAxMTIx.YUI7FA.BrQsIipJz6jNJQoC1gDBAc1Ye0k')
