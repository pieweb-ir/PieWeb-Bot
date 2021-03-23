print("[*] Loading bot...")
import discord
from discord import DMChannel
from discord.ext import commands
import os
import json
import asyncio
from discord import VoiceClient
from discord.utils import get
import sys
import random
import ast
import traceback
import textwrap
import importlib
from contextlib import redirect_stdout
import io
import re
import time
from PIL import Image
from io import BytesIO


intents = discord.Intents(messages=True, guilds=True)
intents.voice_states = True
intents.messages = True 
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix=".",intents=intents)
client.remove_command('help')
token = "ODIzOTU0MjQyOTkzMzg5NjQ3.YFoVLw.BoHVrnaBLO3gaCmM3PpGmVpx7IY"
queue = []



@client.event
async def on_ready():
    dark = client.get_guild(778982572221792267)
    channel = client.get_channel(778982572742672406)
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
    membercount = str(dark.member_count)
    await client.change_presence(status = discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"Watching PieWeb.ir"))
    # channel = client.get_channel(802165998333460551)
    # print(channel)
    # await channel.connect()
    # self = client.get_user(808998635077107722)
    # print(self)
    # await self.edit(self_deaf=True)
# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Please pass in all requirements :rolling_eyes:.')
#     elif isinstance(error, commands.MissingPermissions):
#         await ctx.send("You dont have all the requirements :angry:")
#     elif isinstance(error, commands.BadArgument):
#         await ctx.send('I could not find that member...')
#     else:
#         print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
#         traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

#     # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     # create the background task and run it in the background
    #     self.bg_task = self.loop.create_task(self.my_background_task()

# @client.event
# async def on_member_join(member):
    # channel = client.get_channel(747326745094651944)
    # with open('users.json', 'r') as f:
    #     users = json.load(f)
    # await update_data(users, member)
    # with open('users.json', 'w') as f:
    #     json.dump(users, f)

@client.event
async def on_message(message):
    # if message.author.bot == False:
    #     with open('users.json', 'r') as f:
    #         users = json.load(f)
    #     await update_data(users, message.author)
    #     await add_experience(users, message.author, 5)
    #     await level_up(users, message.author, message)
    #     with open('users.json', 'w') as f:
    #         json.dump(users, f)
    await client.process_commands(message)

def is_owner(ctx):
    return ctx.author.id == 366997934983872512

@client.group(pass_context=True)
async def voice(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid sub command passed...')

@voice.group(pass_context=True)
async def c(ctx):
    if ctx.invoked_subcommand is c:
        await ctx.send('Invalid sub command passed...')

@c.command()
async def limit(ctx,  limit : int):
    print(limit)
    if ctx.author.voice == None:
        await ctx.send('Your not in any voice channel')
    elif ctx.author.voice.channel.category.id == 747071079138197534:
        await ctx.author.voice.channel.edit(user_limit = limit)
@c.command()
async def rename(ctx, *,name : str):
    if ctx.author.voice == None:
        await ctx.send('Your not in any voice channel')
    elif ctx.author.voice.channel.category.id == 747071079138197534:
        await ctx.author.voice.channel.edit(name=name)
channels = []
async def connect():
    channel = client.get_channel(747753070267465749)
    await channel.connect()
    self = client.get_user(752486189419987014)
    await self.edit(deafen=True)

@client.command()   
async def server(ctx):
    message_author = ctx.author
    message_author_avatar = ctx.author.avatar_url
    name = str(ctx.guild.name)
    owner = str(ctx.guild.owner)
    membercount = str(ctx.guild.member_count)
    region = str(ctx.guild.region)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        colour=discord.Color.purple()
    )    
    embed.set_author(name=f"{message_author}", icon_url=f"{message_author_avatar}")
    embed.set_footer(text=f"{client.user.name}#{client.user.discriminator}", icon_url=f"{client.user.avatar_url}")
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner:", value = ctx.guild.owner.mention , inline = True)
    embed.add_field(name="Server Name", value = name, inline=True)
    embed.add_field(name="Region:", value = region, inline=True)
    embed.add_field(name="Total Members:", value = membercount, inline=True)
    await ctx.send (embed=embed) 

@client.command()
async def dm(ctx, user: discord.User, count:int , *, message=None):
    try:    
        i  = 0
        while i <= count:
            message = message
            await user.send(message)
            i += 1
            time.sleep(1)
    except:
        await ctx.send("Current user's DM is closed.")

# @client.command(pass_context =True)
# async def help(ctx):
#     author = ctx.message.author
#     embed = discord.Embed(
#         colour = discord.Colour.dark_blue()
#     )
#     embed.set_author(name='Help')
#     embed.add_field(name='.ping', value='Returns Pong!', inline=True)

