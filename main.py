import os, discord, sys, random, time, logging
from turtle import title
from discord.ext import commands
# import off 

# registros con el modulo logger de discord.py 

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# intentos 

intents = discord.Intents.default()
intents.members = True

# info 

prefix = "!"
token = "OTUwNDgwNDk4OTQwMDUxNTM3.YiZh8g._BF6q5QXQLwlNDullduZJ_8p43c"

bot = commands.Bot(command_prefix=prefix) 

# inicio 

@bot.event
async def on_ready():
        print('\nBot iniciado!') # mira el comentario abajo > 
        await bot.change_presence (activity=discord.Activity(type=discord.ActivityType.watching,name='como vender organos')) # esto lo puse a gusto, pero si vos quieres cambialo sin problema xd

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Bienvenido {0.mention} a {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
            # esto lo saque de la guia de discord.py 

# comandos 

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name ="reiniciar")
async def reiniciar(ctx):
    id = str(ctx.author.id)
    if id == 848254286437023805 or 889604243680530463:
        await ctx.send("Reiniciando el bot...")
        restart_bot()
    else: 
        await ctx.send("No tienes los permisos suficientes!")

@bot.command(name ="apagar")
async def apagar(ctx):
    id = str(ctx.author.id)
    if id == 848254286437023805 or 889604243680530463:
        await ctx.send("Apagando el bot ...")
        await ctx.bot.logout()
    else:
        await ctx.send("No tienes los permisos suficientes!")

@bot.command(name= 'ping')
async def ping(ctx):
    antes = time.monotonic()
    m=await ctx.send('Pong!')
    p1=(time.monotonic()-antes)*1000
    p2=(str(p1).split('.'))[0]
    await m.edit(content=f'Pong! (ms={p2})')

@bot.command(name= 'sex')
async def sex(ctx):
    await ctx.message.add_reaction(emoji="🍆")
    await ctx.message.add_reaction(emoji="🍑")

@bot.listen(name= "sex")
async def sex(ctx):
    await ctx.message.add_reaction(emoji="🍆")
    await ctx.message.add_reaction(emoji="🍑")

@bot.command(name="sexo")
async def sexo(ctx):
    message= "**SEXOO**"
    react_nessasge = await ctx.send(message)
    await react_nessasge.add_reaction(emoji="🍆")
    await react_nessasge.add_reaction(emoji="🍑")
 
bot.run(token)

