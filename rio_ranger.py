import random
import discord
from discord.ext import commands
from discord.utils import get
import os

TOKEN = ''

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = ('Рио, '), intents = intents)
bot.remove_command('help')

@bot.command()
async def привет(ctx):
    phrase_number = random.randint(1, 5)
    if phrase_number == 1:
        await ctx.send('...')
    if phrase_number == 2:
        await ctx.send('Я буду поддерживать вас на этом этаже! Наилучшие пооооожелания!')
    if phrase_number == 3:
        await ctx.send('Бооже, жуть.')
    if phrase_number == 4:
        await ctx.send('Я Наряжающаяся Кукла, Рио Рейнджер!')
    if phrase_number == 5:
        await ctx.send('Я... папин шедевр... Рио Рейнджер...')

@bot.command()
async def рулетка(ctx):
    n = random.randint(1, 6)
    kill = random.randint(1, 6)
    count = 0
    kill_rio = random.randint(1, 10)
    if n == kill or n == count or count == kill:
        await ctx.send('Неудачник, ты мёртв!')
        count = 0
    elif kill_rio == 4:
        await ctx.send('https://cdn.discordapp.com/attachments/918951122830491688/918956692690075668/ENac8EfXYAEea_2.png')
        await ctx.send('Не надо... Сафалин... Не надо... пожалуйста...!! Мне не нужно сердце... не сейчас...!! Я просто... должен умереть... но ты...!! Хватит...!! ХВААААААААТИТ...!! Аааххх... Меня захлёстывают... эти ненужные эмоции... Нет...!! Это не...!! Простите меня... просто...!!')
        await ctx.bot.logout()
    else:
        await ctx.send('Похоже, тебе повезло, какая жалость')
        count += 1
    if count == 8:
        count = 0

@bot.command()
async def быть(ctx, *, arg):
    n = random.randint(1, 4)
    if n == 1:
        await ctx.send('Тебе, придурок, не быть, конечно же.')
    if n == 2:
        await ctx.send('Ещё какие цитатки знаешь?')
    if n == 3:
        await ctx.send('А если и быть, то незачем.')
    if n == 4:
        await ctx.send('Кошмааар. Я не могу опьянеть, чтобы продолжить эту дискуссию.')

