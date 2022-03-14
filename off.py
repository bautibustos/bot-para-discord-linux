import os, discord, sys

def restart_bot(id):
    print ("Inicie")
    ingresante = int (id) #ingreso
    print ('ingresante:', ingresante)
    if ingresante == 848254286437023805 or 889604243680530463:# gaucho y jack 
        print ("ingresamos")
        os.execv(sys.executable, ['python'] + sys.argv)#restartea el bot
    else:
        print ('error al reiniciar comprovacion incorrecta')

def den_if():
    async def shutdown(ctx):
        await ctx.send('Apagando ...')
        await ctx.bot.logout()

def off_bot(id):
    print ('go')
    ingreso = int (id)
    print (ingreso)

    print ('go')
    if ingreso == 848254286437023805 or 889604243680530463: # gaucho y jack
        print ('go2')
        den_if()
        print ("go3")



        