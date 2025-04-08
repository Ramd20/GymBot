import discord
import scraper
import os
from dotenv import load_dotenv

load_dotenv()  # load variables from .env into environment

SECRET_TOKEN = os.getenv("SECRET_TOKEN")
ACTIVE = os.getenv("ACTIVE", "False") == "True"

class Client(discord.Client):
    async def on_ready(self):
        print("Running Gym Bot")

    async def on_message(self, message):
        if message.content[0] == "!":
            if message.author == self.user:
                return

            if not ACTIVE:
                await message.channel.send("Bot Hours: 9am to 11pm")
                return

            userMessage = message.content.lower()[1:] #to ignore !
            if userMessage == "war" or userMessage == "mccomas":
                await message.channel.send(scraper.scrapeGym(userMessage))



intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(SECRET_TOKEN)