@bot.command()
async def хд(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/918951122830491688/919151640278351922/800936f5bd8e67dc.jpg')


@bot.command()
async def как(ctx, *, arg):
    if arg == 'тебе не стыдно':
        await ctx.send('А с чего бы вдруг должно быть?')
    else:
        await ctx.send('Уж всяко лучше твоего.')

@bot.command()
async def я(ctx, *, arg = None):
    if arg == None:
        j = random.randint(1, 3)
        if j == 1:
            await ctx.send('Головка от хуя')
        if j == 2:
            await ctx.send('Верёвка для белья')
        if j == 3:
            await ctx.send('Зелёная свинья')
    else:
        await ctx.send('Мне нет до этого дела.')

@bot.command()
async def где(ctx, *, arg):
    await ctx.send('Убийственная игра, третий этаж.')

@bot.command()
async def смысл(ctx, *, arg = None):
    if arg == 'жизни':
        n = random.randint(1, 5)
        if n == 1:
            await ctx.send('В том, чтобы слушать меня.')
        if n == 2:
            await ctx.send('Прежде чем об этом задумываться, докажи, что наверняка не умрёшь завтра.')
        if n == 3:
            await ctx.send('Ты совсем дурак?')
        if n == 4:
            await ctx.send('Боооже, отвали.')
        if n == 5:
            await ctx.send('Не бухай больше: моё терпение не вечно.')
    if arg == None:
        await ctx.send('Договаривай реплику либо заткнись.')

@bot.command()
async def расскажи(ctx, *, arg):
    if arg == 'о юттд':
        await ctx.send('Your Turn To Die -Смертельная Игра решением большинства- (Kimi ga Shine) бесплатная игра в жанре хоррор/приключения/переговоры, разработанная Nankidai и сделанная в RPG Maker MV')
    if arg == 'о себе':
        await ctx.send('Рио Рейнджер или Тото Ноэль (ト ト ・ ノ エ ル, Toto Noeru?), «Переодевающаяся Кукла», является Мастером третьего этажа в Смертельной Игре.')
    if arg == 'обо мне':
        await ctx.send('А тебя я знать не знаю')
    if arg == 'анекдот':
        joke = random.randint(1, 20)
        if joke == 1:
            await ctx.send('Люди, которые переходят на красный, вам так важно, чтобы в вашей смерти был виноват именно автомобилист?')
        if joke == 2:
            await ctx.send('Что бы я ни собирался делать, Гашу может рассказать такую же историю, в которой кто-то умер.')
        if joke == 3:
            await ctx.send('Игроки собираются сбежать. Инструктируют мастеров этажей:\n— Что бы ни случилось, делайте вид, что так и должно быть.\nПришли игроки к выходу, смотрят — вход завалило.\nГашу, посмотрев на часы:\n— Десять тридцать пять, точно по графику.')
        if joke == 4:
            await ctx.send('Кейджи, узнав, что цель кукол — убить:\n— Порублю, суки!\nКуклы испугались и скинулись по рублю.')
        if joke == 5:
            await ctx.send('Кью-таро рассказывает Гину про свои матчи:\n— Ну вот, бегу по полю, и тут ХУЯК, слева враги! ХУЯК! Справа враги!\nНао, бледнея:\n— Ты что такое говоришь? Это же ребёнок!\nКью-таро подскакивает:\n— Какой нахуй ребёнок?! Сборная Кореи, блять!')
        if joke == 6:
            await ctx.send('Джо: слушай, а чего там волхвы принесли новорождённому Иисусу?\nСара: даров\nДжо: привет!')
        if joke == 7:
            await ctx.send('Шин: мне не нравится, как вы игнорируете меня\nСара: ну так скажи, как игнорировать, чтобы тебе нравилось')
        if joke == 8:
            await ctx.send('Я тебе не клоун.')
        if joke == 9:
            await ctx.send('Майли: есть проблема, нужно решение\nСоу: у меня есть план\nМайли: он не должен привести к каким-либо странным последствиям\nСоу: у меня нет плана')
        if joke == 10:
            await ctx.send('Сара: Шин, ты заебал уже врать!\nШин: Я ключник.')
        if joke == 11:
            await ctx.send('Кейджи: сколько тебе лет?\nСоу: а сколько бы ты мне дал?\nКейджи: пожизненное')
        if joke == 12:
            await ctx.send('Приводит батя Сары Кая с женой знакомить:\n— это Кай, он будет нас защищать.\nОна спрашивает:\n— А где он жить будет?\nБатя Сары отвечает:\n— А он вообще жить не хочет.')
        if joke == 13:
            await ctx.send('Кейджи: простите, я потерял своего знакомого, Соу, на пляже. Можно я сделаю объявление?\nОхранник: конечно!\nКейджи, наклоняясь к микрофону: прощай, уёбок.')
        if joke == 14:
            await ctx.send('Сара: Кай так долго вечно сидит в своей комнате \nКейджи: он похож на депрессивного\nСара: режется значит\nКейджи: кое-что покруче\nСара: вскрывается')
        if joke == 15:
            await ctx.send('Гин ловил ртом капли с сосульки. Глупая и нелепая смерть.')
        if joke == 16:
            await ctx.send('Мишима: Ты кто?\nМайли: Твоя смерть.\nМишима: А почему в цветном платье, с рюшечками?\nМайли: Нелепая.')
        if joke == 17:
            await ctx.send('Реко: Есть здесь врач?!\nСафалин: Да, я патологоанатом.\nРеко: Мой брат умирает!\nСафалин: И уже скоро мы узнаём, какова причина смерти...')
        if joke == 18:
            await ctx.send('Гин, после яда: Доктор, я буду жить?\nСафалин: С вопросом, есть ли жизнь после смерти, пожалуйста, обращайтесь в церковь, а я врач.')
        if joke == 19:
            await ctx.send('Сара: можешь привести мне пример парадокса, одновременного грустного и смешного?\nДжо: клоун умер от скуки!')
        if joke == 20:
            await ctx.send('Шин признался друзьям в том, что они геи.')

@bot.command()
async def скучно(ctx):
    n = random.randint(1, 7)
    if n == 1:
        await ctx.send('Можем поиграть в русскую рулетку. Буду рад выстрелить в тебя!')
    if n == 2:
        await ctx.send('И что?')
    if n == 3:
        await ctx.send('Меня это не интересует.')
    if n == 4:
        await ctx.send('Можешь умереть: это точно исправит твоё состояние.')
    if n == 5:
        await ctx.send('Хуючно.')
    if n == 6:
        await ctx.send('Рассказать анекдот?')
    if n == 7:
        await ctx.send('Скука только для ведьм яд, тебе же ничего не будет.')

@bot.command()
async def тебя(ctx, *, arg):
    if arg == 'отменили в твиттере':
        await ctx.send('Плевать.')
    if arg == 'никто не любит':
        await ctx.send('Как и тебя.')

@bot.command()
async def что(ctx, *, arg):
    if arg == 'за игнор':
        n = random.randint(1, 3)
        if n == 1:
            await ctx.send('Ты меня раздражаешь.')
        if n == 2:
            await ctx.send('...')
        if n == 3:
            await ctx.send('Я не обязан тебе отвечать.')
    if arg == 'такое кабачок':
        n = random.randint(1, 4)
        if n == 1:
            await ctx.send('Тебя что, в гугле забанили?')
        if n == 2:
            await ctx.send('То, что вскоре окажется в твоей заднице.')
        if n == 3:
            await ctx.send('Овощ, употребление которого в некоторых случаях может вызвать спазмы в желудке и диарею.')
        if n == 4:
            await ctx.send('Говорят, девушки любят его использовать не по прямому назначеееению.')

@bot.command()
async def почему(ctx, *, arg):
    if arg == 'жить так сложно' or arg == 'так сложно жить':
        await ctx.send('Такова судьба жалких людей.')

@bot.command()
async def хах(ctx):
    await ctx.send('Хех?')

@bot.command()
async def ты(ctx, *, arg):
    if arg == 'дурак' or arg == 'дурак?':
        await ctx.send('В отличие от тебя, нет.')
    if arg == 'мёртв' or arg == 'мертв':
        await ctx.send('Я не уверен, мне тебя послать к окулисту или к психиатру?')

@bot.command()
async def стыдись(ctx):
    await ctx.send('Отказываюсь.')

@bot.command()
async def хочешь(ctx, *, arg):
    if arg == 'покачаться на качелях?':
        n = random.randint(1, 3)
        if n == 1:
            await ctx.send('Чего?')
        if n == 2:
            await ctx.send('Если ты потом покатаешься на члене.')
        if n == 3:
            await ctx.send('С тобой? Нет.')

@bot.command()
async def пиф(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/918951122830491688/918956692690075668/ENac8EfXYAEea_2.png')

@bot.command()
async def да(ctx):
    await ctx.send('Пизда.')

@bot.command()
async def смертельная(ctx, *, arg = None):
    if arg == 'игра':
        names = ['Рио', 'Нона', 'Мышка', 'Рей', 'Коробка', 'Ириз']
        cards = ['Ключник', 'Жертва', 'Мудрец', 'Житель', 'Житель', 'Житель']
        n = len(names)
        voted_for = random.randint(0, n - 1)
        sacrifise_runs_with = random.randint(0, n - 1)
        await ctx.send(f'Большинство проголосовали за {names[voted_for]}')
        await ctx.send(f'Раскрываю роли!')
        count = 0
        for i in range(n):
            k = random.randint(0, len(cards) - 1)
            await ctx.send(f'{names[count]} - {cards[k]}')
            if cards[k] == 'Жертва':
                sacrifice = count
            if cards[k] == 'Ключник':
                keymaster = count
            count += 1
            del cards[k]
        if names[voted_for] == names[sacrifice]:
            await ctx.send('Большинство проголосовали за Жертву.')
            if sacrifice != sacrifise_runs_with:
                await ctx.send(f'{names[sacrifice]} сбегает с {names[sacrifise_runs_with]}.')
            else:
                await ctx.send(f'{names[sacrifice]} сбегает.')
        if names[voted_for] == names[keymaster]:
            await ctx.send('Большинство проголосовали за Ключника. Умирают все!')
        if names[voted_for] != names[keymaster] and names[voted_for] != names[sacrifice]:
            await ctx.send('Вы сделали правильный выбор.')
            await ctx.send(f'Умирают {names[voted_for]} и Жертва - {names[sacrifice]}')
    if arg == None:
        await ctx.send('Иди просрись, придурок')

bot.run(TOKEN)