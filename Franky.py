import discord, sys, asyncio, re, random, os, time, platform, socket, psutil, cpuinfo
from discord.ext import commands
import random
from requests import get
from discord.ext.commands import Bot

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

async def reload_bot():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@bot.event
async def on_ready():
    print (bcolors.OKGREEN + (time.strftime("%d/%m/%Y %H:%M:%S :")), ("Connexion de {} avec l'id {}").format(bot.user.name, bot.user.id) + bcolors.ENDC)
    em = discord.Embed(title='Le bot a redémarré', description="Nous nous éfforçons de continuellement améliorer le bot,\nce redémarrage est pour nous le seul moyen pour mettre a jour Franky.\nNous sommes désolés pour les désagréments.", colour=0x43b581)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.send_message(bot.get_channel('310127519753830400'), embed=em)
    await bot.change_presence(game=discord.Game(name='!help ｜ BETA v0.8'))

@bot.event
async def on_member_join(member):
    server = member.server
    em = discord.Embed(title='Bienvenue sur le serveur, ' + member.name, description="**!help** pour avoir de l'aide !", colour=0x43b581)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.send_message(server, embed=em)
    await bot.add_roles(member, discord.Object("310129439256084482"))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(member.name) + bcolors.ENDC, "s'est connecté", bcolors.WARNING + ("et est devenu Random") + bcolors.ENDC, "avec succès.")

@bot.event
async def on_member_remove(member):
    server = member.server
    em = discord.Embed(title=member.name + ' a quitté le serveur..', colour=0xe74c3c)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.send_message(server, embed=em)
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(member.name) + bcolors.ENDC, "a quitté le serveur", bcolors.WARNING + (":(") + bcolors.ENDC, "avec succès.")

@bot.event
async def on_server_join(server):
    channel = None
    for chan in server.channels:
        if chan.is_default:
            if chan.is_private:
                return
            channel = chan
            break
    if channel is None:
        return
    em = discord.Embed(title='Bonjour, je suis Franky !', description="N'oubliez pas de me donner un rôle ayant les droits d'administration, ou je ne pourrai rien faire pour vous aider..", colour=0x43b581)
    await bot.send_message(channel, embed=em)

@bot.command(pass_context=True)
async def botsysteminfo(ctx):
    message = ctx.message
    await bot.send_typing(message.channel)
    author = message.author
    extIP = get('https://ipapi.co/ip/').text
    networkAdress = socket.gethostbyname(socket.gethostname())
    currentUsageCPU = psutil.cpu_percent()
    pid = os.getpid()
    py = psutil.Process(pid)
    currentRamUsage = py.memory_info()[0]/2.**30
    os_uname = os.uname()
    info = cpuinfo.get_cpu_info()
    info_cpu = info['brand']
    from psutil import virtual_memory
    mem = virtual_memory()
    mem_total = mem.total
    mem_total = mem_total / 1000000000
    st = psutil.disk_usage('/')
    st = st.total / 1000000000
    disk_used = psutil.disk_usage('/')
    disk_used = disk_used.used / 1000000000
    em = discord.Embed(title='Informations sur le serveur du bot :', description="**Configuration matérielle du serveur :**\nProcesseur : **{}**\nMémoire RAM : **{}**Gb\nCapacité totale du disque : **{}**Gb\nLe serveur du bot est hébergé par **Amazon USA Ouest (Oregon)**\n\n**Utilisation actuelle du serveur :**\nL'utilisation actuelle du processeur est de **{}**%\nL'utilisation actuelle de la RAM est de **{}**Gb\nL'utilisation du disque et de : **{}**Gb\nL'adresse IP du serveur du bot est **{}**".format(info_cpu, round(mem_total, 2), round(st, 2), currentUsageCPU, round(currentRamUsage, 3), round(disk_used, 2), extIP), colour=0x3498db)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.say(embed=em)
#    await bot.say("**Configuration matérielle du serveur :**\nProcesseur : **{}**\nMémoire RAM : **{}**Gb\nCapacité totale du disque : **{}**Gb\nLe serveur du bot est hébergé par **Amazon USA Ouest (Oregon)**\n\n**Utilisation actuelle du serveur :**\nL'utilisation actuelle du processeur est de **{}**%\nL'utilisation actuelle de la RAM est de **{}**Gb\nL'utilisation du disque et de : **{}**Gb\nL'adresse IP du serveur du bot est **{}**".format(info_cpu, round(mem_total, 2), round(st, 2), currentUsageCPU, round(currentRamUsage, 3), round(disk_used, 2), extIP))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!botsysteminfo") + bcolors.ENDC, "avec succès.")

@bot.command(pass_context=True)
async def help(ctx):
    message = ctx.message
    author = message.author
    em = discord.Embed(title='Liste des commandes :', description="**!messages_count** : Savoir combien de messages vous avez sur le channel \n**!clear** : Nettoie le channel **(doit être éxécutée par un admin)** \n**!askfranky** : Vous répond Oui, Non ou Peut-être de manière aléatoire \n**!botsysteminfo** : Donne des informations sur le système du bot\n**!gitbot** : Envoi un lien vers le répertoire GitHub du bot\n**!admincall** : Appelles un admin **(a utiliser uniquement en cas de besoin réel !)**\n**!ping** : Vous donne le temps de latence entre le serveur du bot et Google France\n**!frankyonmyserver** : Vous permet d'ajouter Franky sur votre serveur !", colour=0x3498db)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.say(embed=em)
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!help") + bcolors.ENDC, "avec succès.")

