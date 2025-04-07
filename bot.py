import discord
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
from copilotkit_faq import faq_dict

# Load environment variables from .env
load_dotenv()

aclient = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get keys from environment
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Forum Channel ID
allowed_forum_id = 1357411011132395650

# Build FAQ context string from the imported dictionary
context_string = faq_dict

def build_prompt(user_question):
    return f"""
You are a helpful assistant for developers using CopilotKit.
Use the FAQ context below to answer the user's question. Be accurate and include code if relevant.
Only use the context provided and do not make up any information.
If the message is not a question and causual messages like hi hlo reply as friendly.
Include links and codeblocks in the answer use DFM format to answer.

{context_string}

User question: {user_question}
Answer:"""

@client.event
async def on_ready():
    print(f'✅ Bot is online as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if isinstance(message.channel, discord.Thread) and message.channel.parent_id == allowed_forum_id:
        user_question = message.content.strip()

        try:
            # Use the new OpenAI API method
            print("\n\nuser question : ", user_question)
            response = await aclient.chat.completions.create(model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful developer assistant."},
                {"role": "user", "content": build_prompt(user_question)}
            ],
            temperature=0.3)
            print("llm response : ", response.choices)

            answer = response.choices[0].message.content
            await message.reply(answer)

        except Exception as e:
            print(f"❌ Error: {e}")
            await message.reply(f"Hello, We are looking in to this. We will get back to you shortly.")

# Run the bot using token from .env
client.run(DISCORD_TOKEN)