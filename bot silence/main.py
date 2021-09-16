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

# send a help msg when the bot joins a server
@bot.event
async def on_guild_join(guild):
    embed = discord.Embed()
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed.add_field(name="Obrigado por me adicionar no seu servidor!",
                            value="Se vc ja esta em um sala, apenas manda #silence para silenciar todos que estão em um sala por 6 segundos.")
            await channel.send(embed=embed)
            break

@bot.command()
async def oi(ctx):
    await ctx.send("SILÊNCIO!")


@bot.command(pass_context=True)
async def silence(ctx):

  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    author = ctx.author
    canal = author.voice.channel.members
    voice = await channel.connect()
    source = FFmpegPCMAudio('Global_Silence.mp3.mpeg')
    player = voice.play(source)
        
      #mutar geral
      
    for member in canal:  # porcorre os membros no canal
        if not member.bot:  # So mutar pessoas
          await member.edit(mute=True)
        
    sleep(6)  
        
    for member in canal:
      if not member.bot:
        await member.edit(mute=False)

        
    await ctx.guild.voice_client.disconnect()
          
  else:
    await ctx.send("Vc tem que estar em uma sala primeiro animal")
      
# cadastra o token do bot
with open("token.txt","r",encoding = "utf-8") as f:
  bottoken = f.read()

bot.run(bottoken)

