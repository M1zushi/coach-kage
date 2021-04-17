import discord
from discord.ext import commands
import asyncio
import random
import os


class Volleyball(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def serve(self, ctx):
        responses = ['*hits it too hard, getting it out successfully*',
                    '*hits it right into the net*',
                    '*hits it with incredible power and speed*',
                    '*hits it over the net towards the line*',
                    '*hits it right at the libero, but it is still a tough hit*',
                    '*hits a service ace!* **NICE SERVE**',
                    '*hits an amazing serve over the net*']
        await ctx.send(f'*{ctx.message.author.mention}* {random.choice(responses)}')


    @commands.command()
    async def receive(self, ctx):
        responses = ['*receives successfully, an A pass*',
                    '*receives with a bit of struggle, a B pass*',
                    '*dives for the ball, a C pass* **NICE RECEIVE**',
                    '*gets an overhand receive, but the momentum is weak* **COVER!**',
                    '*receives a strong hit, sending the ball flying straight up high* **GOMENNASAI**',
                    '*receives ball, but it flies off course*',
                    '*dives for the ball, barely missing it*']
        await ctx.send(f'*{ctx.message.author.mention}* {random.choice(responses)}')


    @commands.command()
    async def set(self, ctx):
        responses = ['*sets the ball perfectly*',
                    '*sets the ball high in the air*',
                    '*sets the ball with speed towards the spiker*',
                    '*sets the ball in a lob*',
                    '*sets the ball across the court to the other side*',
                    '*passes the ball with an underhand due to it being low* **GOMENNASAI**',
                    '*jumps for a set but hits the ball over for a dump*',
                    '*sets the ball off course getting it out*',
                    '*sets too long*',
                    '*sets too short*']
        await ctx.send(f'*{ctx.message.author.mention}* {random.choice(responses)}')


    @commands.command()
    async def spike(self, ctx):
        responses = ['*spikes, hitting a strong line shot*',
                    '*spikes, hitting a cross shot at the unprepared reciever*',
                    '*spikes from the back*',
                    '*swings his hand aggresively, only to go for a feint throwing off the enemy team*',
                    '*flicks his wrist, spiking the ball straight down*',
                    '*spikes intensly and quickly, hitting it with aggresion*',
                    '*times spike incorrectly, completely missing the ball*',
                    '*spikes ball too hard getting it out*']
        await ctx.send(f'*{ctx.message.author.mention}* {random.choice(responses)}')


    @commands.command()
    async def block(self, ctx):
        responses = ['*jumps up reading the hit and shutting it down*',
                    '*blocks the spike but sends the ball high back to the enemy team*',
                    '*gets a one touch slowing down the spike*',
                    '*puts up a solid wall, narrowing down the path of the spike*',
                    '*blocks the ball but hits it out*']
        await ctx.send(f'*{ctx.message.author.mention}* {random.choice(responses)}')


def setup(client):
    client.add_cog(Volleyball(client))
