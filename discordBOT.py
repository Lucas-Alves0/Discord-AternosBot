import discord

client = discord.Client()
token = {
    'TOKEN':'MTMxMzY0NTM4NzkxMDc0NjEyMg.GiJnSi.45RK4BxPMGgoXrzSDZLPjzVnwTDsauEW59HY_Y'
}
@client.event
async def on_ready():
    print(f"We've logged in as {client.user}")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content.startswith('Hello AtBot'):
        await message.channel.send('Hello!')

    if message.content.startswith('How are you?'):
        await message.channel.send("I'm Pretty fine and you?")

client.run(token['TOKEN'])