#     await author.send(author, embed=embed)   
@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def user(ctx, *, member:discord.Member = None):
    if member == None:
        author = ctx.message.author
        author_id = ctx.message.author.id
        authorAvatarUrl = author.avatar_url
        created_at = author.created_at.strftime("%b %d, %Y")
        joined_at = author.joined_at.strftime("%b, %d, %Y")
        embed = discord.Embed(colour=discord.Colour(0xed558a))
        embed.set_thumbnail(url="{}".format(authorAvatarUrl))
        embed.set_author(name='{}'.format(author), icon_url="{}".format(authorAvatarUrl))
        embed.set_footer(text="{}".format(author), icon_url="https://images-ext-1.discordapp.net/external/JpyzxW2wMRG2874gSTdNTpC_q9AHl8x8V4SMmtRtlVk/https/orcid.org/sites/default/files/files/ID_symbol_B-W_128x128.gif")
        embed.add_field(name="**Joined Discord :**", value="``{}``".format(created_at), inline=True)
        embed.add_field(name="Joined Server :", value="``{}``".format(joined_at), inline=True)
        embed.add_field(name="User ID :", value="``{}``".format(author_id), inline=True)
        await ctx.send(embed=embed)
    else:
        userAvatarUrl = member.avatar_url
        user = member
        user_id = member.id
        created_at = member.created_at.strftime("%b %d, %Y")
        joined_at = member.joined_at.strftime("%b, %d, %Y")
        embed = discord.Embed(colour=discord.Colour(0xed558a))
        embed.set_thumbnail(url="{}".format(userAvatarUrl))
        embed.set_author(name='{}'.format(user), icon_url="{}".format(userAvatarUrl))
        embed.set_footer(text="{}".format(user), icon_url="https://images-ext-1.discordapp.net/external/JpyzxW2wMRG2874gSTdNTpC_q9AHl8x8V4SMmtRtlVk/https/orcid.org/sites/default/files/files/ID_symbol_B-W_128x128.gif")
        embed.add_field(name="**Joined Discord :**", value="``{}``".format(created_at), inline=True)
        embed.add_field(name="Joined Server :", value="``{}``".format(joined_at), inline=True)
        embed.add_field(name="User ID :", value="``{}``".format(user_id), inline=True)  
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, channel:discord.TextChannel, *, text:str):
    await channel.send(text)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def avatar(ctx, *,  avamember : discord.Member=None):
    if avamember == None:
        author = ctx.message.author
        authorProfile = ctx.message.author.avatar_url
        author = ctx.message.author
        authorProfile = ctx.message.author.avatar_url
        userAvatarUrl = author.avatar_url
        embeded = discord.Embed()
        embeded.set_image(url=userAvatarUrl)
        embed = discord.Embed(title="Avatar link", colour=discord.Colour(0x8febff), url='{}'.format(userAvatarUrl))
        embed.set_image(url=userAvatarUrl)
        embed.set_author(name='{}'.format(author), icon_url="{}".format(authorProfile))
        embed.set_footer(text="Requested by {}".format(author), icon_url="{}".format(authorProfile))
        await ctx.send(embed=embed)
    else:
        userAvatarUrl = avamember.avatar_url
        user = avamember
        author = ctx.message.author
        authorProfile = ctx.message.author.avatar_url
        requestor = discord.Member
        requestorProfile = discord.Member.avatar_url
        # await ctx.send(embed=discord.Embed(title=f"test", description=f"test"))
        embeded = discord.Embed()
        embeded.set_image(url=userAvatarUrl)
        embed = discord.Embed(title="Avatar link", colour=discord.Colour(0x8febff), url='{}'.format(userAvatarUrl))
        embed.set_image(url=userAvatarUrl)
        embed.set_author(name='{}'.format(user), icon_url="{}".format(userAvatarUrl))
        embed.set_footer(text="Requested by {}".format(author), icon_url="{}".format(authorProfile))
        await ctx.send(embed=embed)
@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error
@client.command()
async def member_count(ctx):
    await ctx.send(ctx.guild)

@client.command()
async def ping(ctx) :
    """ Pong! """
    ctx.message.delete
    before = time.monotonic()
    message = await ctx.send("***Pong!***")
    asyncio.sleep(3)
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`Your ping is: {int(ping)}ms`")



