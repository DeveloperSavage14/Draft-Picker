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

@tree.command(name="draft", description="Starts drafting")
@app_commands.choices(start=[
    app_commands.Choice(name="Enemy", value="enemy"),
    app_commands.Choice(name="Friendly", value="friendly")
])
async def draft(interaction: discord.Interaction, start: str, details: str = None):
    image_url = "https://example.com/image.jpg"
    embed = discord.Embed(title="Drafting Session")

    embed.set_image(url=image_url)

    embed.add_field(name="First Pick", value=start, inline=True)
    embed.add_field(name="Details", value=details if details else "No details provided", inline=True)

    await interaction.response.send_message(embed=embed)

bot.run(token)
