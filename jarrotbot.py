import discord
from discord.ext import commands

import praw, os, random, asyncio, time, typing, requests

DISCORD_BOT_TOKEN="INSERT BOT TOKEN HERE"

REDDIT_APP_ID="GET THIS FROM REDDIT"
REDDIT_APP_SECRET="GET THIS FROM REDDIT FFS"

reddit = praw.Reddit(
    client_id=REDDIT_APP_ID,
    client_secret=REDDIT_APP_SECRET,
    password="Your damn reddit password",
    user_agent="anynameyouwanthere",
    username="your reddit username",
)


Client = discord.Client()
client = commands.Bot(command_prefix = "Set Your Prefix Here")

@client.event
async def on_ready():
  print ("------------------------------------")
  print ("Bot Name: " + client.user.name)
  print ("Discord Version: " + discord.__version__)
  print ("------------------------------------")
  await client.change_presence(activity=discord.Game(name='on SaladMC'))

@client.command()
async def jarrot(ctx):
    em = discord.Embed(title = "Loading jarrot...")
    em.set_thumbnail(url="https://mir-s3-cdn-cf.behance.net/project_modules/disp/35771931234507.564a1d2403b3a.gif")

    message = await ctx.send(embed=em)

    subreddit = reddit.subreddit("jarrot")
    all_subs = []

    top = subreddit.top(limit = 100)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    embed= discord.Embed(title = name)
    embed.set_image(url=url)
    await message.delete()
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def mightyjarrot(ctx,context):

    message = ["https://i.imgur.com/sCthP6y.png","https://i.imgur.com/2ZEmDPp.png","https://i.imgur.com/1lCCwwc.png","https://i.imgur.com/nzcpaW8.png","https://i.imgur.com/hdQgoaT.png","https://i.imgur.com/XpwqV00.png"]
    rndm = random.choice(message)
    embed=discord.Embed(title="Mighty jared")
    embed.set_image(url=rndm)
    await ctx.send(embed=embed)


client.run(DISCORD_BOT_TOKEN)
