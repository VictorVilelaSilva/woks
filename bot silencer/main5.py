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


intents = discord.Intents.default()
intents.members = True

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
            member.edit(mute=True)

            member.edit(mute=False)
            
          
          else:
            # desmutar o bot
            member.edit(mute=False)
            embed.clear_fields()
            botEmbed.set_author(
            name=f"desmutaos: {member.name}")
          
    else:
        await ctx.send("Vc tem que estar em uma sala primeiro animal")
      
# cadastra o token do bot
with open("token.txt","r",encoding = "utf-8") as f:
  bottoken = f.read()

bot.run(bottoken)

