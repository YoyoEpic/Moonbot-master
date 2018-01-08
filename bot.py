from discord.ext import commands
from random import randint
import checks
import re
import asyncio
import discord.utils
import discord.errors
import io
import datetime
import random
import os
import discord
import aiohttp
import time
import websockets
import json
import outlook
import steamapi

description = "The Most Racist Bot in Discord."
bot = commands.Bot(command_prefix=">", description=description)
Token = 'Mjk3OTQ5MDk3ODk2MzEyODMy.C8IOUQ.LVscXkQ8z8wVMPSUg8qZWbnsAJM'

wrap = "```py\n{}\n```"

mail = outlook.Outlook()

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Hello you filthy faggot nigger " + ctx.message.author.mention)


@bot.command(pass_context=True)
async def vape(ctx):
    await bot.say("I'll be real with you fucking faggots, I spent literally 20 fucking minutes looking for stupid offensive fag vape jokes. Only have 3.")
    await asyncio.sleep(1)
    await bot.say(random.choice(open('vape.txt').readlines()))


@bot.command(pass_context=True)
async def betterhelp(ctx):
    await bot.say("Check your DM's, you fucking faggot nigger.")
    await bot.whisper(open('helpmessage.txt', encoding='utf-8').read())


@bot.command(pass_context=True)
async def helpfun(ctx):
    await bot.whisper(open('helpfun.txt', encoding='utf-8').read())


@bot.command(pass_context=True)
async def helpmeme(ctx):
    await bot.whisper(open('helpmeme.txt', encoding='utf-8').read())


@bot.command(pass_context=True)
async def helpadmin(ctx):
    await bot.whisper(open('helpadmin.txt', encoding='utf-8').read())


@bot.command(pass_context=True)
async def helpother(ctx):
    await bot.whisper(open('helpother.txt', encoding='utf-8').read())
	
	
@bot.command(pass_context=True)
async def state(ctx):
    await bot.say(random.choice(open('state.txt').readlines()))	


@bot.command(pass_context=True)
async def say(ctx, *, message):
    await bot.say(message)
	
	
@bot.command(pass_context=True)
async def triggered(ctx):
	await bot.upload("triggered.gif")
	
	
@bot.command(pass_context=True)	
async def notifydev(ctx, message):
        if len(ctx.message.content) > 10:
            await bot.send_typing(ctx.message.channel)
            await bot.send_message(ctx.message.channel, "Nigger, sent to Master.")
            await bot.send_message(discord.User(id='140886965359738880'), "New message from `" + ctx.message.author.name + "` Discrim: `" + ctx.message.author.discriminator + "` ID: `" + ctx.message.author.id + "` Server Name: `" + ctx.message.author.server.name + "` Message: `" + ctx.message.content[len(">notifydev "):].strip() + "`")
        else:
            await bot.send_message(message.channel, "You'd need to put a message in this....")
			

@bot.command(pass_context=True)
@checks.is_owner()
async def msg(ctx, id, reason):
	await bot.send_message(discord.User(id=id), reason)			


@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("Faggot, here's the bot's link: https://discordapp.com/oauth2/authorize?&client_id=189840216058626048&scope=bot&permissions=268626999")


@bot.command(pass_context=True)
async def niggers(ctx):
    await bot.say("I fucking hate niggers like you, you shitty worthless cum stain. I hope they tie ropes by your limbs and make horses literally tear your limbs off.  " + ctx.message.author.mention)


@bot.command(pass_context=True)
async def ilikeyou(ctx):
    await bot.say("☜(ﾟヮﾟ☜) Thanks, I like myself too, but hate nignogs like you!")

	
@bot.command(pass_context=True)
async def retarded(ctx):
	await bot.upload("retardedmeme.PNG")
	

@bot.command(pass_context=True)
async def yiff(ctx):
    await bot.upload('kek.png')


@bot.command(pass_context=True)
async def shitpost(ctx):
    await bot.say(random.choice(open('shitpost.txt', encoding='utf-8').readlines()))


