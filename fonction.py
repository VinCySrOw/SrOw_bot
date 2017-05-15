# -*- coding: utf-8 -*-
import discord, sys, asyncio, re, random, os, time, platform, socket, psutil, cpuinfo
from requests import get
from discord.ext.commands import Bot
from discord.ext import commands

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

'''
Events...
'''

async def on_bot_ready_events(client):
    print (bcolors.OKGREEN + (time.strftime("%d/%m/%Y %H:%M:%S :")), ("Connexion de {} avec l'id {}").format(client.user.name, client.user.id) + bcolors.ENDC)
    em = discord.Embed(title='Le bot a redémarré', description="Nous nous éfforçons de continuellement améliorer le bot,\nce redémarrage est pour nous le seul moyen pour mettre a jour Franky.\nNous sommes désolés pour les désagréments.", colour=0x43b581)
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await client.send_message(client.get_channel('310127519753830400'), embed=em)
    await client.change_presence(game=discord.Game(name='!help ｜ BETA v0.3'))

async def on_member_join_events(member, client):
    server = member.server
    fmt = "{0.mention} a rejoint le serveur !"
    await client.send_file(server, 'bot_ribbons/bienvenue-ribbon-yellow-stitched.png')
    await client.send_message(server, "Bienvenue sur le serveur, {0.mention}, **!help** pour avoir de l'aide !".format(member))
    await client.add_roles(member, discord.Object("310129439256084482"))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(member.name) + bcolors.ENDC, "s'est connecté", bcolors.WARNING + ("et est devenu Random") + bcolors.ENDC, "avec succès.")

async def on_member_remove_events(member, client):
    server = member.server
    fmt = "{0.mention} a quitté le serveur.."
    await client.send_message(server,fmt.format(member))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(member.name) + bcolors.ENDC, "a quitté le serveur", bcolors.WARNING + (":(") + bcolors.ENDC, "avec succès.")

'''
Here are all te functions that are doing something directly on the bot's server
'''

async def reload_bot():
    python = sys.executable
    os.execl(python, python, * sys.argv)


'''
Here are all the bot's commands on the chat
'''

async def messages_count_cmd(message, client):
    author = message.author
    counter = 0
    tmp = await client.send_message(message.channel, 'Comptage des messages...')
    async for log in client.logs_from(message.channel, limit=100):
        if log.author == message.author:
            counter += 1
    await client.edit_message(tmp, '{}, vous avez écrit {} messages dans ce salon.'.format(author.name, counter))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!messages_count") + bcolors.ENDC, "avec succès.")

async def sleep_cmd(message, client):
    author = message.author
    await client.send_typing(message.channel)
    arg = 0
    msg = message.content
    argument = re.findall('\d+', msg)
    try:
        arg = int(argument[0])
    except IndexError:
        arg = int(5)
    await asyncio.sleep(arg)
    await client.send_message(message.channel, "Aaaaah j'ai bien dormi !")
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!sleep") + bcolors.ENDC, "avec succès.")

async def help_cmd(message, client):
    author = message.author
    await client.send_file(message.channel, 'bot_ribbons/help-ribbon-yellow-stitched.png')
    await client.send_message(message.channel, "**!messages_count** : Savoir combien de messages vous avez sur le channel \n**!clear** : Nettoie le channel **(doit être éxécutée par un admin)** \n**!askfranky** : Vous répond Oui, Non ou Peut-être de manière aléatoire \n**!sleep** : Donnez un peu de repos a Franky ! \n**!reload** : Redémarre le bot **(doit être éxécutée par un admin)** \n**!botsysteminfo** : Donne des informations sur le système du bot\n**!gitbot** : Envoi un lien vers le répertoire GitHub du bot\n**!admincall** : Appelles un admin **(a utiliser uniquement en cas de besoin réel !)**\n**!ping** : Vous donne le temps de latence entre le serveur du bot et Google France\n**!frankyonmyserver** : Vous permet d'ajouter Franky sur votre serveur !")
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!help") + bcolors.ENDC, "avec succès.")

async def clear_cmd(message, client):
    author = message.author
    if author.server_permissions.administrator == True:
        counter = 0
        tmp = await client.send_message(message.channel, 'Nettoyage des messages...')
        await asyncio.sleep(5)
        async for msg in client.logs_from(message.channel):
            counter += 1
            await client.delete_message(msg)
        await client.send_message(message.channel, '{} messages ont été supprimés dans ce salon.'.format(counter))
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!clear") + bcolors.ENDC, "avec succès.")
    else:
        await client.send_message(message.channel, "<:warning_sign:312526599473856512> **Vous n'êtes pas autorisé a faire cela !**")
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, bcolors.FAIL + "a éxécuté la commande" + bcolors.ENDC, bcolors.WARNING + ("!clear") + bcolors.ENDC, bcolors.FAIL + "sans y être autorisé." + bcolors.ENDC)
        await client.send_message(discord.Object("312523151126953984"), "**{}** a tenté d'éxécuter la commande **!clear** dans **{}**".format(author.mention, message.channel.mention))


