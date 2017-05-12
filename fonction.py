# -*- coding: utf-8 -*-
import discord, sys, asyncio, re, random, os, time, platform, socket, psutil
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
Commonly used Variables
'''

is_Admin = discord.Permissions.administrator

'''
Events...
'''

async def on_bot_ready_events(client):
    print (bcolors.FAIL + (time.strftime("%d/%m/%Y %H:%M:%S :")), ("Connexion de {} avec l'id {}").format(client.user.name, client.user.id)+ bcolors.ENDC)
    await client.send_message(client.get_channel('310127519753830400'), "<:green_check_mark:312524276760707074> **Le bot a démarré sans erreur !**")

async def on_member_join_events(member, client):
    server = member.server
    fmt = "{0.mention} a rejoint le serveur !"
    await client.send_message(server,fmt.format(member))
    await client.send_message(server, "!help pour une liste des commandes !")
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
    await client.send_message(message.channel, '**!messages_count** : Savoir combien de messages vous avez sur le channel \n**!clear** : Nettoie le channel **(doit être éxécutée par un admin)** \n**!askfranky** : Vous répond Oui, Non ou Peut-être de manière aléatoire \n**!sleep** : Donnez un peu de repos a Franky ! \n**!reload** : Redémarre le bot **(doit être éxécutée par un admin)** \n**!botsysteminfo** : Donne des informations sur le système du bot\n**!gitbot** : Envoi un lien vers le répertoire GitHub du bot')
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
        await client.send_message(discord.Object("312523151126953984"), "**{}** a tenté d'éxécuter la commande **!clear** dans **#{}**".format(author.name, message.channel))


async def  ask_franky_cmd(message, client):
    author = message.author
    await client.send_typing(message.channel)
    await asyncio.sleep(5)
    options = ["Oui","Non","Peut-être"]
    option = random.choice(options)
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
        await client.send_message(discord.Object("312523151126953984"), "**{}** a tenté d'éxécuter la commande **!reload** dans **#{}**".format(author.name, message.channel))

async def bot_system_info(message, client):
    author = message.author
    tmp = await client.send_message(message.channel, "**Chargement des données.**")
    await client.edit_message(tmp, "**Chargement des données.**")
    await asyncio.sleep(1)
    tmp = await client.edit_message(tmp, "**Chargement des données..**")
    await asyncio.sleep(1)
    await client.edit_message(tmp, "**Chargement des données...**")
    networkAdress = socket.gethostbyname(socket.gethostname())
    currentUsageCPU = psutil.cpu_percent()
    pid = os.getpid()
    py = psutil.Process(pid)
    currentRamUsage = py.memory_info()[0]/2.**30
    os_uname = os.uname()
    await client.edit_message(tmp, "L'utilisation actuelle du processeur est de **{}**%".format(currentUsageCPU))
    await client.send_message(message.channel, "L'utilisation actuelle de la RAM est de **{}**Gb".format(round(currentRamUsage, 3)))
    await client.send_message(message.channel, "L'adresse IP du serveur du bot est **{}**".format(networkAdress))
    await client.send_message(message.channel, "Le serveur du bot est hébergé par **Amazon**")
    print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!botsysteminfo") + bcolors.ENDC, "avec succès.")

async def bot_github(message, client):
    author = message.author
    await client.send_message(message.channel, "Voici le répertoire GitHub du bot, n'oubliez pas de donner crédits si vous en faite usage..")
    await client.send_typing(message.channel)
    await asyncio.sleep(5)
    await client.send_message(message.channel, "https://github.com/VinCySrOw/SrOw_bot")

async def get_role(message, client):
    author = message.author
    if author.server_permissions.administrator == True:
        await client.send_message(message.channel, "Ok c'est bon")
    else:
        await client.send_message(message.channel, "Vous n'êtes pas autorisé a faire cela.")