@bot.command(pass_context=True)
async def insult(ctx):
    await bot.say(random.choice(open('insult.txt').readlines()))
	
	
@bot.command(pass_context=True)
async def dramaalert(ctx, *, message):
	await bot.say("Hello DramaAlert nation. I'm your host, Killer Keemstar. Let's get roooooooiiiiight into the news! Our first story today: {}. And that's it for the news, if you like DramaAlert, slap a like on the like button. Let's shoot for 2 likes, DramaAlert Nation now over 1 million, 446 thousand subscribers!".format(message))
	await asyncio.sleep(3)
	await bot.say("fucking niggers.")


@bot.command(pass_context=True)
async def roast(ctx, *users: discord.User):
    for user in users:
        await bot.say((random.choice(open('roast.txt').readlines())) + str(user.mention))


@bot.command(pass_context=True)
async def pressf(ctx):
    await bot.say(ctx.message.author.name + " has paid their respects.")
    await bot.say("Respects paid: " + str(randint(0, 1000)))
	
	
@bot.command(pass_context=True)	
@checks.is_owner()	
async def join(ctx, *, message):
    try:
        inv = await bot.get_invite(ctx.message.content[6:])
        try:
            await bot.accept_invite(inv)
            await bot.say("Hello, I'm a bot! I was added to this server.")
            await bot.say("Successfully joined the invite `" + message.content[6:] + "`!")
        except:                                    
            await bot.say("Couldn't join, sorry!")
    except Forbidden:
        pass	


@bot.command(pass_context=True)
async def furries3(ctx):
	await bot.say("Hi, yeah. As a precaution, I'm going to have to do this in order to not be banned by Discord or the bot being taken offline. For 99% of people, this doesn't apply, but still read. If you think you will be triggered by the content I am about to show you, refer to this: >disclaimer. Disclaimer has been updated, be sure to check it out.")
	await bot.say("If you read the disclaimer, and you still want to keep going, you can do >whynot. If not, you can still use the bot.")


@bot.command(pass_context=True)
async def whynot(ctx):
	await bot.say("I think I'm done. Too much cancer. I mean, seriously, how much fucking cancer do they think is good enough? I try to live cancer free, but now I think Hitler really wasn't wrong. I mean, he just targeted the wrong demographic. Let me prove it.")
	await bot.upload("kill.png")
	await bot.say("If you want to really know why we all hate furries, it's mostly for this reason right here. Not only is the art fucking cancer, but the guy crosses out dad. I mean, how much of a fag do you have to believe that a WORK OF CANCER IS YOUR FUCKING DREAM DAD. These people, I swear, aren't sane at all. I mean, for god's sakes, who pays for these images? Who in their right mind would pay out the ass for these fucking images.")
	await asyncio.sleep(5)
	await bot.upload("yourself.png")
	await bot.say("These OC's. There's nothing more retarded than actually talking about what your dick or whatever looks like. I mean, ffs, how much cancer can you fit in a fucking bio until it becomes a meme. Seriously. I actually wonder why you would put fucking thought in that whole thing. It's not fucking real. It's about as real as your girlfriend. I also don't remember s hermaphrodite being a gender. At all. There's only two genders, and you are fucking wrong if you think there's more. There isn't. At. Fucking. All.")
	await asyncio.sleep(5)
	await bot.upload("oboi.png")
	await bot.say("My fucking god. I have never seen anything worse in my life. Generally. This takes ovarian cancer times 200. It can't be unfucking seen. This is trash. Where is fucking Hitler when you need him? I swear, you prove to me that Hitler didn't target the wrong demographic and I will shoot you. No fucking doubt. What so fucking ever.")
	await asyncio.sleep(5)
	await bot.upload("same.png")
	await bot.say("Pretty much my thoughts, right now. I think I'm done with these commands. I think I'm retiring. There's nothing fucking sacred anymore. Everything has been tainted by furfags, I don't know how to deal with it.")
	await bot.upload("done.png")
	await bot.say("Yup. Done. They ruined the nazi party. Awesome. I'm quitting.")
	await bot.upload("wakemeup.png")
	
	
