from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import time

time.sleep(10)

#EnigmaRobotic part
file_Enigma = open('EnigmaRobotic.json', 'r')
Enigma = json.load(file_Enigma)
url = "https://discord.com/api/webhooks/835667618966274049/AdZHPUdOjGSjouemEOD_-0XLLz3w3UfktuzMMpneWh_VlwYlCd73hAQoYs6hxQoy35tO"

#cmd_root part
file_cmd_root = open('cmd_root.json', 'r')
cmd_root = json.load(file_cmd_root)

#7MSe1523NJtYp6j.json part
file_7MSe1523NJtYp = open('A7MSe1523NJtYp6j', 'r')
7MSe1523NJtYp = json.load(file_7MSe1523NJtYp)

#vision_aio.json part
file_vision_aio = open('vision_aio.json', 'r')
vision_aio = json.load(file_vision_aio)

#NurikAIO part
file_NurikAIO = open('NurikAIO.json', 'r')
NurikAIO = json.load(file_NurikAIO)

#NoraCop part
file_NoraCop = open('NoraCop.json', 'r')
NoraCop = json.load(file_NoraCop)


if os.path.getsize('EnigmaRobotic.json') > 0:
	webhook = DiscordWebhook(url=url, content="@"+Enigma["username"]+" just tweeted!  " + Enigma["link"])
	embed = DiscordEmbed( description=Enigma["tweet"], color='03b2f8')
	embed.set_author(name= "@"+Enigma["name"], url='https://twitter.com/EnigmaSuccess', icon_url='https://pbs.twimg.com/profile_images/1330265623704834049/popnuvDa_400x400.jpg')
	embed.set_image(url=Enigma["photos"])

	embed.set_footer(text='From Twitter', icon_url="https://support.content.office.net/en-us/media/0da17e2a-9ed5-496a-b161-9fd4491ce5c7.png")
	embed.set_timestamp()
	webhook.add_embed(embed)
	response = webhook.execute()
else:
	pass

if os.path.getsize('cmd_root') > 0:
	webhook = DiscordWebhook(url=url, content="@"+cmd_root["username"]+" just tweeted!  " + cmd_root["link"])
	embed = DiscordEmbed( description=cmd_root["tweet"], color='03b2f8')
	embed.set_author(name= "@"+cmd_root["name"], url='https://twitter.com/cmd_root', icon_url='https://pbs.twimg.com/profile_images/1242504658503045125/Hp9gJa6e_400x400.jpg')
	embed.set_image(url=cmd_root["photos"])

	embed.set_footer(text='From Twitter', icon_url="https://support.content.office.net/en-us/media/0da17e2a-9ed5-496a-b161-9fd4491ce5c7.png")
	embed.set_timestamp()
	webhook.add_embed(embed)
	response = webhook.execute()		
else:
	pass

if os.path.getsize('A7MSe1523NJtYp6j.json')	> 0 :
	webhook = DiscordWebhook(url=url, content="@"+7MSe1523NJtYp["username"]+" just tweeted!  " + 7MSe1523NJtYp["link"])
	embed = DiscordEmbed( description=7MSe1523NJtYp["tweet"], color='03b2f8')
	embed.set_author(name= "@"+7MSe1523NJtYp["name"], url='https://twitter.com/7MSe1523NJtYp6j', icon_url='https://abs.twimg.com/sticky/default_profile_images/default_profile_400x400.png')
	embed.set_image(url=7MSe1523NJtYp["photos"])

	embed.set_footer(text='From Twitter', icon_url="https://support.content.office.net/en-us/media/0da17e2a-9ed5-496a-b161-9fd4491ce5c7.png")
	embed.set_timestamp()
	webhook.add_embed(embed)
	response = webhook.execute()
else:
	pass

if os.path.getsize('vision_aio.json') > 0:
	webhook = DiscordWebhook(url=url, content="@"+vision_aio["username"]+" just tweeted!  " + vision_aio["link"])
	embed = DiscordEmbed( description=vision_aio["tweet"], color='03b2f8')
	embed.set_author(name= "@"+vision_aio["name"], url='https://twitter.com/vision_aio', icon_url='https://pbs.twimg.com/profile_images/1334481408119672833/3CsK6QRz_400x400.jpg')
	embed.set_image(url=vision_aio["photos"])

	embed.set_footer(text='From Twitter', icon_url="https://support.content.office.net/en-us/media/0da17e2a-9ed5-496a-b161-9fd4491ce5c7.png")
	embed.set_timestamp()
	webhook.add_embed(embed)
	response = webhook.execute()

else:
	pass

if os.path.getsize('NurikAIO.json') > 0:
	webhook = DiscordWebhook(url=url, content="@"+NurikAIO["username"]+" just tweeted!  " + NurikAIO["link"])
	embed = DiscordEmbed( description=NurikAIO["tweet"], color='03b2f8')
	embed.set_author(name= "@"+NurikAIO["name"], url='https://twitter.com/NurikAIO', icon_url='https://pbs.twimg.com/profile_images/1374056488457605122/nNKzwurK_400x400.jpg')
	embed.set_image(url=NurikAIO["photos"])

	embed.set_footer(text='From Twitter', icon_url="https://support.content.office.net/en-us/media/0da17e2a-9ed5-496a-b161-9fd4491ce5c7.png")
	embed.set_timestamp()
	webhook.add_embed(embed)
	response = webhook.execute()

else: 
	pass

if os.path.getsize('NoraCop.json') > 0:
	webhook = DiscordWebhook(url=url, content="@"+NoraCop["username"]+" just tweeted!  " + NoraCop["link"])
	embed = DiscordEmbed( description=NoraCop["tweet"], color='03b2f8')
	embed.set_author(name= "@"+NoraCop["name"], url='https://twitter.com/NoraCops', icon_url='https://pbs.twimg.com/profile_images/1379608782716743687/cN5lMSFl_400x400.jpg')
	embed.set_image(url=NoraCop["photos"])

	embed.set_footer(text='From Twitter', icon_url="https://support.content.office.net/en-us/media/0da17e2a-9ed5-496a-b161-9fd4491ce5c7.png")
	embed.set_timestamp()
	webhook.add_embed(embed)
	response = webhook.execute()




