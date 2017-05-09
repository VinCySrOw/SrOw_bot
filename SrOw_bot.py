# -*- coding: utf-8 -*-
import discord, sys, asyncio, re, random, os, time
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

client = discord.Client()

@client.event
async def on_ready():
    print (bcolors.FAIL + (time.strftime("%d/%m/%Y %H:%M:%S :")), ("Connexion de {} avec l'id {}").format(client.user.name, client.user.id)+ bcolors.ENDC)

    await client.send_message(client.get_channel('310127519753830400'), "**Le bot a démarré sans erreur !**")


@client.event
async def on_message(message):

#!messages_count pour savoir combien de message l'utilisateur a posté

    if message.content.startswith('!messages_count'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Comptage des messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        author=message.author
        await client.edit_message(tmp, '{}, vous avez écrit {} messages dans ce salon.'.format(author.name, counter))
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!messages_count") + bcolors.ENDC, "avec succès.")

#!sleep pour tester

    elif message.content.startswith('!sleep'):
        arg = 0
        msg = message.content
        argument = re.findall('\d+', msg)
        try:
            arg = int(argument[0])
        except IndexError:
            arg = int(5)
        await asyncio.sleep(arg)
        await client.send_message(message.channel, "Aaaaah j'ai bien dormi !")
        author=message.author
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!sleep") + bcolors.ENDC, "avec succès.")

#!help pour une liste des commandes

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, '**!messages_count** : Savoir combien de messages vous avez sur le channel \n**!clear** : Nettoie le channel \n**!askfranky** : Vous répond Oui, Non ou Peut-être de manière aléatoire \n**!sleep** : Donnez un peu de repos a Franky ! \n**!reload** : Redémarre le bot')
        author=message.author
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!help") + bcolors.ENDC, "avec succès.")

#!clear pour nettoyer un canal

    elif message.content.startswith("!clear"):
        if message.content.startswith('!clear'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Nettoyage des messages...')
            await asyncio.sleep(5)
            async for msg in client.logs_from(message.channel):
                counter += 1
                await client.delete_message(msg)
        await client.send_message(message.channel, '{} messages ont été supprimés dans ce salon.'.format(counter))
        author=message.author
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!clear") + bcolors.ENDC, "avec succès.")

#!askfranky répond Oui, Non ou Peut-être de manière aléatoire

    elif message.content.startswith("!askfranky"):
        options = ["Oui","Non","Peut-être"]
        option = random.choice(options)
        await client.send_message(message.channel, '{}'.format(option))
        author=message.author
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!askfranky") + bcolors.ENDC, "avec succès.")


    elif message.content.startswith("!reload"):
        tmp = await client.send_message(message.channel, "**Redémarrage du bot en cours.**")
        await client.edit_message(tmp, "**Redémarrage du bot en cours.**")
        await asyncio.sleep(1)
        tmp = await client.edit_message(tmp, "**Redémarrage du bot en cours..**")
        await asyncio.sleep(1)
        await client.edit_message(tmp, "**Redémarrage du bot en cours...**")
        author=message.author
        print (bcolors.WARNING + (time.strftime("%d/%m/%Y %H:%M:%S")) + bcolors.ENDC, ":", bcolors.WARNING + ("{}").format(author.name) + bcolors.ENDC, "a éxécuté la commande", bcolors.WARNING + ("!reload") + bcolors.ENDC, "avec succès.")
        python = sys.executable
        os.execl(python, python, * sys.argv)



client.run("MzEwODg4ODQyNTgyNTU2Njg0.C_EjNA.gwJ4yCCiEMxsQW6ryLYZ57Vss4o")