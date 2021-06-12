import discord
from discord import embeds
from discord import client
from discord import guild
from discord.ext import commands
import json 

def addStuff(name, time):
    with open('info.json') as infoFile:
        coming = json.load(infoFile)
    print("hey")
    coming[name] = time
    print(coming)
    with open("info.json", "w+") as outfile: 
        json.dump(coming, outfile)

def removeStuff(name):
    print("hey")
    with open('info.json') as infoFile:
        coming = json.load(infoFile)
    coming.pop(name)
    with open("info.json", "w+") as outfile: 
        json.dump(coming, outfile)

intents = discord.Intents.default()
intents.members = True


mainClient = commands.Bot(command_prefix = '$', intents = intents)

@mainClient.event
async def on_ready():
    print('Ready to recognize!')

@mainClient.event
async def on_member_join(member):
    serverGuild = mainClient.get_guild(842752761594773575)
    channel = serverGuild.get_channel(853041836088360990)
    embed1 = discord.Embed(
        title='RSVP',
        description='Use the "$rsvp" to confirm your spot at the party!\n\n$rsvp [first name] [phone #] [time your coming (X:XX)]\n\nUse command $cancel [yourname] to cancel ur RSVP\n\nIf you forgot what to do use command $howto',
        colour=discord.Colour.blue()
    )
    embed1.set_author(name='Banana Party!')
    
    await member.send(f'Welcome to the {serverGuild.name}, {member.name}!')
    await channel.send(embed = embed1)
    await member.send(embed = embed1)


@mainClient.command()
async def rsvp(ctx,name, pn, time):
    serverGuild = mainClient.get_guild(842752761594773575)
    confirmChannel = serverGuild.get_channel(853315141742493696)
    await ctx.send(f'Congrats {name}, you have successfuly signed up for the party!\nYou will be arriving at {time}pm')
    
    confirmEmbed = discord.Embed(
        title = str(name.title()) + ' Confirmed!',
        description = 'Time reaching: ' + str(time) + '\n\nPhone number: ' + str(pn),
        colour = discord.Colour.green()
    )
    addStuff(str(name), str(time))
    await confirmChannel.send(embed = confirmEmbed)

@mainClient.command()
async def cancel(ctx, name):
    serverGuild = mainClient.get_guild(842752761594773575)
    cancelChannel = serverGuild.get_channel(853320317156982835)
    await ctx.send(f'You have cancelled your RSVP {name}')

    cancelEmbed = discord.Embed(
        title = str(name.title()) + ' cancelled',
        description = 'They will no longer attend the party',
        colour = discord.Colour.dark_red()
    )
    removeStuff(str(name))
    await cancelChannel.send(embed = cancelEmbed)

@mainClient.command()
async def howto(ctx):
    embed1 = discord.Embed(
        title='RSVP',
        description='Use command $rsvp to confirm your spot at the party!\n\n$rsvp [first name] [phone #] [time your coming (X:XX)]\n\nTo cancel use $cancel',
        colour=discord.Colour.blue()
    )
    embed1.set_author(name='Banana Party!')
    await ctx.send(embed = embed1)

@mainClient.command()
async def predict(ctx, filename):
    print(check.startSearch())
    check.vidOut(filename)





mainClient.run('ODUzMDQxNTgxMzUwNDUzMzA5.YMPm4Q.RXwvh_EfJA1QoBbTjnmx4AiLUOE')
