#!/usr/bin/env python3.5

import discord
import asyncio
from discord.ext import commands
import logging
from datetime import datetime, date, time, timedelta
import sys
import random
import math
import config #config file that contains api keys

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

client = discord.Client()


@client.event
async def on_message(message):

    #print (message.server)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #testserver = client.get_server('481172019518373899')
    #testserver = discord.Server(id='481172019518373899')
    #print ("Server:")
    #print (testserver)

   # headcrabs = {
   #            "server": discord.Server(id='147850792626290688'),
   #            "role": discord.Role(server=discord.Server(id='147850792626290688'), id='232961867448975360'),
   #            "permissions": discord.Permissions(send_messages=False)
   #             }
   
    #role = discord.utils.get(discord.Server(id='147850792626290688').roles, name="mutes")

    if message.content.startswith('<:fendi_no'):
        testserver = message.server
        #badrole = discord.utils.get(testserver.roles, name="badrole")
        badrole = discord.utils.get(testserver.roles, id="410209923964731393")
        #goodrole = discord.utils.get(testserver.roles, name="goodrole")
        goodrole = discord.utils.get(testserver.roles, id="481172194903195668")
        doomsday = testserver.get_member('90033106198761472')
        await asyncio.sleep(random.random()*3)
        if discord.utils.get(doomsday.roles, id="410209923964731393") is None:
            msg = 'Moving to mutes'.format(message)
            await client.send_message(message.channel, msg)
            print ('adding {0} to role {1}'.format(doomsday, badrole))
            await client.add_roles(doomsday, badrole)
            await asyncio.sleep(1)
            # print ('removing {0} from role {1}'.format(doomsday, goodrole))
            # await client.remove_roles(doomsday, goodrole)
            #loop.call_later(10, unmute, loop2)
            await asyncio.sleep(300) # wait 10 seconds, then unmute
            await asyncio.sleep(random.random()*3)
            msg = 'Unmuting'.format(message)
            await client.send_message(message.channel, msg)
            # print ('adding {0} to role {1}'.format(doomsday, goodrole))
            # await client.add_roles(doomsday, goodrole)
            await asyncio.sleep(1)
            print ('removing {0} from role {1}'.format(doomsday, badrole))
            await client.remove_roles(doomsday, badrole)
            

    # if the message has more than 5 words and a 1/100 chance
    if len(message.content.split(' ')) > 5 and random.randint(1,42) == 8:
            # rembot resurrection 
            #print ('Test')
            #print (type(message.content))
            words = message.content.split(' ')
            print (words)
            wordToReplace = math.floor(random.random() * len(words))
            #print (wordToReplace)
            word2ToReplace = math.floor(random.random() * len(words))
            #print (word2ToReplace)
            if word2ToReplace == wordToReplace:
               # find a new word
               word2ToReplace = word2ToReplace - 1
            firstword = words[wordToReplace]
            secondword = words[word2ToReplace]
            newwords = ["I'll", firstword, "your", secondword]
            remmessage = ' '.join(newwords)
            print (newwords)
            await client.send_message(message.channel, remmessage)

    # if the message has more than 3 words and a 1/100 chance
    if len(message.content.split(' ')) > 3 and random.randint(1,100) == 25:
    #if str(message.server) == 'Paul_testserver' and len(message.content.split(' ')) > 3:
            # buttbot resurrection 
            words = message.content.split(' ')
            print (words)
            wordToReplace = math.floor(random.random() * len(words))
            words[wordToReplace] = 'butt'
            buttmessage = ' '.join(words)
            print (buttmessage)
            await client.send_message(message.channel, buttmessage)
            
            
# documentation
# steamtoid server ID = 147850792626290688
# fendi ID = 90033106198761472
# mute ID = 410209923964731393
# headcrabs ID = 232961867448975360

# test server ID = 481172019518373899
# walt test ID = 141046693176016896
# DF test ID = 230883507243712513
# grant = 137896130020114432
# lee = 201937511746895875

# https://discordapp.com/oauth2/authorize?client_id=234158064167682050&scope=bot
# test server roles 'roles': ['481172194903195668', '481172122719223830']
# badrole = 481172122719223830
# goodrole = 481172194903195668


#<:fendi_no:481185602017165322>

@client.event
async def on_ready():
    #loop.call_soon(hello_world, loop)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.version_info)

client.run(config.discord_bot_token)
