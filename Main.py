import discord
import os
from discord.ext import commands
import requests
import json
from googlesearch import search

client = commands.Bot(command_prefix="=", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Class Buddy is ready to serve you!")
    print("---------------------------------")

client.load_extension('remind')
client.load_extension('music')
client.load_extension('motivation')

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am your Class Buddy!")

@client.command()
async def thanks(ctx):
    await ctx.send("Happy to serve you anytime!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(1000828970767482991)
    await channel.send("Welcome! I can't wait to help you in your ITMGT class")

@client.command()
async def announcements(ctx, title, url, date, points):
    embed = discord.Embed(title=title,
                          url=url,
                          description="Keep in my mind:",
                          color=0x4dff4d)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://www.allthingsdogs.com/corgi-mix/")
    embed.add_field(name="Due date: " + date,
                    value="Total Points: " + points,
                    inline=False)
    embed.set_footer(text="Thank you for reading!")
    channel = client.get_channel(1000797034355368009)
    await channel.send(embed=embed)

@client.command()
async def gmeet(ctx):
    embed = discord.Embed(title="Google Meet Class Link",
                          url="https://meet.google.com/owk-pgiy-aao",
                          description="Please Click")
    await ctx.send(embed=embed)


@client.command()
async def canvas(ctx):
    embed = discord.Embed(title="Canvas Link",
                          url="https://ateneo.instructure.com/courses/23438",
                          description="Do not forget about me.")
    await ctx.send(embed=embed)

def give_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -"+ json_data[0]['a']
    return quote

@client.command()
async def quote(ctx):
  quote = give_quote()
  await ctx.send(quote)

@client.command()
async def find(ctx,*, query):
		author = ctx.author.mention
		await ctx.channel.send(f"Here are the links related to your question {author} !")
		async with ctx.typing():
				for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
						await ctx.send(f"\n:point_right: {j}")
				await ctx.send("Have any more questions:question:\nFeel free to ask again :smiley: !")

my_token = os.environ['Key']
client.run(my_token)
