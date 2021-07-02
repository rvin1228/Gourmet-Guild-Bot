import discord
from discord.ext import commands
import os

class customCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Custom Commands
    @commands.command()
    async def clear(self, ctx, amount=5):
    	await ctx.channel.purge(limit=amount)
        
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Guide',
            description = "Welcome to Gourmet Guild's Help.\nFind the usage of available commands below:",
            colour = discord.Colour.orange()

        )

        embed.set_footer(text='Gourmet Guild')
        embed.set_image(url='https://media.discordapp.net/attachments/849145577987899426/860517464689213460/albiononline.png?width=959&height=480')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/849145577987899426/860517059434774588/discord_bot___system_s_logo_by_starkaahn_dc9ne7m-fullview.png')
        embed.set_author(name='Gourmet Guild | Help Commands', icon_url='https://media.discordapp.net/attachments/849145577987899426/860517059434774588/discord_bot___system_s_logo_by_starkaahn_dc9ne7m-fullview.png')
        embed.add_field(name='Command Prefix', value='-gg', inline=False)
        embed.add_field(name='List of Commands', value='-gg help\n•Shows the help panel.\n\n-gg price <item name>\n•Show the latest minimum sell order prices of an item.\n\n-gg quick <item name>\n•Faster version of (-gg price), without statistics.\n\n-gg search <option> <player/guild name>\n•Search and show details about a player or guild (<option> - player or guild).\n\n-gg gold <number of days>\n•Show past 6 hours gold prices, and displays past <number of days> gold prices.', inline=False)

        await ctx.send(embed=embed)
        
		
def setup(client):
    client.add_cog(customCmds(client))