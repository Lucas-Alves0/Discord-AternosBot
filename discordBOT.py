import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"We've logged in as {client.user}")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')

client.run('MTMxMzE0MTc5Mjk5NjMyNzUxNQ.GfNlys.NnKuaDDHd5YBqJfjwRIE3lbuISPrkH2N3nT3ks')