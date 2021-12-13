import discord
from dotenv import load_dotenv
import os
import requests
import random
from discord.ext import commands
from emoji import emojize
from discord_slash import SlashCommand, SlashContext
import json

load_dotenv()
TOKEN = 'TOKEN'

client = commands.Bot(command_prefix = '?', self_bot=False, case_insensitive=True, intents=discord.Intents.default())
slash = SlashCommand(client, sync_commands=True)

# status untuk reaksi
react_stat = 'unset'

# global variabel
counter = 1
data = []


# kumpulan emoji
red_heart = emojize('❤️')
like = emojize('👍')
dislike = emojize('👎')
panco = emojize('💪')
smile_one = emojize('😁')
smile_two = emojize('😃')
think = emojize('🤔')
agree  =emojize('🤝')
right_arrow = emojize('➡')
left_arrow = emojize('⬅')
edit = emojize('⌨️')
page = emojize('🔹️')
ind = emojize('🇮🇩️')


def get_color():
	color = "0x"
	while True:
		choose = "abcdef0123456789"
		clr = random.choice(choose)
		color += clr
		if len(color) == 8:
			break
	return color


def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = response.json()
	quote = json_data[0]["q"] + "\n ~*" + json_data[0]["a"] + "*"
	return(quote)

def reset_react_stat():
	global react_stat
	react_stat = 'unset'
	return react_stat



@client.event
async def on_ready():
    global data
    print(f"Logged in as {client.user}")
    data = []
    for guild in client.guilds:
        data.append(guild.id)
    with open('guild_ids.json', 'w') as file:
        json.dump(data, file)
        file.close()



@client.command(name='test')
async def _test(ctx, arg):
	reset_react_stat()
	global edit
	global react_stat
	react_stat = 'test'
	emb = discord.Embed(title="KBBI", description="Sebelumn edit")
	message = await ctx.send(embed=emb)
	await message.add_reaction(edit)


	if react_stat == 'test':
		@client.event
		async def on_raw_reaction_add(payload):
			reaction = payload.emoji
			member = payload.member
			if member != client.user:
				emb = discord.Embed(title="KBBI", description="Editan selesai")
				await message.edit(embed=emb)


		# @client.event
		# async def on_raw_reaction_remove(payload):
		# 	print(str(payload.emoji))

	# def check(reaction, user):
	# 	return user == ctx.author and str(reaction.emoji) == right_arrow
	# await client.wait_for('reaction_add', timeout=60.0, check=check)
	# await ctx.send("ke kanan")

	# def check(reaction, user):
	# 	return user == ctx.author and str(reaction.emoji) == left_arrow
	# await client.wait_for('reaction_add', timeout=60.0, check=check)
	# await ctx.send("ke kiri")



description = "Command yang diawali dengan $wifu tidak menyediakan nama atau informasi tambahan dari karakter. Pilihan yang bisa dicari : waifu, pat, neko, shinobu, megumin, cuddle, blush, nom"

