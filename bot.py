from discord.ext import commands,tasks
from lists import *
from myClasses.randomStuff import *
from myClasses.apis import *
import random
from pprint import pformat
# Reading the token for authentication
token = open('./token.txt','r').read()
newBot = commands.Bot(command_prefix='.')

# Events
class Events(commands.Cog):
    def __init__(self,newBot):
        self.newBot = newBot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")

# When a new member joins the server
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} has joined the server. Cheers!')

# When a member leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member} left the server')


# Creating commands
# By default, the name of the function is the name that we will use to run the command
class Commands(commands.Cog):
    def __init__(self,newBot):
        self.newBot = newBot
    
    @commands.command()
    async def hi(self,ctx):
        await ctx.send(f'Hello')
    
# Making alias for a command
# @newBot.command(aliases=['comm1','comm2'])
# async def _someCommand()
    @commands.command
    async def quest(self,ctx,*,question):
        answer = random.choice(questResponses)
        await ctx.send(f'Question: {question}\nAnswer: {answer}')

    @commands.command()
    # Deleting messages
    async def clear(self,ctx,amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def joke(self,ctx,*,joke=''):
        jokeApi = Apis()
        jokeData = jokeApi.jokeApi(joke)
        jokeData=pformat(jokeData)
        await ctx.send(jokeData)
    
    @commands.command()
    async def search(self,ctx,*,ques):
        searchApi = Apis()
        ques = str(ques)
        ques = ques.replace(" ","")
        if ques=='':
            await ctx.send("Enter something to search")
        else:
            dat = searchApi.searchApi(ques)
            await ctx.send(dat)

# Running the bot.
newBot.add_cog(Events(newBot))
newBot.add_cog(Commands(newBot))
newBot.run(token);


