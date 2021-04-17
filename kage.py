import discord
import asyncio

import random
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv('.env')

client = commands.Bot(command_prefix = "c.",
                      case_insensitive = True,
                      activity = discord.Game(name = 'Volleyball'),
                      status = discord.Status.online
                      )
client.remove_command('help')

@client.event
async def on_ready():
    print('Coach Kage is warming up.')

@client.command()
async def die(ctx):
    if ctx.author.id in [436973854485643264]:
        await ctx.send(f"Bye Daddy {ctx.author.display_name}!")
        await client.logout()

@client.command()
async def help(ctx):
    embed = discord.Embed(
        description = '``Code blocks`` = How the commands should be used, <> = Required arguments, you don\'t include either in your commands. | Commands can be in full lower or upper cap, as well as only the first letter capitilized.',
        colour = discord.Colour(0Xb8f2f2)
    )

    embed.set_author(
    name='Help'
    )

    embed.set_footer(
    text='Success rates might change in the future. Also the follow-ups to each move depends on the result of the previous move, for now the bot does not decide this though.'
    )

    embed.add_field(
    name='**General Commands**',
    value='*The following are General Commands*', inline=False
    )

    embed.add_field(
    name='ping',
    value='``ping`` | Shows latency of bot in ms', inline=False
    )

    embed.add_field(
    name='8ball',
    value='``8ball <question>`` | Answers yes and no questions in 8ball fashion', inline=False
    )

    embed.add_field(
    name='whoistoru',
    value='``whoistoru`` | Answers who is Toru...', inline=False
    )

    embed.add_field(
    name='americaisbest',
    value='``americaisbest`` | With Kaze it shows a link starting the video at a **certain** time, but with Kage it shows something else...**Kage is a nerd**', inline=False
    )

    embed.add_field(
    name='marryme',
    value='``marryme`` | **See for yourself**', inline=False
    )

    embed.add_field(
    name='loli',
    value='``loli`` | All I can say is that Kaze and Kage have different opinions about this', inline=False
    )

    embed.add_field(
    name='cookie',
    value='``cookie`` | GIMMIE COOKIE', inline=False
    )

    embed.add_field(
    name='milk',
    value='``milk`` | *sip sip*', inline=False
    )

    embed.add_field(
    name='jam', value='``jam`` | *headbang*', inline=False
    )

    embed.add_field(
    name='back',
    value='``back`` | Kage is back', inline=False
    )

    embed.add_field(
    name=("\u200b"),
    value=("\u200b"), inline=False
    )

    embed.add_field(
    name='**Volleyballl Commands**',
    value='*The following are Volleyball Commands*', inline=False
    )

    embed.add_field(
    name='serve',
    value='``serve`` | You serve the volleyball, has a 5/7 success chance', inline=False
    )

    embed.add_field(
    name='receive',
    value='``receive`` | You receive the volleyball, has a 5/7 success chance', inline=False
    )

    embed.add_field(
    name='set',
    value='``set`` | You set the ball for the spiker, has a 7/10 success chance', inline=False
    )

    embed.add_field(
    name='spike',
    value='``spike`` | You spike the volleyball, has a 6/8 success chance', inline=False
    )

    embed.add_field(
    name='block',
    value='``block`` | You block the spike, has a 4/5 success chance', inline=False
    )

    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! I won the ping pong game. You lost on {round(client.latency * 1000)}ms')

@client.command()
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'Hell yeah!',
                'Without a doubt.',
                'Yes – definitely.',
                'Of course you dumb dumb.',
                'As I see it, yes.',
                'Most likely.',
                'Yeah pretty much.',
                'Daddy Mizu says yes!',
                'The council says yes.',
                'Uhhhhhhhhh.',
                'I will tell you later.',
                'Better not tell you now.',
                'It is a secret.',
                'Wait till your birthday for an answer.',
                'Eh...no.',
                'Nu!.',
                'Daddy Mizu says nu!',
                'Of course not.',
                'Very doubtful.']
    await ctx.send(f":8ball: **{ctx.author.name}'s Question:** *{question}*\n:8ball: **My wisdom:** *{random.choice(responses)}*.")

@client.command()
async def whoisToru(ctx):
    await ctx.send('Toru is the person that should do her homework and practice more.')

