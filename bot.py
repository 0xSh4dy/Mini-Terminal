from discord.ext import commands,tasks
from lists import *
from discord import File
from myClasses.randomStuff import *
from myClasses.apis import *
import random
from pprint import pformat
from PIL import Image
from urllib.request import urlretrieve
import os
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
    @commands.command()
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

    @commands.command()
    async def weather(self,ctx,city):
        city = str(city)
        city = city.replace(" ","")
        if city == "":
            await ctx.send("Please enter the name of the city to check weather data")
        else:
            weatherData = Apis().weatherApi(city)
            await ctx.send(weatherData)

    @commands.command()
    async def movie(self,ctx,movie):
        movie = str(movie)
        movie = movie.replace(" ","")
        if movie == "":
            await ctx.send("Please enter the name of the movie")
        else:
            movieData = Apis().movieApi(movie)
            await ctx.send(movieData)

    @commands.command()
    async def image(self,ctx,image='random'):
        image = str(image)
        image = image.replace(" ","")
        
        if image == "":
            await ctx.send("Please enter the name of the image")
        else:    
            imageUrl = Apis().imageApi(image)
            if imageUrl=="No":
                await ctx.send("Image not found")
            else:
                urlretrieve(imageUrl,"image.jpg")
                with open('image.jpg','rb') as f:
                    picture = File(f)
                await ctx.send(file=picture)
                cwd = os.getcwd()
                os.remove(cwd+'/'+'image.jpg')         

class MusicCommands(commands.Cog):
    def __init__(self,newBot):
        self.newBot = newBot
    
    @commands.command(pass_context=True)
    async def join(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            await channel.connect()
            await ctx.send(f"Mini Terminal joined the channel {channel}")
        except(AttributeError):
            res = "You need to be connected to a voice channel in order to use this command"
            await ctx.send(res)

    @commands.command()
    async def leave(self,ctx):
        
        channel = ctx.message.author.voice.channel
        await ctx.send(ctx.message.author.voice.channel.disconnect())
        # except(AttributeError):
        #     res = "You need to be connected to a voice channel in order to use this command"
        #     await ctx.send(res)

# Running the bot.
newBot.add_cog(Events(newBot))
newBot.add_cog(Commands(newBot))
newBot.add_cog(MusicCommands(newBot))
newBot.run(token)


