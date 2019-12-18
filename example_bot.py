import discord
from discord.ext import commands
import time
import asyncio

client = commands.Bot(command_prefix='!')

joined = 0
messages = 0
leaving = 0

# logging statistics of the server into stats.txt
async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            # update every 24 hours
            await asyncio.sleep(86400)
        except Exception as e:
            print(e)
            await asyncio.sleep(86400)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == "normal": # check that we are sending in normal channel
            await channel.send_message(f"""Welcome to the server :b:ruh {member.mention}""")
    # print to console
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    global leaving
    leaving += 1
    for channel in member.guild.channels:
        if str(channel) == "normal":
            await channel.send_message(f""":b:ruh has left the server {member.mention}""")
    # print to console
    print(f'{member} has left the server')


@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(201857474855305217)
    print(message.content) # Log all messages into console

    if message.content.find("!hello") != -1:
        await message.channel.send("What's god :b:ruh!")
    elif message.content == "!users":
        await message.channel.send(f"""# of :b:ruhs in the server: {id.member_count}""")

@client.command()
async def bing(ctx):
    await ctx.send(':b:ong!')

@client.command()
async def hello(ctx):
    await ctx.send("What's good :b:ruh!")

@client.command()
async def users(ctx):
    id = ctx.guild
    await ctx.send(f"""# of :b:ruhs in the server: {id.member_count}""")

client.loop.create_task(update_stats())
client.run("NTI3Njk4Njk5MjgzODU3NDA5.Xfkegw.OiQiYaEneSuWHLPkET-OpwPe2cI")
