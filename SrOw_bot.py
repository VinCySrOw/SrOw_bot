# -*- coding: utf-8 -*-
import discord, sys, asyncio, re, random, os, time, platform
from discord.ext.commands import Bot
from discord.ext import commands
import fonction

prefix = "!"
client = discord.Client()
server = discord.Server.name

@client.event
async def on_ready():
    await fonction.on_bot_ready_events(client)

@client.event
async def on_server_join(self):
    print('joining {0}'.format(server.name))

@client.event
async def on_member_join(member):
    await fonction.on_member_join_events(member, client)

@client.event
async def on_member_remove(member):
    await fonction.on_member_remove_events(member, client)

@client.event
async def on_message(message):

    if message.content.startswith(prefix + 'messages_count'):
        await fonction.messages_count_cmd(message, client)

    elif message.content.startswith(prefix + 'sleep'):
        await fonction.sleep_cmd(message, client)

    elif message.content.startswith(prefix + 'help'):
        await fonction.help_cmd(message, client)

    elif message.content.startswith(prefix + 'clear'):
        await fonction.clear_cmd(message, client)

    elif message.content.startswith(prefix + 'askfranky'):
        await fonction.ask_franky_cmd(message, client)

    elif message.content.startswith(prefix + 'reload'):
        await fonction.reload_cmd(message, client)

    elif message.content.startswith(prefix + 'botsysteminfo'):
        await fonction.bot_system_info(message, client)

    elif message.content.startswith(prefix + 'gitbot'):
        await fonction.bot_github(message, client)

    elif message.content.startswith(prefix + 'ping'):
        await fonction.ping(message, client)

    elif message.content.startswith(prefix + 'admincall'):
        await fonction.admin_call(message, client)

    elif message.content.startswith(prefix + 'frankyonmyserver'):
        await fonction.franky_on_my_server(message, client)

client.run("xxxxxxxxxxx")