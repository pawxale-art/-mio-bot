from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_flask, daemon=True).start()
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower() == "ciao":
        await message.channel.send(f"Ciao {message.author.mention} come stai? 🥰")
    await bot.process_commands(message)
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")
@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao {ctx.author.mention} come stai? 🥰")
bot.run(os.getenv("DISCORD_TOKEN"))
