import os
from chatcompletion import chat_bot
import openai
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')
DISC_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print("We have logged in!".format(client))

@tree.command(name = "hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hey <@{}> ! This is a slash command!".format(interaction.user.id))

@tree.command(name = "chat")
async def chat(interaction: discord.Interaction, chat_message: str):
    await interaction.response.send_message(chat_bot(chat_message))

client.run(DISC_TOKEN)