@bot.command(pass_context=True)
async def furries2(ctx):
	await bot.say("Hi, yeah. As a precaution, I'm going to have to do this in order to not be banned by Discord or the bot being taken offline. For 99% of people, this doesn't apply, but still read. If you think you will be triggered by the content I am about to show you, refer to this: >disclaimer. Disclaimer has been updated, be sure to check it out.")
	await bot.say("If you read the disclaimer, and you still want to keep going, you can do >keepgoing. If not, you can still use the bot.")

	
@bot.command(hidden=True, pass_context=True)
async def disclaimer(ctx):
	await bot.whisper("This bot is an extremely racist and offensive. I have said that in my help menus where you can get the commands. This disclaimer is basically where I say you are going to look at content thats gonna be triggering. So, if you don't want to look at the content, skip over the command and do something else. If you still want to see the content, you have been warned. I have purposefully censored the images, and done everything in my power to not trigger you or someone else. You have been warned. Also Maxie has given his permission to post the following images. (Because in the end, he thinks its cancer, too) If you think you are going to find yourself in the content, do **NOT** use the commands. I will not be responsible for any bad shit.")

	
@bot.command(hidden=True, pass_context=True)
async def keepgoing(ctx):
	await bot.say("Oh god, back it again. >furries wasn't just the cancer on a St. Jude's research patient, it's now gone beyond that realm. This is now the cancer of the extreme. These *things* have to be stopped. They have to.")
	await bot.upload("fuckingwhy.png")
	await bot.say("The cancer just flows here. It's so fucking disgusting to where I can't even question why people like this type of shit. Seriously, who talks about having a big enough dick where you can pass out. Seriously, no other words.")
	await asyncio.sleep(5)
	await bot.upload("whatare.png")
	await bot.say("You see, why do I go through this hell to bring you all content that's supposed to laugh at this shit. I'm literally done with these furry commands. Like honestly. I think all the males are fucking gay in the fandom. There's no other way. WHO WOULD MAKE THIS TYPE OF FUCKING CONTENT? WHO ENJOYS THIS?")
	await asyncio.sleep(5)
	await bot.upload("you.png")
	await bot.say("My fucking god, this only keeps proving my point. Most guys in the cancer ass fandom are fucking gay. Who makes a character that has a *blue icy cold transparent cock*. To be honest, I bet their parents are so dissapointed in them. I am, and I am not even a parent.")
	await asyncio.sleep(5)
	await bot.upload("fucking.png")
	await bot.say("These censor bars don't do justice. I mean. For god's sake, it's like god fucking abandoned them at childhood. Who makes these pictures? It's so bad. If only I could upload the uncensored versions. You would understand.")
	await asyncio.sleep(5)
	await bot.upload("hi.png")
	await bot.say("This one is the worst one. Not even fucking funny. Seriously, I could not find anything else on dickface here, but I found this.")
	await asyncio.sleep(5)
	await bot.upload("gay.png")
	await bot.say("Why. Just why. Not even worth my fucking time.")

	
@bot.command(pass_context=True)
async def data(ctx, *users: discord.User):
    for user in users:
        await bot.say("Userdata for {}: \nUsername: {} \nUser ID: {} \nUser Avatar Hash: {} \nURL for User Avatar: {} \nUser Account Created At: {} \nAll this just for one nigger. Wow. You need a life. Or some rope.".format(user, user.name, user.id, user.avatar, user.avatar_url, user.created_at))


@bot.command(hidden=True, pass_context=True)
@checks.is_owner()
async def test2(ctx):
		inv1 = list(bot.servers)[69]
		inv2 = await bot.create_invite(inv1)
		await bot.say(inv2)
		
		