@client.command()
async def americaisbest(ctx):
    await ctx.send('I do not see them winning volleyball championships.')

@client.command()
async def marryme(ctx):
    await ctx.send('How about you go do 5 reps of 90 pushups.')

@client.command()
async def loli(ctx):
    await ctx.send('Lolis have no atheletic potiential.')

@client.command()
async def cookie(ctx):
    await ctx.send('Cookies are healthy, eat up :cookie:')

@client.command()
async def milk(ctx):
    await ctx.send('*sip* You caught me having some milk, have some yourself before the next match :milk:')

@client.command()
async def dice(ctx):
    responses = ['1',
                '2',
                '3',
                '4',
                '5',
                '6']
    await ctx.send(f':handshake: *rolling the dice* \n\n:game_die: You rolled a {random.choice(responses)}')

@client.command()
async def jam(ctx):
    await ctx.send('*jams while serving for the 500th time*')

@client.command()
async def back(ctx):
    await ctx.send('*Coach Kage has warmed up and prepared all training plans*')



# Volleyball commands

'''
There are no accidents... EXCEPT YOU
Ouch you just had to be honest
Today's Result : Honesty Wins.
Streak :
    Honesty : 0+4
    Mizu : 0-4
'''

class Player:
    def __init__(self, member: discord.Member):
        self.user = member.display_name

@client.command()
async def volley(ctx, member: discord.Member):
    # client.load_extension(f'cogs.{extension}')
    startGame = discord.Embed(
        title = f'**Team {ctx.author.display_name}** vs **Team {member.display_name}**',
        colour = discord.Colour(0Xb8f2f2),
        description = 'If you wish to continue and start the volleyball match please react to this message in 20 seconds'
    )

    startGame.set_author(
        name = f'{ctx.author}',
        icon_url = ctx.author.avatar_url
    )

    startGame.add_field(
        name = '__Reminders__',
        value = '''
        ● 10 seconds before you lose the rally [not yet lol]
        ● 3 Touches maximum per side in one rally [not yet lol]
        ● Typical order (can be special cases) :
        [Team 1] Serve -> [Team 2] Recieve -> [Team 2] Set -> [Team 2] Spike -> [Team 1] Recieve...(and on until one loses the rally)\n
        '''
    )

    startGame = await ctx.send(embed = startGame)
    await startGame.add_reaction('🏐')

    def checkg(reaction, user):
        a = user == ctx.author
        b = str(reaction.emoji) == '🏐'
        c = user == member
        if a and b:
            a = True
        elif c and b:
            c = True
        return a and b and c

    # You are like literally every new programmer... BOKE! MIZU BOKE! Yay

    try:
       reaction, user = await client.wait_for(event = 'reaction_add', timeout = 10.0, check = checkg)
    except asyncio.TimeoutError:
        await ctx.send('You are late to the court, the game\'s cancelled.')
    else:
        await ctx.send('Good luck to both sides and may the home team commence with the serve.')


    # def checkw(m, author):
    #     return m.author == author
    #
    # try:
    #    m = await client.wait_for(event = 'message', timeout = 10.0, check = lambda x: checkw(x, ctx.author))
    #    msg = await client.wait_for(event = 'message', timeout = 10.0, check = checkw)
    # except asyncio.TimeoutError:
    #     await ctx.send('You\'re too slow!')
    # else:
    #     await ctx.send('Good luck to both sides and may the home team commence with the serve.')



@client.event
async def on_message(message):

    loss = ['*hits it too hard, getting it out successfully*',
            '*hits it right into the net*',
            '*sets the ball off course getting it out*',
            '*sets too long*',
            '*sets too short*',
            '*times spike incorrectly, completely missing the ball*',
            '*spikes ball too hard getting it out*',
            '*blocks the ball but hits it out*']

    if any(thing in message.content for thing in loss):
            await message.channel.send(f'***whistle*** point goes to the opposing team of last touch')
            return

    await client.process_commands(message)



@client.event
async def on_message(message):

    win = ['*hits a service ace!* **NICE SERVE**',
            '*jumps up reading the hit and shutting it down*']

    if any(thing in message.content for thing in win):
            await message.channel.send(f'***whistle*** point goes to the team of last touch')
            return

    await client.process_commands(message)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))
