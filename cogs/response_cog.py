import random
import string

import discord
from discord.ext import commands

class Responses(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.lower().startswith('hello'):
            await message.channel.send('Hello?')
        if message.content.lower().startswith('fuck off'):
            await message.channel.send('How about no?')
        if message.content.lower().startswith('fuck you'):
            await message.channel.send('Fuck you!')
        if message.content.lower().startswith('wucka') or message.content.lower().startswith('woka'):
            rand = random.randint(0,100)
            if rand <= 30:
                await message.channel.send('What.')
            if 30 < rand <= 60:
                await message.channel.send('I\'m trying to sleep')
            if 60 < rand < 100:
                await message.channel.send('dad told me not to talk to strangers')
            if rand == 100:
                await message.channel.send('YOU DARE SUMMON ME?')
