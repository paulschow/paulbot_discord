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
import emojipastagenerator as Emojipasta

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

client = discord.Client()


@client.event
async def on_message(message):

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #if message.content.startswith('<:fendi_no'):
    if 'fendi_no' in message.content:
    # this mutes a particular user for 5 minutes when a specific emote is used
        muterole = discord.utils.get(message.server.roles, id="410209923964731393")
        fendiuserid = message.server.get_member('90033106198761472')
        await asyncio.sleep(random.random())
        # don't do anything if fendi is already muted
        if discord.utils.get(fendiuserid.roles, id="410209923964731393") is None:
            if random.randint(1,10) == 27 and message.author.id != '147851234328444929' and message.author.id != '90033106198761472' and message.author.id != '230883507243712513' and message.author.id != '108658728194019328':
                # random chance to backfire and mute the wrong person
                # but don't do it to me, fendi, DF, or sol
                #TODO clean this up lmao
                await asyncio.sleep(random.random())
                usertomute = message.author
                await client.send_typing(message.channel)
                await asyncio.sleep(random.random())
                await client.send_message(message.channel, 'How about I mute ' + message.author.mention + ' instead?')
            elif random.randint(1,2) == 2 and message.author.id == '141046693176016896':
                # 50% chance to mute walt
                await asyncio.sleep(random.random())
                usertomute = message.author
                await client.send_typing(message.channel)
                await asyncio.sleep(random.random())
                await client.send_message(message.channel, 'How about I mute ' + message.author.mention + ' instead?')
            else:
                usertomute = message.server.get_member('90033106198761472')
                await client.send_typing(message.channel)
                await asyncio.sleep(random.random())
                msg = 'Moving to mutes'.format(message)
                await client.send_message(message.channel, msg)

            #print ('adding {0} to role {1}'.format(usertomute, muterole))
            await client.add_roles(usertomute, muterole)
            await asyncio.sleep(1)
            await asyncio.sleep(300) # wait 5 minutes, then unmute
            await client.send_typing(message.channel)
            await asyncio.sleep(random.random())
            msg = 'Unmuting'.format(message)
            await client.send_message(message.channel, msg)
            await asyncio.sleep(1)
            #print ('removing {0} from role {1}'.format(usertomute, muterole))
            await client.remove_roles(usertomute, muterole)
            



    # if the message has more than 5 words and a 1/69 chance
    if len(message.content.split(' ')) > 5 and random.randint(1,69) == 8:
            # rembot resurrection
            # takes two words and puts them in an I'll X your Y format
            words = message.content.split(' ')
            #print (words)
            wordToReplace = math.floor(random.random() * len(words))
            word2ToReplace = math.floor(random.random() * len(words))
            # don't use the same word twice thanks
            if word2ToReplace == wordToReplace:
               # find a new word
               word2ToReplace = word2ToReplace - 1
            firstword = words[wordToReplace]
            secondword = words[word2ToReplace]
            # don't even bother if the words are less than or equal to 2 letters
            if len(firstword) <= 2 or len(secondword) <= 2:
                return
            # remove plurals (100% guaranteed to work in English)
            if firstword.endswith("s"):
                firstword = firstword[:-1]
            newwords = ["I'll", firstword, "your", secondword]
            remmessage = ' '.join(newwords)
            #print (newwords)
            await client.send_typing(message.channel)
            await asyncio.sleep(random.random())
            await client.send_message(message.channel, remmessage)

    # if the message has more than 3 words and a 1/100 chance
    elif (3 < len(message.content.split(' ')) < 15) and random.randint(1,100) == 25:
            # buttbot resurrection 
            # replaces one word in a message with butt
            words = message.content.split(' ')
            #print (words)
            wordToReplace = math.floor(random.random() * len(words))
            words[wordToReplace] = 'butt'
            buttmessage = ' '.join(words)
            #print (buttmessage)
            await client.send_typing(message.channel)
            await asyncio.sleep(random.random())
            await client.send_message(message.channel, buttmessage)
            
    # if the message has more than 3 words and a 1/96 chance
    elif len(message.content.split(' ')) > 3 and random.randint(1,96) == 33:
            # "You're a X" thing 
            words = message.content.split(' ')
            #print (words)
            wordToGet = math.floor(random.random() * len(words))
            wordgot = words[wordToGet]
            # don't even bother if the word is less than or equal to 2 letters
            if len(wordgot) <= 2:
                return
            # remove plurals (100% guaranteed to work in English)
            if wordgot.endswith("s"):
                wordgot = wordgot[:-1]
            # use a/an correctly
            if wordgot[0] in {'a', 'e', 'i', 'o', 'u'}:
                xwords = ["You're", "an", wordgot]
            else:
                xwords = ["You're", "a", wordgot]
            xmessage = ' '.join(xwords)
            #print (xmessage)
            await client.send_typing(message.channel)
            await asyncio.sleep(random.random())
            await client.send_message(message.channel, xmessage)
            
            
    # if the message has more than 3 words and a 1/184 chance
    elif (3 < len(message.content.split(' ')) < 15) and random.randint(1,184) == 26:
            #CaPiTaLiZe EvErY OtHeR LeTtEr
            words = message.content
            #print (words)
            cap_words = ""
            i = True # capitalize
            for char in words:
                if i:
                    cap_words += char.upper()
                else:
                    cap_words += char.lower()
                if char != ' ':
                    i = not i
            #print (cap_words)
            await client.send_typing(message.channel)
            await asyncio.sleep(random.random())
            await client.send_message(message.channel, cap_words)
            
            
    # if the message has more than 3 words and a 1/64 chance
    elif len(message.content.split(' ')) > 3 and random.randint(1,64) == 26:
    # turns text into emojipasta
    # copied from https://github.com/Kevinpgalligan/EmojipastaBot
        words = message.content
        #print (words)
        #generator = EmojipastaGenerator.of_default_mappings()
        generator = Emojipasta.EmojipastaGenerator.of_default_mappings()
        emoji_words = generator.generate_emojipasta(words)
        #print (emoji_words)
        await client.send_typing(message.channel)
        await asyncio.sleep(random.random())
        await client.send_message(message.channel, emoji_words)
            
            
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
# me = 147851234328444929

# https://discordapp.com/oauth2/authorize?client_id=234158064167682050&scope=bot
# test server roles 'roles': ['481172194903195668', '481172122719223830']
# muterole = 481172122719223830
# goodrole = 481172194903195668


#<:fendi_no:481185602017165322>

#elif str(message.server) == 'Paul_testserver' and len(message.content.split(' ')) > 3:

@client.event
async def on_ready():
    print ('Logged in as: {0} , {1}'.format(client.user.name, client.user.id))
    print(discord.version_info)

client.run(config.discord_bot_token)