@bot.command(hidden=True, pass_context=True)
@checks.is_owner()
async def hax(ctx, *, message):
        hax = await bot.create_invite(discord.utils.find(lambda m: m.name == message, bot.servers))
        await bot.say(hax)		

		
@bot.command(pass_context=True)
@checks.is_owner()
async def steamuser(ctx, *, message):
	try:
		steamapi.core.APIConnection(api_key="2C1CAF7902437510D866D0B0F0D1C8CE")
		top = steamapi.user.SteamUser(message)
		await bot.say(top)
	except discord.ext.commands.errors.MissingRequiredArgument:
		await bot.say("Nigger, you forgot your fucking Steam64ID. Maybe next time, read >betterhelp faggot.")
		
		
@bot.event
async def on_message(ctx):
    if ctx.message.server.id == "110373943822540800" and ctx.message.channel.name == "ultimate-shitposting" or "testing-nsfw":
        await bot.process_commands(ctx)
    else:
        return


@bot.command(pass_context=True)
async def dlotto(ctx):
    await bot.say("Welcome to DiscordLotto! Gamble your skins and soundpacks here! Free 50 cents when you use code: 'banb1nzy'! To start gambling, use either >gamblesound or >gambleskins")


@bot.command(pass_context=True)
async def gambleskins(ctx):
    await bot.say("Putting skins in now.")
    await asyncio.sleep(5)
    await bot.say("Flipping coin...")
    rr_bullet = randint(1, 6)
    rr_count = 1
    if rr_bullet == rr_count:
	    await bot.say("YOU JUST WON THESE SKINS! " + random.choice(open("skins.txt").readlines()))
	    rr_bullet = randint(1, 6)
	    rr_count = 1
    else:
	    await bot.say("You lost your skins. Don't worry though, you still have more.")
	    rr_count = rr_count + 1

		
@bot.command(pass_context=True)
async def furries(ctx):
	await bot.say("Hi, yeah. As a precaution, I'm going to have to do this in order to not be banned by Discord or the bot being taken offline. For 99% of people, this doesn't apply, but still read. If you think you will be triggered by the content I am about to show you, refer to this: >disclaimer.")
	await bot.say("If you read the disclaimer, and you still want to keep going, you can do >showme. If not, you can still use the bot.")

	
@bot.command(hidden=True, pass_context=True)
async def showme(ctx):
    await bot.say("Furries are the most cancerous things known to mankind. They are like a worst form of a nigger. No one fucking likes them, and they have no fucking friends. They wonder why they get hate, but they don't realize half the shit they do, NO ONE ELSE DOES.")
    await bot.upload("wtf.png")
    await bot.say("I'm going to let your look at that picture and let you decide what's wrong with it.")
    await asyncio.sleep(5)
    await bot.say("Another reason: They don't realize that most normal people don't want to hear the kinks they have. But Ohhhhhhh boi, they make complete fucking sure you know what they have. No one should be forced to listen to other's fetishes. I am not posting a picture for your sake.")
    asyncio.sleep(5)
    await bot.say("It wouldn't be so bad, but I mean, seriously, look at this bio.")
    await bot.upload("wtf2.png")
    await bot.say("You see what I fucking mean? 'Two Cat Parents'. Okkkkay whatever suits you. Knot size. oh god, DO NOT LOOK WHAT IT MEANS. YOU REGRET LIFE CHOICES.")
    await asyncio.sleep(10)
    await bot.say("You noticed I was gone for a bit longer, I just did a round of bleach. And here's another reason why furries are cancer: http://www.experienceproject.com/question-answer/What-Breed-Of-K9-Has-The-Best-Looking-Cock-And-Knot-My-Girl-Wants-To-Know/2238281 <---- not for the faint of heart. Don't do this for a gain.")
	
		

