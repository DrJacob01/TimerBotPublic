# https://youtu.be/kNUuYEWGOxA?t=467
# https://youtu.be/jh1CtQW4DTo

import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
import asyncio
from discord.ext.commands import bot


bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is ready')
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands") #syncs the commands
    except Exception as e:
        print(e)

# a command that starts a timer for however long the user states (minutes) and then sends a message saying "Timer is done" and @'s the user
@bot.tree.command(name="timer", description="Starts a timer for however long you state")
async def timer(interaction: discord.Interaction, minutes: int):
    await interaction.response.send_message(f"Timer has been set for {minutes} minutes by <@{interaction.user.id}>!")
    await interaction.followup.send("Starting in 3:")
    await asyncio.sleep(1)
    await interaction.followup.send("2:")
    await asyncio.sleep(1)
    await interaction.followup.send("1:")
    await asyncio.sleep(1)
    await interaction.followup.send("GOOOOO!")
    await asyncio.sleep(minutes * 60)
    await interaction.followup.send(f"<@{interaction.user.id}> Timer is done")

'''@bot.tree.command(name="hello", description="Says hello to you")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

# a command that sends "hello" and a green button that says "POSATIVE" and a red button that says "NEGATIVE"
@bot.tree.command(name="hello2", description="Says hello to you")
async def hello2(interaction: discord.Interaction):
    button1 = Button(label="POSATIVE", style=discord.ButtonStyle.green, emoji="👍")
    button2 = Button(label="NEGATIVE", style=discord.ButtonStyle.red, emoji="👎")

    async def button1_callback(interaction):
        await interaction.response.send_message("You clicked POSATIVE!")

    async def button2_callback(interaction):
        await interaction.response.send_message("You clicked NEGATIVE!")

    button1.callback = button1_callback
    button2.callback = button2_callback

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    await interaction.response.send_message('Hello!', view=view)'''


'''@bot.command()
async def hello(ctx):
    button1 = Button(label="POSATIVE", style=discord.ButtonStyle.green, emoji="👍")
    button2 = Button(label="NEGATIVE", style=discord.ButtonStyle.red, emoji="👎")
    button3 = Button(label="FUNNY", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    async def button1_callback(interaction):
        await interaction.response.send_message("You clicked POSATIVE!")

    async def button2_callback(interaction):
        await interaction.response.send_message("You clicked NEGATIVE!")

    async def button3_callback(interaction):
        await interaction.response.send_message("You clicked FUNNY!") # This will never be called because the URL button opens the URL in the browser

    button1.callback = button1_callback
    button2.callback = button2_callback
    button3.callback = button3_callback

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    await ctx.send('Hello!', view=view)'''

bot.run('')