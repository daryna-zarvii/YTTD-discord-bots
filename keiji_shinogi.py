import random
import discord
from discord.ext import commands
from discord.utils import get
import os
import regex as re

TOKEN = ''

deleted = 0

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = 'Кейджи, ', intents = intents)
bot.remove_command('help')

uncensored = ['блять', 'хуй', 'пизда', 'пиздец', 'нахуй', 'в пизду', 'ебать', 'охуеть']

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        greeting = re.search(r'(П|п)(Р|р)(И|и)(В|в)(Е|е)*(Т|т)', ctx.content)
        mention = re.search(r'(К|к)+(Е|е)*(Й|й|ц|Ц)*(Д|д)*(Ж|ж)*(И|и)+', ctx.content)
        how_are_you_doing = re.search(r'(К|к)*(А|а)*(К|к) (Т|т)*(В|в)*(О|о)*(И|и)* (Д|д)(Е|е)*(Л|л)(А|а)', ctx.content)
        sara_mentioned = re.search(r'(С|с)(А|а)*(Р|р)(А|а|Ы|ы|У|у|Е|е)', ctx.content)
        shut_up = re.search(r'(З|з)(А|а)(Т|т)(К|к)(Н|н)(И|и)*(С|с)(Ь|ь|Б|б)*', ctx.content)
    else:
        greeting = None
        mention = None
        how_are_you_doing = None
        sara_mentioned = None
        shut_up = None

    if 'Кейджи, ' in ctx.content:
        greeting = None
        mention = None
        how_are_you_doing = None
        sara_mentioned = None
        shut_up = None
        
    if mention != None and greeting == None and shut_up == None:
        m = random.randint(1, 4)
        if m == 1:
            await ctx.reply('Требуется помощь мистера Полицейского?')
        if m == 2:
            await ctx.reply(f'Что-то случилось, {ctx.author.display_name}?')
        if m == 3:
            await ctx.reply(f'Хочешь поговорить, {ctx.author.display_name}?')
        if m == 4:
            await ctx.reply(f'Я слушаю, {ctx.author.display_name}')

        if str(ctx.author) == 'eeriez#4985':
            n = random.randint(0, 9)
            if n == 8:
                await ctx.reply('Дружелюбный Полицейский всегда на твоей стороне')


    if mention != None and greeting != None and shut_up == None:
        m = random.randint(1, 2)
        if m == 1:
            await ctx.reply('Здравствуй')
        if m == 2:
            await ctx.reply(f'Как поживаешь, {ctx.author.display_name}?')
        
        if str(ctx.author) == 'Мышка#2112':
            h = random.randint(0, 9)
            if h == 4:
                await ctx.reply('А между делом кажется тебе давно не напоминали, что ты миленькая')


    if mention != None and how_are_you_doing != None and shut_up == None:
        m = random.randint(0, 2)
        if m == 0 or m == 2:
            await ctx.reply('У Мистера Полицейского всё прекрасно, но я с радостью послушал бы о твоей жизни')
        if m == 1:
            await ctx.reply('Не отказался бы сейчас от жаркого, в остальном неплохо')

    if mention != None and greeting == None and shut_up != None:
        if str(ctx.author) != 'k0r0bka#8264' and str(ctx.author) != 'pipirip#7020':
            await ctx.reply('Ладушки')
        else:
            await ctx.reply('Вот уж не ожидал таких грубостей')

    if sara_mentioned != None:
        await ctx.reply('Вы знакомы с Сарой?')

    for i in range(len(uncensored)):
        if uncensored[i] in ctx.content:
            b = random.randint(1, 20)
            if b == 3:
                await ctx.reply('Что вызвало такие бурные эмоции?')


bot.run(TOKEN)
