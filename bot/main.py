import discord
import os
from dotenv import load_dotenv

load_dotenv('.env.txt')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('https://discord.gg') or message.content.startswith('https://discord.com/invite/'):
        print("Sniffed invite: " + message.content)

t = os.getenv("TOKEN")
client.run(t)