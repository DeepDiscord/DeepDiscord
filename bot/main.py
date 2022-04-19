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

    if message.content.startswith('https://discord.gg') or message.content.startswith('https://discord.com/invite/') and message.content != "https://discord.gg" or message.content != "https://discord.com/invite/":
        print("Sniffed invite: " + message.content)
        with open("database.txt", "a") as myfile: # something nice about python is it creates the file if it doesn't exsist
            myfile.write(message.content + "\n")

t = os.getenv("TOKEN")
client.run(t)