@bot.command(pass_context=True)
async def gamblesound(ctx):
    await bot.say("Putting soundpacks in now.")
    await asyncio.sleep(5)
    await bot.say("Flipping coin...")
    rr_bullet = randint(1, 6)
    rr_count = 1
    if rr_bullet == rr_count:
	    await bot.say("YOU JUST WON THESE SOUNDPACKS " + random.choice(open("sounds.txt").readlines()))
	    rr_bullet = randint(1, 6)
	    rr_count = 1
    else:
	    await bot.say("You lost your sounds, but don't worry, you have more.")
	    rr_count = rr_count + 1


@bot.command(pass_context=True)
async def updates(ctx):
    await bot.say(open("update.txt", encoding='utf-8').read())


@bot.command(pass_context=True)
async def offensive(ctx):
    await bot.say(random.choice(open('racist.txt', encoding='utf-8').readlines()))


@bot.command(pass_context=True)
async def _8ball(ctx):
    await bot.say(random.choice(open('balls.txt').readlines()))


@bot.command(pass_context=True)
async def rule34(ctx):
    await bot.say("Seriously. No one in your chat probably wants to see cancer porn like you. End your nigger life right now, nignog.")


@bot.command(pass_context=True)
async def e621(ctx):
    await bot.say("Did you not pay attention to fucking >rule34? You fucking yiffer, I don't want your dragon x dog porn on here. Get another bot fag.")


@bot.command(pass_context=True)
async def devserver(ctx):
    await bot.whisper("Nigger, here's the invite. https://discord.gg/012PB9UgbBXgvQ2GZ")


@bot.event
async def on_message(ctx, messages:int):
    if ctx.message.server.id == "173190262271508480" and ctx.message.content == "kys" "bitch" "cunt" "fag" "furfag" "faggot" "fuck you":
        await bot.purge_from(ctx.message.channel, limit=messages + 1)


@bot.command(pass_context=True)
async def rr(ctx):
    rr_bullet = randint(1, 6)
    rr_count = 1
    if rr_bullet == rr_count:
	    await bot.say(ctx.message.author.mention + ' This nigger just died.')
	    rr_bullet = randint(1, 6)
	    rr_count = 1
    else:
	    await bot.say('Nigger, you lived...for now.')
	    rr_count = rr_count + 1


@bot.command(pass_context=True)
async def ver(ctx):
    await bot.say("Current bot version number: v2.6. Codename: ""Moon Man Moon Man can't you see?""")


@bot.command(pass_context=True)
async def id(ctx):
    await bot.say("Nigger, here's your ID: " + ctx.message.author.id)
	
	
@bot.command(pass_context=True)	
@checks.is_owner()
async def newemail(ctx):
	mail.login('mrsamiman@hotmail.com', 'samialtamimi000')
	mail.inbox()
	await bot.whisper(mail.unread())



@bot.command(pass_context=True)
async def discrim(ctx):
    await bot.say(
        "Are you really that retarded that you can't see your discrim? Here it is fag: #" + ctx.message.author.discriminator)


@bot.event
async def on_server_join(ctx):
	await bot.send_message(ctx.message.channel, "Thanks for inviting me to your server. To get started in the world of racism and memes: use >betterhelp. If you think you can handle a big list of commands, use: >help.")
		
		
@bot.command(pass_context=True)
async def spiderman(ctx):
    spidey = ['spiderman1.jpg',
              'spiderman2.jpg',
              'spiderman3.jpg',
              'spiderman4.jpg',
              'spiderman5.jpg',
              'spiderman6.jpg',
              'spiderman7.jpg',
              'spiderman8.jpg',
              'spiderman9.jpg',
              'spiderman10.jpg',
              'spiderman11.jpg',
              'spiderman12.jpg',
              'spiderman13.jpg',
              'spiderman14.jpg',
              'spiderman15.jpg',
              'spiderman16.jpg',
              'spiderman17.jpg',
              'spiderman18.jpg',
              'spiderman19.jpg',
              'spiderman20.jpg',
              'spiderman21.jpg',
              'spiderman22.jpg',
              'spiderman24.jpg',
              'spiderman26.jpg',
              'spiderman27.jpg',
              'spiderman28.png',
              'spiderman29.jpg',
              'spiderman30.jpg',
              'spiderman31.jpg',
              'spiderman32.jpg',
              'spiderman33.png',
              'spiderman34.png',
              'spiderman35.jpg',
              'spiderman36.png',
              'spiderman37.jpg', ]
    await bot.upload(random.choice(spidey))