@bot.command(pass_context=True)
async def messages_count(ctx):
    message = ctx.message
    author = message.author
    server = author.server
    counter = 0
    async for log in bot.logs_from(message.channel, limit=100):
        if log.author == message.author:
            counter += 1
    counter = str(counter)
    em = discord.Embed(title=author.name + ' vous avez écrit ' + counter + ' messages dans ce salon.', colour=0x3498db)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.send_message(server, embed=em)
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!messages_count") + bcolors.ENDC, "avec succès.")

@bot.command(pass_context=True)
async def reload(ctx):
    message = ctx.message
    author = message.author
    if author.id == '213683309530710016':
        if author.server_permissions.administrator == True:
            print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!reload") + bcolors.ENDC, "avec succès.")
            await reload_bot()
        else:
            em = discord.Embed(title="Vous n'êtes pas autorisé a faire cela !", description="Seuls les administrateurs peuvent lancer cetter commande.", colour=0xe74c3c)
            em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
            await bot.say(embed=em)
            print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, bcolors.FAIL + "a éxécuté la commande" + bcolors.ENDC, bcolors.WARNING + ("!reload") + bcolors.ENDC, bcolors.FAIL + "sans y être autorisé." + bcolors.ENDC)
            em2 = discord.Embed(title=message.author.name + " a tenté d'éxécuter la commande **!reload** dans #" + message.channel.name, colour=0xf39c12)
            em2.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
            await bot.send_message(discord.Object("312523151126953984"), embed=em2)
    else:
        em = discord.Embed(title="Vous n'êtes pas autorisé a faire cela !", description="Seul le créateur du bot peut lancer cette commande.", colour=0xe74c3c)
        em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
        await bot.say(embed=em)

@bot.command(pass_context=True)
async def clear(ctx):
    message = ctx.message
    author = message.author
    if author.server_permissions.administrator == True:
        counter = 0
        tmp = await bot.say('Nettoyage des messages...')
        await asyncio.sleep(5)
        async for msg in bot.logs_from(message.channel):
            counter += 1
            await bot.delete_message(msg)    
        em = discord.Embed(title='Nettoyage terminé', description=("{} messages ont été supprimés dans ce salon.".format(counter)), colour=0x43b581)
        em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
        await bot.say(embed=em)
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!clear") + bcolors.ENDC, "avec succès.")
    else:
        em2 = discord.Embed(title="Vous n'êtes pas autorisé a faire cela !", description="Seuls les administrateurs peuvent lancer cetter commande.", colour=0xe74c3c)
        em2.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
        await bot.say(embed=em2)
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, bcolors.FAIL + "a éxécuté la commande" + bcolors.ENDC, bcolors.WARNING + ("!clear") + bcolors.ENDC, bcolors.FAIL + "sans y être autorisé." + bcolors.ENDC)
        em3 = discord.Embed(title=message.author.name + " a tenté d'éxécuter la commande **!clear** dans #" + message.channel.name, colour=0xf39c12)
        em3.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
        await bot.send_message(discord.Object("312523151126953984"), embed=em3)

@bot.command(pass_context=True)
async def askfranky(ctx):
    message = ctx.message
    author = message.author
    server = author.server
    await bot.send_typing(message.channel)
    await asyncio.sleep(5)
    options = ["Oui","Non","Peut-être"]
    option = random.choice(options)
    em = discord.Embed(title=option, colour=0x3498db)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.send_message(server, embed=em)
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!askfranky") + bcolors.ENDC, "avec succès.")

@bot.command(pass_context=True)
async def gitbot(ctx):
    message = ctx.message
    author = message.author
    server = author.server
    em = discord.Embed(title="Voici le répertoire GitHub du bot, n'oubliez pas de donner crédits si vous en faite usage..", description='[Répertoire GitHub : SrOw_bot par SrOw](https://github.com/VinCySrOw/SrOw_bot)', colour=0x3498db)
    em.set_author(name='GitHub', icon_url="https://github.com/fluidicon.png")
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.say(embed=em)
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!gitbot") + bcolors.ENDC, "avec succès.")

@bot.command(pass_context=True)
async def admincall(ctx):
    message = ctx.message
    author = message.author
    em = discord.Embed(title="Un administrateur a été appelé.", colour=0x43b581)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.say(embed=em)
    em3 = discord.Embed(title=message.author.name + " a appelé un admin dans #" + message.channel.name, colour=0x43b581)
    em3.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.send_message(discord.Object("312523151126953984"), embed=em3)
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a appelé un admin dans", bcolors.WARNING + ("#{}".format(message.channel.name)) + bcolors.ENDC, "avec succès.")

@bot.command(pass_context=True)
async def ping(ctx):
    message = ctx.message
    author = message.author
    ping_FR = os.popen("ping -c 1 www.google.fr | tail -1| awk '{print $4}' | cut -d '/' -f 2").read()
    ping_FR = str(ping_FR)
    em = discord.Embed(title="Le serveur a " + ping_FR + "ms de ping vers Google France", colour=0x43b581)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.say(embed=em)
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!ping") + bcolors.ENDC, "avec succès.")

@bot.command(pass_context=True)
async def frankyonmyserver(ctx):
    message = ctx.message
    author = message.author
    em = discord.Embed(title='Franky sur votre serveur !', description="Pour ajouter Franky a votre serveur, cliquez **[sur ce lien !](https://discordapp.com/oauth2/authorize?client_id=313592994886320139&scope=bot&permissions=0)**", colour=0x43b581)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await bot.say(embed=em)

bot.run('MzEzNTkyOTk0ODg2MzIwMTM5.C_s_GA.SYb-zGr4iQwgxVp2RK9r1ED22Tg')