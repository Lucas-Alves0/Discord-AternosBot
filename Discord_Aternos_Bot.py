from python_aternos.atserver import ServerStartError
import python_aternos as aternos
from time import sleep
import discord
from discord.ext import commands
from keep_alive import keep_alive

# Aternos instance

atclient = aternos.Client()
user = {'username':'SrLks7162', 'password':'L6070al#'}
atclient.login(str(user['username']),str(user['password']))
atlog = atclient.account

servs = atlog.list_servers()
myserv = servs[1]
myserv.fetch()

# Discord instance

# Criação de intents necessários
intents = discord.Intents.default()
intents.message_content = True  # Caso precise ler o conteúdo da mensagem
dcbot = commands.Bot(command_prefix="!", intents=intents)
dctoken = {
    'TOKEN':
    'MTMxMzY0NTM4NzkxMDc0NjEyMg.GSY92J.argtbVI8M3VvMjztAbojaj5ZcP1ka4Brc3gyqk'
}


@dcbot.event
async def on_ready():
  print(f'Bot logado como {dcbot.user}')


@dcbot.event
async def on_message(message):
  if message.author == dcbot.user:
    return

  if 'olá aternos' in message.content.lower():
    await message.channel.send(
        f'Olá {message.author.name}!\nVamos começar?\n\nCaso queira iniciar o servidor, digite "!iniciar".\n\nTambém tenho outros comandos, digite "!ajuda" para ver.'
    )

  await dcbot.process_commands(message)


@dcbot.event
async def on_member_join(member):
  channel = dcbot.get_channel('1308960430911393917')
  myserv.fetch()
  await channel.send(f'Seja muito bem vindo {member.mention}, aproveite a play com todos os outros.\n\nEndereço do servidor: {myserv.domain}\n\nPorta: {myserv.port}')


@dcbot.command(name='iniciar')
async def iniciar(ctx):
  myserv.fetch()

  try:
    await ctx.send('Abrindo servidor...')
    myserv.start(headstart=True)
    myserv.fetch()
    await ctx.send(
        f'O servidor está iniciando, aguarde\n\nStatus do servidor: {myserv.status}'
    )
  except ServerStartError:
    await ctx.send('O servidor já está iniciando')


@dcbot.command(name='parar')
async def parar(ctx):
  myserv.fetch()
  await ctx.send('Fechando servidor...')

  try:
    myserv.stop()
  except Exception as e:
    await ctx.send(f'O servidor já está sendo fechado!')
  while myserv.status != 'offline':
    myserv.fetch()
    await ctx.send(
        f'O servidor está sendo fechado, aguarde\n\nStatus de fechamento do servidor: {myserv.status}'
    )
    sleep(10)
  else:
    sleep(10)
    myserv.fetch()
    await ctx.send(f'Servidor: {myserv.status}')


@dcbot.command(name='status')
async def status(ctx):
  myserv.fetch()
  await ctx.send(f'O servidor está {myserv.status}')


@dcbot.command(name='jogadores')
async def jogadores(ctx):
  myserv.fetch()
  await ctx.send(
      f'Jogadores online:\n\n{myserv.players_list}\n\n{myserv.players_count} de {myserv.slots} jogadores online'
  )


@dcbot.command(name='infoserver')
async def infoserver(ctx):
  myserv.fetch()
  await ctx.send(
    f'Endereço:{myserv.domain}\nPorta:{myserv.port}'
  )


@dcbot.command(name='ajuda')
async def ajuda(ctx):
  await ctx.send(
      'Comandos:\n\n!iniciar - Inicia o servidor\n!parar - Para o servidor\n!status - Mostra o status do servidor\n!jogadores - Mostra os jogadores online\n!infoserver - Mostra o endereço e porta do servidor\n!ajuda - Mostra os comandos'
  )


keep_alive()
dcbot.run(dctoken['TOKEN'])