async def  ask_franky_cmd(message, client):
    author = message.author
    await client.send_typing(message.channel)
    await asyncio.sleep(5)
    options = ["Oui","Non","Peut-être"]
    option = random.choice(options)
    await client.send_file(message.channel, 'bot_ribbons/askfranky-ribbon-yellow-stitched.png')
    await client.send_message(message.channel, '{}'.format(option))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!askfranky") + bcolors.ENDC, "avec succès.")

async def reload_cmd(message, client):
    author = message.author
    if author.server_permissions.administrator == True:
        tmp = await client.send_message(message.channel, "**Redémarrage du bot en cours.**")
        await client.edit_message(tmp, "**Redémarrage du bot en cours.**")
        await asyncio.sleep(1)
        tmp = await client.edit_message(tmp, "**Redémarrage du bot en cours..**")
        await asyncio.sleep(1)
        await client.edit_message(tmp, "**Redémarrage du bot en cours...**")
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!reload") + bcolors.ENDC, "avec succès.")
        await reload_bot()
    else:
        await client.send_message(message.channel, "<:warning_sign:312526599473856512> **Vous n'êtes pas autorisé a faire cela !**")
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, bcolors.FAIL + "a éxécuté la commande" + bcolors.ENDC, bcolors.WARNING + ("!reload") + bcolors.ENDC, bcolors.FAIL + "sans y être autorisé." + bcolors.ENDC)
        await client.send_message(discord.Object("312523151126953984"), "**{}** a tenté d'éxécuter la commande **!reload** dans **{}**".format(author.mention, message.channel.mention))

async def bot_system_info(message, client):
    await client.send_file(message.channel, 'bot_ribbons/botsysteminfo-ribbon-yellow-stitched.png')
    await client.send_typing(message.channel)
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
    await client.send_message(message.channel, "**Configuration matérielle du serveur :**\nProcesseur : **{}**\nMémoire RAM : **{}**Gb\nCapacité totale du disque : **{}**Gb\nLe serveur du bot est hébergé par **Amazon USA Ouest (Oregon)**\n\n**Utilisation actuelle du serveur :**\nL'utilisation actuelle du processeur est de **{}**%\nL'utilisation actuelle de la RAM est de **{}**Gb\nL'utilisation du disque et de : **{}**Gb\nL'adresse IP du serveur du bot est **{}**".format(info_cpu, round(mem_total, 2), round(st, 2), currentUsageCPU, round(currentRamUsage, 3), round(disk_used, 2), extIP))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!botsysteminfo") + bcolors.ENDC, "avec succès.")

async def bot_github(message, client):
    author = message.author
    await client.send_file(message.channel, 'bot_ribbons/gitbot-ribbon-yellow-stitched.png')
    await client.send_message(message.channel, "Voici le répertoire GitHub du bot, n'oubliez pas de donner crédits si vous en faite usage..")
    await client.send_typing(message.channel)
    await asyncio.sleep(5)
    em = discord.Embed(title='Voici le lien :', description='[Répertoire GitHub : SrOw_bot par SrOw](https://github.com/VinCySrOw/SrOw_bot)', colour=0x43b581)
    em.set_author(name='GitHub', icon_url="https://github.com/fluidicon.png")
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await client.send_message(message.channel, embed=em)
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!gitbot") + bcolors.ENDC, "avec succès.")

async def admin_call(message, client):
    author = message.author
    await client.send_file(message.channel, 'bot_ribbons/admincall-ribbon-yellow-stitched.png')
    await client.send_message(message.channel, "Un administrateur a été appelé.")
    await client.send_message(discord.Object("312523151126953984"), "**{}** a appelé un admin dans **{}**".format(author.mention, message.channel.mention))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a appelé un admin dans", bcolors.WARNING + ("#{}".format(message.channel.name)) + bcolors.ENDC, "avec succès.")

async def ping(message, client):
    ping_FR = os.popen("ping -c 1 www.google.fr | tail -1| awk '{print $4}' | cut -d '/' -f 2").read()
    ping_FR = float(ping_FR)
    await client.send_file(message.channel, 'bot_ribbons/ping-ribbon-yellow-stitched.png')
    await client.send_message(message.channel, "Le serveur a **{}**ms de ping vers Google France.".format(round(ping_FR,2)))
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!ping") + bcolors.ENDC, "avec succès.")

async def franky_on_my_server(message, client):
    em = discord.Embed(title='Franky sur votre serveur !', description="Pour ajouter Franky a votre serveur, cliquez **[sur ce lien !](https://discordapp.com/oauth2/authorize?client_id=313592994886320139&scope=bot&permissions=0)", colour=0x43b581)
    em.set_author(name='SrOw')
    em.set_footer(text=time.strftime("Le %d/%m/%Y à %H:%M:%S"))
    await client.send_message(message.channel, embed=em)