@client.command(name='wifu', description=description)
async def _wifu(ctx, option):
	reset_react_stat()
	if option == 'waifu':
		req = requests.get('https://api.waifu.pics/sfw/waifu').json()
		image = req["url"]
		emb = discord.Embed(title="Waifu Random", description="Nama karakter belum bisa diperoleh", color=int(get_color(), 16))
		emb.set_image(url=image)
		emb.set_thumbnail(url='https://static.zerochan.net/Rem.%28Re%3AZero%29.full.2012467.jpg')
		await ctx.send(embed=emb)

	if option == 'pat':
		req = requests.get('https://api.waifu.pics/sfw/pat').json()
		image = req["url"]
		emb = discord.Embed(title="Waifu Random", description="Nama karakter belum bisa diperoleh", color=int(get_color(), 16))
		emb.set_image(url=image)
		await ctx.send(embed=emb)

	if option == 'neko':
		req = requests.get('https://api.waifu.pics/sfw/neko').json()
		image = req["url"]
		emb = discord.Embed(title="Waifu Random", description="Nama karakter belum bisa diperoleh", color=int(get_color(), 16))
		emb.set_image(url=image)
		await ctx.send(embed=emb)

	if option == 'shinobu':
		req = requests.get('https://api.waifu.pics/sfw/shinobu').json()
		image = req["url"]
		emb = discord.Embed(title="Shinobu", description=f"Sumber : {image}", color=int(get_color(), 16))
		emb.set_image(url=image)
		await ctx.send(embed=emb)

	if option == 'megumin':
		req = requests.get('https://api.waifu.pics/sfw/megumin').json()
		image = req["url"]
		emb = discord.Embed(title="Megumin", description=f"Sumber : {image}", color=int(get_color(), 16))
		emb.set_image(url=image)
		await ctx.send(embed=emb)

	if option == 'cuddle':
		req = requests.get('https://api.waifu.pics/sfw/cuddle').json()
		image = req["url"]
		emb = discord.Embed(title="Waifu Random", description="Nama karakter belum bisa diperoleh", color=int(get_color(), 16))
		emb.set_image(url=image)
		await ctx.send(embed=emb)

	if option == 'blush':
		req = requests.get('https://api.waifu.pics/sfw/blush').json()
		image = req["url"]
		emb = discord.Embed(title="Waifu Random", description="Nama karakter belum bisa diperoleh", color=int(get_color(), 16))
		emb.set_image(url=image)
		await ctx.send(embed=emb)

	if option == 'nom':
		req = requests.get('https://api.waifu.pics/sfw/nom').json()
		image = req["url"]
		emb = discord.Embed(title="Waifu Random", description="Nama karakter belum bisa diperoleh", color=int(get_color(), 16))
		emb.set_image(url=image)
		await ctx.send(embed=emb)


@client.command(name="neko")
async def _neko(ctx):
	reset_react_stat()
	global red_heart
	global smile_two
	global react_stat
	react_stat = 'neko'

	req = requests.get('https://nekos.best/api/v1/nekos').json()
	image = req["url"]
	artist = req["artist_name"]
	artist_href = req["artist_href"]
	sumber = req["source_url"]
	emb = discord.Embed(title="Neko Mimi", description=f"Ahaa penggemar neko mimi!\nArtist : {artist}\nArtist href : {artist_href}\nSource : {sumber}", color=int(get_color(), 16))
	emb.set_image(url=image)
	message = await ctx.send(embed=emb)

	await message.add_reaction(red_heart)
	await message.add_reaction(smile_two)

	if react_stat == 'neko':
		@client.event
		async def on_raw_reaction_add(payload):
			reaction = str(payload.emoji)
			member = payload.member
			global counter
			global react_stat
			if reaction == red_heart and counter == 1:
				await ctx.send("Ayo claim!!!")
				counter += 1
				if counter > 1:
					reset_react_stat()


@client.command(name="pic")
async def _pic(ctx, width: int, height: int):
	reset_react_stat()
	req = requests.get(f'https://picsum.photos/{width}/{height}').url
	await ctx.send(req)


@client.command(name="pixabay")
async def _pixabay(ctx, page):
	reset_react_stat()
	req = requests.get('https://pixabay.com/api/?key=23674684-9f5640643ea73d520e6c34326&caetgory=background&safesearch=true&order=popular&pretty=true&q=flower&per_page=5&page={}'.format(page)).json()
	result = req["hits"]
	for i in range(len(result)):
		await ctx.send(result[i]["webformatURL"])


@client.command(name='inspire')
async def _inspire(ctx):
	reset_react_stat()
	quote = get_quote()
	await ctx.send(quote)


@client.command(name="calc")
async def _calc(ctx, num1: float, operand, num2: float):
	reset_react_stat()
	if operand == "+":
		await ctx.send(num1 + num2)
	elif operand == "-":
		await ctx.send(num1 - num2)
	elif operand == "*":
		await ctx.send(num1 * num2)
	elif operand == "/":
		await ctx.send(num1 / num2)
	else:
		await ctx.send("Mau ngitung apa waw?")



