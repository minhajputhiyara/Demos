# Example code to implement the bot into a forum channel

import discord

intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot is online as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore other bots

    # Replace this with your actual forum channel ID
    allowed_forum_id = "#your channel id"

    # Check if the message is in a thread inside your forum channel
    if isinstance(message.channel, discord.Thread) and message.channel.parent_id == allowed_forum_id:
        if "hello" in message.content.lower():
            await message.reply("Hey there! 👋")

# Replace with your real token
client.run('#your tiken')
