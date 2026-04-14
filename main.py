import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# --- جزء خادم الويب (مهم جداً لـ Render) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- جزء البوت ---
intents = discord.Intents.all()  # تأكد أنك فعلت الخيارات في صفحة المطورين كما فعلنا سابقاً
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')
    print('------')

# استدعاء خادم الويب
keep_alive()

# ضع التوكن الخاص بك هنا
client.run('ضـع_تـوكـن_بـوتـك_هـنـا')
