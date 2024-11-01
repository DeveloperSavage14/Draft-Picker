import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Add this line

bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync commands with Discord
    print(f'Logged in as {bot.user}')

@tree.command(name="draft", description="Starts drafting")
@app_commands.choices(start=[
    app_commands.Choice(name="Enemy", value="enemy"),
    app_commands.Choice(name="Friendly", value="friendly")
])
async def draft(interaction: discord.Interaction, start: str, details: str = None):
    if details:
        await interaction.response.send_message(f"You chose {start} with details: {details}")
    else:
        await interaction.response.send_message(f"You chose {start}")



bot.run('MTMwMTcxMzYzOTE0OTAxNTA2MA.G4mUTt.1ZmqlMnRwNfGtJ9NEMAjzaQhoMnReD-2pDyTTY')
