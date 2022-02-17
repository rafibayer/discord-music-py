from discord.ext.commands import Bot
from discord.ext import commands
from cogs import play_cog

class MusicBot(Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)


if __name__ == '__main__':

    # your secret bot token
    token = open('token.txt').read()

    bot = MusicBot(command_prefix='!')

    bot.add_cog(play_cog.Play(bot))

    print("bot starting up...")
    bot.run(token)