@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int):
        await ctx.message.delete()
        mention =ctx.author.mention
        await ctx.channel.purge(limit=limit)
        deleteStatus = await ctx.send('Cleared by {}'.format(ctx.author.mention), delete_after=15)
        # await ctx.send(embed=discord.Embed(title=f'Cleared by {mention}'.format(ctx.author.mention)))
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@client.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def rename(ctx, member: discord.Member, *,nick):
    old_name = member.name
    server_old_name =  member.display_name
    if server_old_name != None:
        old_name = member.display_name
    else:
        old_name = member.name
    new_name = nick
    await member.edit(nick=nick)
    await ctx.send(embed=discord.Embed(title=f"{member.name}'s nickname changed by {ctx.author.name}", description=f"Old nickname: **{old_name}** \nNew nickname: **{new_name}** ".format(old_name, new_name)))
@rename.error
async def rename_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("You Need The `rename members` Permissions To Do That Command")

@client.command()
async def join(ctx):
    message = ctx.message
    channel = ctx.author.voice.channel
    user = ctx.author.id
    await message.add_reaction('👍')
    await channel.connect()

@client.command()
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await ctx.voice_client.disconnect()

# #############################################Leveling system############################################


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

# @client.command()
# async def level(ctx, member: discord.Member = None):
#     if not member:
#         id = ctx.message.author.id
#         with open('users.json', 'r') as f:
#             users = json.load(f)
#         lvl = users[str(id)]['level']
#         await ctx.send(f'You are at level {lvl}!')
#     else:
#         id = member.id
#         with open('users.json', 'r') as f:
#             users = json.load(f)
#         lvl = users[str(id)]['level']
#         await ctx.send(f'{member.mention} is at level {lvl}!')
# ########################################################################################################


# @client.command(pass_context=True)
# async def eval(self, ctx, *, body: str):
#         """Evaluates a code"""

#         env = {
#             'bot': self.bot,
#             'ctx': ctx,
#             'channel': ctx.channel,
#             'author': ctx.author,
#             'guild': ctx.guild,
#             'message': ctx.message,
#             '_': self._last_result
#         }

#         env.update(globals())

#         body = self.cleanup_code(body)
#         stdout = io.StringIO()

#         to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

#         try:
#             exec(to_compile, env)
#         except Exception as e:
#             return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

#         func = env['func']
#         try:
#             with redirect_stdout(stdout):
#                 ret = await func()
#         except Exception as e:
#             value = stdout.getvalue()
#             await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
#         else:
#             value = stdout.getvalue()
#             try:
#                 await ctx.message.add_reaction('\u2705')
#             except:
#                 pass

#             if ret is None:
#                 if value:
#                     await ctx.send(f'```py\n{value}\n```')
#             else:
#                 self._last_result = ret
#                 await ctx.send(f'```py\n{value}{ret}\n```')





# #####################################################Play music###############################################


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@client.command()
@commands.check(is_owner)
async def eval_(ctx, *, cmd):
    """Evaluates input.
    Input is interpreted as newline seperated statements.
    If the last statement is an expression, that is the return value.
    Usable globals:
      - `bot`: the bot instance
      - `discord`: the discord module
      - `commands`: the discord.ext.commands module
      - `ctx`: the invokation context
      - `__import__`: the builtin `__import__` function
    Such that `>eval 1 + 1` gives `2` as the result.
    The following invokation will cause the bot to send the text '9'
    to the channel of invokation and return '3' as the result of evaluating
    >eval ```
    a = 1 + 2
    b = a * 2
    await ctx.send(a + b)
    a
    ```
    """
    fn_name = "_eval_expr"

    cmd = cmd.strip("` ")

    # add a layer of indentation
    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    # wrap in async def body
    body = f"async def {fn_name}():\n{cmd}"

    parsed = ast.parse(body)
    body = parsed.body[0].body

    insert_returns(body)

    env = {
        'bot': ctx.bot,
        'discord': discord,
        'commands': commands,
        'ctx': ctx,
        '__import__': __import__
    }
    exec(compile(parsed, filename="<ast>", mode="exec"), env)

    result = (await eval(f"{fn_name}()", env))
    await ctx.send(result)

@client.command()
async def move(ctx,member:discord.Member=None):
    author = ctx.message.author
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    if not member:
        await ctx.send("Who am I trying to move? Use .move @user")
    else:
        await ctx.send("You are not connected to voice!")    
    await member.move_to(channel)
@client.command()
async def uptime(ctx):
    await ctx.send(f"{client.uptime}")

"""                                        Ticket section                               """



def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@client.command()
@commands.check(is_owner)
async def restart(ctx):
    await ctx.message.delete()
    message = await ctx.send("Restarting... Allow up to 5 seconds", delete_after=10)
    restart_program()

@client.command()
@commands.check(is_owner)
async def shutdown(ctx):
    '''Schaltet mich ab :( (BOT OWNER ONLY)'''
    await ctx.send('**:ok:** Bye!')
    #self.bot.gamesLoop.cancel()
    await ctx.logout()
    sys.exit(0)
client.run(token)
