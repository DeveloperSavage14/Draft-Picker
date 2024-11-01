import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}')

enemy1 = "???"
enemy2 = "???"
enemy3 = "???"
friendly1 = "???"
friendly2 = "???"
friendly3 = "???"
@tree.command(name="draft", description="Starts drafting")
@app_commands.choices(start=[
    app_commands.Choice(name="Enemy", value="enemy"),
    app_commands.Choice(name="Friendly", value="friendly")
])
async def draft(interaction: discord.Interaction, start: str, user1: str, user2: str, user3: str):
    image_url = "https://example.com/image.jpg"
    embed = discord.Embed(title="Drafting Session")
    embed.set_image(url=image_url)
    
    # Add fields to make a 3x2 table
    embed.add_field(name="Enemy1", value=enemy1 if enemy1 else "????", inline=True)
    embed.add_field(name="Enemy2", value=enemy2 if enemy2 else "????", inline=True)
    embed.add_field(name="Enemy3", value=enemy3 if enemy3 else "????", inline=True)
    embed.add_field(name=user1, value=friendly1 if friendly1 else "????", inline=True)
    embed.add_field(name=user2, value=friendly2 if friendly2 else "????", inline=True)
    embed.add_field(name=user3, value=friendly3 if friendly3 else "????", inline=True)

    await interaction.response.send_message(embed=embed)

bot.run(token)