@client.command(name="kbbi")
async def _kbbi(ctx, kosakata):
	reset_react_stat()
	global ind
	global right_arrow
	global left_arrow
	global react_stat
	react_stat = 'kbbi'
	req = requests.get('https://new-kbbi-api.herokuapp.com/cari/{}'.format(kosakata)).json()
	global hasil
	hasil = len(req["data"])
	makna = req["data"]

	global current_kbbi_page
	current_kbbi_page = 1

	emb = discord.Embed(title="KBBI", description=f"{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}\nKosakata yang dicari : **{kosakata}**\n\n\n\nLema        \n> _{makna[current_kbbi_page - 1]['lema']}_\nArti        \n> _{makna[current_kbbi_page - 1]['arti'][0]['kelas_kata']}_\nDeskripsi        \n> _{makna[current_kbbi_page - 1]['arti'][0]['deskripsi']}_\n\nHalaman **{current_kbbi_page}/{hasil}**", color=0xaaaaaa)
	message = await ctx.send(embed=emb)
	await message.add_reaction(left_arrow)
	await message.add_reaction(right_arrow)

	async def inc_page():
		global current_kbbi_page
		global hasil
		current_kbbi_page += 1
		if current_kbbi_page - 1 == hasil:
			current_kbbi_page = 1
		emb = discord.Embed(title="KBBI", description=f"{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}\nKosakata yang dicari : **{kosakata}**\n\n\n\nLema        \n> _{makna[current_kbbi_page - 1]['lema']}_\nArti        \n> _{makna[current_kbbi_page - 1]['arti'][0]['kelas_kata']}_\nDeskripsi        \n> _{makna[current_kbbi_page - 1]['arti'][0]['deskripsi']}_\n\nHalaman **{current_kbbi_page}/{hasil}**", color=0xaaaaaa)
		await message.edit(embed=emb)

	async def dec_page():
		global current_kbbi_page
		global hasil
		current_kbbi_page -= 1
		if current_kbbi_page == 0:
			current_kbbi_page = hasil
		emb = discord.Embed(title="KBBI", description=f"{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}{ind}\nKosakata yang dicari : **{kosakata}**\n\n\n\nLema        \n> _{makna[current_kbbi_page - 1]['lema']}_\nArti        \n> _{makna[current_kbbi_page - 1]['arti'][0]['kelas_kata']}_\nDeskripsi        \n> _{makna[current_kbbi_page - 1]['arti'][0]['deskripsi']}_\n\nHalaman **{current_kbbi_page}/{hasil}**", color=0xaaaaaa)
		await message.edit(embed=emb)

	if react_stat == 'kbbi':
		@client.event
		async def on_raw_reaction_add(payload):
			reaction = str(payload.emoji)
			member = payload.member
			if member != client.user and reaction == right_arrow:
				await inc_page()
			elif member != client.user and reaction == left_arrow:
				await dec_page()

		@client.event
		async def on_raw_reaction_remove(payload):
			reaction = str(payload.emoji)
			member = payload.member
			if member != client.user and reaction == right_arrow:
				await inc_page()
			elif member != client.user and reaction == left_arrow:
				await dec_page()


@client.command(name="gif", description="Mencari 50 gif random dari gif tenor. Contoh cara mencari :\n$gif bunga")
async def _gif(ctx, *query):
	reset_react_stat()
	opt = random.randint(0, 50)
	query = '+'.join(query)
	req = requests.get(f'https://g.tenor.com/v1/search?key=L0PVL4TV1391&q={query}&limit=50&media_filter=minimal').json()
	hasil = req["results"][opt]["media"][0]["gif"]["url"]
	await ctx.send(hasil)


@slash.slash(name='cek', guild_ids=data)
async def _cek(ctx: SlashContext, arg):
    await ctx.send('Berhasil! => {}'.format(arg))


client.run(os.getenv(TOKEN))