@bot.command(pass_context=True)
async def discourse(ctx):
    await bot.say("Don't let that weight to go your ass because you got fed the discourse nigger nogger toilet clogger")
    await bot.upload("discourse.png")

	
@bot.command(pass_context=True)
async def nsfw(ctx):
	await bot.say("You want some nsfw? You know what? Fuck you faggot.")
	
	
@bot.command(pass_context=True)
async def safe(ctx):
	await bot.say("There's nothing about this bot that's safe faggot.")
	

@bot.command(pass_context=True)
async def songs(ctx):
    await bot.say("All of these links are the albums except for a couple. Enjoy. :wink:")
    await bot.say(random.choice(open('songs.txt').readlines()))


@bot.command(pass_context=True)
async def bullshit(ctx):
    await bot.say("Love getting my bot kicked for doing literally nothing but being racist, what a great punishment. I realize I didn't register the bot, that's my fault, but don't kick a bot that's supposed to *racist* in a NON-PG server.")
    await bot.upload("really.png")
    await asyncio.sleep(5)
    await bot.say("It doesn't even say in the rules that any form of racism isn't allowed. WOW. I'm *assuming* that information is the rules.")
    await bot.upload("why.jpeg")
    await asyncio.sleep(5)
    await bot.say("I even thought that it would say more in Best Practices, but NOPE. Nothing. I literally got my bot kicked because of *triggering* or *offensive slang*. Seriously? It's not a PG server, if it is, there should be a tag, but it's not. So, I just got kicked for using my free speech card.")
    await bot.upload("where.png")


@bot.command(pass_context=True)
async def triple(ctx):
    await bot.say('https://www.youtube.com/watch?v=OQj2L5Zuv9Y')


@bot.command(pass_context=True)
async def _420(ctx):
    await bot.upload("420.gif")


@bot.command(pass_context=True)
async def retard(ctx):
	await bot.say("This is the type of retarded people that straight need to die.")
	await bot.upload("re.png")
	await bot.say("Maybe he is right. Maybe it's just body hair. Not like it could fucking fur.")
	await bot.upload("tard.png")
	await bot.say("You know, if you going to at least try to defend your cancerous fandom, at least don't be retarded enough to do that.")


@bot.command(pass_context=True)
async def blazeit(ctx):
    await bot.upload("blazeit.gif")


@bot.command(pass_context=True)
async def jews(ctx):
    await bot.say(random.choice(open("jews.txt").readlines()))


@bot.command(pass_context=True)
async def alex(ctx):
    await bot.say("Type in the chat: Alex is a stupid nigger.")
    await bot.send_typing(ctx.message.server)
    await asyncio.sleep(2)
    await bot.say("Alex is a stupid nigger")


@bot.command(pass_context=True)
async def stats(ctx):
    await bot.say("MoonBot's Official Stats. Brought to you by the 10,000 whipped niggers who died for my clothes. \n"  "Servers MoonBot is on: {} \n"  "Users in Servers with MoonBot: {} \n"  "Number of Messages MoonBot has sent: {}\n"  "Channels MoonBot is in: {}\n"  "Private Channels MoonBot is in: {}".format(str(len(bot.servers)), str(len(set(bot.get_all_members()))), str(len(set(bot.messages))), str(len(set(bot.get_all_channels()))), str(len(set(bot.private_channels)))))


@bot.command(pass_context=True)
async def fuckthefans(ctx):
    await bot.say("I am in this for the money. That's all I care about is your money. Alright, I don't do it to entertain people, That's just a fuckin' scam. I really hope you die of cancer, I hate every single one of you. FUCK THE FANS")


