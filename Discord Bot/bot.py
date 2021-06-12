import discord
from discord.ext import commands

mainClient = commands.Bot(command_prefix = '$')

@mainClient.event
async def on_ready():
    print('Ready to recognize!')


@mainClient.event
async def on_member_join(member):
    print(f'{member} coming to the party!')

@mainClient.command()
async def test(ctx):
    embedTest = discord.Embed(
        title = 'Test Title',
        description = 'Test'
        
    )
    embedTest.set_footer(text = 'Footer Test')
    embedTest.set_author(name = 'Author Name')

    await ctx.send(embed = embedTest)

    












mainClient.run('ODUzMDQxNTgxMzUwNDUzMzA5.YMPm4Q.RXwvh_EfJA1QoBbTjnmx4AiLUOE')