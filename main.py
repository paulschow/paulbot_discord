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

testserver = 'test'

# def hello_world(loop):
    # print('Hello World')
    #loop.stop()

# loop = asyncio.get_event_loop()


# def unmute(loop2):
    # print ('unmuting')
    # testserver = client.get_server('481172019518373899')
    # badrole = discord.utils.get(testserver.roles, name="badrole")
    # goodrole = discord.utils.get(testserver.roles, name="goodrole")
    # doomsday = testserver.get_member('230883507243712513')
    # print ('adding {0} to role {1}'.format(doomsday, goodrole))
    # client.add_roles(doomsday, goodrole)
    # asyncio.sleep(5)
    # print ('removing {0} from role {1}'.format(doomsday, badrole))
    # client.remove_roles(doomsday, badrole)
    #loop.call_later(10, unmute, loop2)

# loop2 = asyncio.get_event_loop()


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
        # print ('badrole:')
        # print (badrole) 
        #goodrole = discord.utils.get(testserver.roles, name="goodrole")
        goodrole = discord.utils.get(testserver.roles, id="481172194903195668")
        #print (goodrole)
        #doomsday = discord.Server(id='481172019518373899').get_member(str(230883507243712513))
        #doomsday = discord.utils.get(message.server.members, name='Walternate')
        doomsday = testserver.get_member('90033106198761472')
        #print (doomsday)
        #msg = 'Hello {0.author.mention}'.format(message)
        #await client.send_message(message.channel, msg)
        #await client.edit_role( headcrabs )
        #await client.edit_role( server, role=discord.Role(id='232961867448975360'), permissions=discord.Permissions(send_messages=False))
        #await client.edit_role( server=discord.Server(id='147850792626290688'), role=discord.Role(server=discord.Server(id='147850792626290688'), id='232961867448975360'), permissions=discord.Permissions(send_messages=False))
        #await edit_channel_permissions(message.channel, target=discord.Role(id='232961867448975360'), overwrite=discord.PermissionOverwrite(send_messages=False))
        #await client.add_roles(member=discord.User(server=discord.Server(id='147850792626290688'),id='90033106198761472'), discord.Role(server=discord.Server(id='147850792626290688'),id='410209923964731393'))
        #await client.add_roles(discord.Server(id='147850792626290688').get_member('147850792626290688'), discord.utils.get(discord.Server(id='147850792626290688').roles, name="mutes"))
        #print ('adding' + doomsday + 'to role' + 'badrole')
        #print (doomsday)
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
            #print ('Test')
            #print (type(message.content))
            words = message.content.split(' ')
            print (words)
            wordToReplace = math.floor(random.random() * len(words))
            #print (wordToReplace)
            #word2ToReplace = math.floor(random.random() * len(words))
            #print (word2ToReplace)
            #if word2ToReplace == wordToReplace:
               # find a new word
               #word2ToReplace = word2ToReplace - 1
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

    
# async def my_background_task():

    # def is_me(m):
        # return m.author == message.author
        # return str(m.author) == "Paul#0814"

    # await client.wait_until_ready()
    # loop = asyncio.get_running_loop()
    # end_time = loop.time() + 5.0
    # while True:
        # print(datetime.datetime.now())
        # if (loop.time() + 1.0) >= end_time:
            # break
        # await asyncio.sleep(1)

#async def my_background_task():

    #def is_me(m):
        #return m.author == message.author
        #return str(m.author) == "Paul#0814"

    #await client.wait_until_ready()
    #counter = 0
    #channel = discord.Object(id='147850792626290688')
    #while not client.is_closed:
    #while not client.is_closed:
        #counter += 1
        #await client.send_message(channel, counter)
        #await client.purge_from(channel, limit=10000, check=is_me, before = datetime.now() - timedelta(hours=24) )
        #await client.send_message(channel, 'Deleted {} message(s)'.format(len(deleted)))
        #raise KeyboardInterrupt
        #sys.exit()
        #await asyncio.sleep(60) # task runs every 60 seconds

    #counter += 1
    #await client.send_message(channel, 'test')
    #await client.send_message(channel, 'Deleting')
    #deleted = client.purge_from(channel, limit=100, check=is_me)
    #await client.send_message(channel, 'Deleted {} message(s)'.format(len(deleted)))
    #await asyncio.sleep(60) # task runs every 60 seconds

#print (message.author)
#print (type(message.author))
#def is_me(m):
    #return m.author == message.author
#    return str(m.author) == "Paul#0814"

#client.send_message(discord.Object(id = '234202626319712257'), 'I will delete myself now...')
#await client.delete_message(msg)
#deleted = client.purge_from("234202626319712257", limit=100, check=is_me)
#client.send_message("234202626319712257", 'Deleted {} message(s)'.format(len(deleted)))

#client.loop.create_task(my_background_task())
# loop.call_soon(hello_world, loop)

#client.loop.create_task(display_date())
client.run(config.discord_bot_token)
#asyncio.run(display_date())
# loop.run_forever()
# loop.close()