@bot.command(hidden=True, pass_context=True)
async def faggotmuncher(ctx):
    await bot.whisper("you are such a fucking faggot. what a fag. take this code tho and pm Master :wink: Code:198admoqnodam01. Join the dev server using >devserver and pm Master for something, i dont fucking know.")


@bot.command(pass_context=True)
async def kappa(ctx):
    await bot.say(open('kappa.txt', encoding='utf-8').read())


@bot.command(pass_context=True)
async def hitler(ctx):
    await bot.upload("hitler.gif")


@bot.command(pass_context=True)
async def waw(ctx):
    await bot.upload("waw.gif")


@bot.event
async def on_message():
    if message.author.id == "117678528220233731":
        await bot.send_message(message.channel, "Yes. From Denamrk. You fucking furfag.")
    else:
        return


@bot.command(pass_context=True)
async def fagit(ctx):
    await bot.upload("y.png")
    await bot.say("Alright, you fucking fag. Let me say something. Your name is probably the worst username I have heard. Seriously, Nico? What kind of shit name is that? It's like you are from an illegal mexican family. And Demius? That literally sounds so gay, it was shot up in Orlando. And X? What are we? Some edgy xbox player? Keep choking on your doritos and mountain dew. And what is with that avatar? I expect a wide arrange of people using my bot, but not fucking bronies. Seriously, get fucking cancer. I hope you grow tumors on your nuts and have them removed.")


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    await bot.process_commands(msg)


@bot.command(pass_context=True)
async def wtf(ctx):
    await bot.upload("fgt.png")
    await bot.say("Let me get this straight: you are in a fucking server where you are supposed to help people, but yet, you freak the fuck out about my question about what you said? Seriously. Get some fucking help.")


@bot.command(pass_context=True)
async def gaben(ctx):
    await bot.say("Nigger, praise your lord and savior, Gaben!")
    await bot.upload("gaben.jpg")


@bot.command(pass_context=True)
async def aw(ctx):
    if ctx.message.author.id == "163521874872107009":
        await bot.upload("luv.png")
    else:
        return


@bot.command(pass_context=True)
async def kys(ctx):
    if ctx.message.author.id == "102960079963164672":
        await bot.say("Kill yourself, faggot.")
    else:
        return


@bot.command(pass_context=True)
async def rekt(ctx):
    await bot.upload("rekt.gif")


@bot.command(pass_context=True)
async def feminazi(ctx):
    await bot.say("There is 39 things wrong with this video. For one thing, they are more racist than me. That's a problem. The other thing is they think black lives matter. What fags. I would shoot these niggers before I would shoot an actual nigger.")
    await bot.say("https://www.youtube.com/watch?v=qUmwyJEH_pE")


@bot.command(pass_context=True)
async def tfw(ctx):
    await bot.say("No one cares about your fucking feelings you faggot. Grow a pair or grow the fuck up.")


@bot.command(pass_context=True)
async def spic(ctx):
    await bot.say(random.choice(open("spic.txt").readlines()))


@bot.command(pass_context=True)
async def yay(ctx):
    await bot.upload("yay.gif")


@bot.command(pass_context=True)
async def talkshit(ctx):
    await bot.upload("talkshit.jpg")


@bot.command(pass_context=True)
async def lenny(ctx):
    await bot.say(random.choice(open('lenny.txt', encoding='utf-8').readlines()))


@bot.command(pass_context=True)
async def fursecute(ctx, mentions):
    fursona = ctx.message.content[len(">fursecute " + mentions):].strip()
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel, "Uh-oh! Nigger alert! Nigger alert, class!")
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel,
                           mentions + ", do you really believe you're a " + fursona + ", bubblehead?!")
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel, "Come on you, you're going to have to sit in the nigger noose.")


@bot.command(pass_context=True)
async def rip(ctx):
    await bot.upload("rip.png")


@bot.command(pass_context=True)
async def sexually(ctx):
    await bot.say(random.choice(open('identify.txt', encoding='utf-8').readlines()))


