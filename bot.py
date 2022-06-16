import discord

import random as rand

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.help'):
        await message.channel.send('Hello! I am DanoBot! I scrape images from the web and send them to you! Use .d or .dano for a picture!')

    if message.content.startswith('.dano'):
        # Generate a random number to select an image
        imgInt = rand.randint(0,137)
        imgStr = str(imgInt)
        # Sends message after pulling from a /imgs directory with images 0-137.jpg
        await message.channel.send('Dano Number: ' + imgStr)
        await message.channel.send(file=discord.File('imgs\\' + imgStr + '.jpg'))

client.run("TOKEN")