@bot.command(pass_context=True)
async def ping(ctx):
    pingtime = time.time()
    pingmsg = await bot.send_message(ctx.message.channel, "Pinging...")
    ping = time.time() - pingtime
    await bot.edit_message(pingmsg, "Took {}ms to ping. Nigger. ".format(ping))


@bot.command(pass_context=True)
async def makeinvite(ctx):
    await bot.say("Really? You can't fucking make your *own* invite? You're helpless. Here's your invite.")
    inv = await bot.create_invite(ctx.message.server)
    await bot.say(inv)


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def changenickname(ctx, nickname, *users: discord.User):
    for user in users:
        await bot.change_nickname(user, nickname)
        await bot.say("I changed `{}` to `{}`".format(user, nickname))
        await asyncio.sleep(.21)


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def getallbans(ctx):
    server = ctx.message.server
    bans = await bot.get_bans(server)
    if len(bans) == 0:
        await bot.say("No bans m8. Who's the nigger that's gonna be next? >:D")
    else:
        await bot.say("The bans on this server are: " + ", ".join(map(str, bans)))


@bot.command(pass_context=True)
@checks.is_owner()
async def setgame(ctx, Game):
    Game = ctx.message.content[len("setgame "):].strip()
    await bot.change_status(discord.Game(name=Game))
    await bot.say("Now playing: {}".format(Game))


@bot.command(hidden=True, pass_context=True)
@checks.is_owner()
async def debug(ctx, *, code: str):
    """Evaluates code."""
    result = eval(code)
    if code.lower().startswith("print"):
        result
    elif asyncio.iscoroutine(result):
        await result
    else:
        await bot.say(wrap.format(result))


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def addrole(ctx, roles: discord.Role, member: discord.User):
    try:
        await bot.add_roles(member, roles)
        await bot.say('Role successfully added!')
    except discord.HTTPException:
        await bot.say('Role not added. Maybe you dont have the permission?')


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def removerole(ctx, roles: discord.Role, user: discord.User):
    try:
        await bot.remove_roles(user, roles)
        await bot.say('Role successfully removed!')
    except discord.HTTPException:
        await bot.say("Role not removed. Maybe you don't have the permission?")


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def kick(ctx, member: discord.User):
    try:
        await bot.kick(member)
        await bot.say('Ayylmao. Nigga got kicked.')
    except discord.HTTPException:
        await bot.say("I dunno, maybe you don't have the perms to do this?")


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def oppress(ctx, *users: discord.User):
    try:
        for user in users:
            allow, deny = ctx.message.channel.overwrites_for(user)
            deny.send_messages = True
            await bot.edit_channel_permissions(ctx.message.channel, user, allow=allow, deny=deny)
            await bot.say("{} cannot speak. It must have bit his tongue out. ;)".format(user))
    except discord.HTTPException:
        await bot.say("Check your hierarchy and see if you have the roles, nigger.")


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def unmute(ctx, *users: discord.User):
    for user in users:
        allow, deny = ctx.message.channel.overwrites_for(user)
        allow.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, user, allow=allow, deny=deny)
        await bot.say("{} can speak. PRAISE THE NIGGER LORD!".format(user))


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def prune(ctx, messages: int):  # stolen from ehj2
    await bot.purge_from(ctx.message.channel, limit=messages + 1)
    removed = messages + 1
    x = await bot.say('These nigger messages got rekt: {}'.format(removed))
    await asyncio.sleep(5)
    await bot.delete_message(x)


@bot.command(pass_context=True)
@checks.admin_or_perm(manage_server=True)
async def ban(ctx, *users: discord.User):
    for user in users:
        try:
            await bot.ban(user, delete_message_days=7)
            await bot.say(user.name + " was rekterino from the server.")
        except discord.HTTPException:
            await bot.say(
                "Ban failed, nigger. Maybe you were trying to ban yourself or someone higher on the role chart?")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')


bot.run(Token)
