from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import time
import subprocess
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

logo = '''
████████╗░██████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
╚══██╔══╝██╔════╝░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
░░░██║░░░██║░░██╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
░░░██║░░░██║░░╚██╗░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
░░░██║░░░╚██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
░░░╚═╝░░░░╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░ 
█▄▄ █▀▀ ▀█▀ ▄▀█
█▄█ ██▄ ░█░ █▀█'''
logo_ent = '''
██████╗░██╗░█████╗░██████╗░███████╗███╗░░██╗████████╗███████╗██████╗░
██╔══██╗██║██╔══██╗██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║███████║██████╔╝█████╗░░██╔██╗██║░░░██║░░░█████╗░░██████╔╝
██╔═══╝░██║██╔══██║██╔══██╗██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
██║░░░░░██║██║░░██║██║░░██║███████╗██║░╚███║░░░██║░░░███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝'''
logo_leave = '''
██████╗░██╗░█████╗░██████╗░██╗░░░░░███████╗░█████╗░██╗░░░██╗███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔══██╗██║░░░██║██╔════╝
██████╔╝██║███████║██████╔╝██║░░░░░█████╗░░███████║╚██╗░██╔╝█████╗░░
██╔═══╝░██║██╔══██║██╔══██╗██║░░░░░██╔══╝░░██╔══██║░╚████╔╝░██╔══╝░░
██║░░░░░██║██║░░██║██║░░██║███████╗███████╗██║░░██║░░╚██╔╝░░███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝'''

logo_spam = '''
░██████╗██████╗░░█████╗░███╗░░░███╗
██╔════╝██╔══██╗██╔══██╗████╗░████║
╚█████╗░██████╔╝███████║██╔████╔██║
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝'''

piar_logo = '''
██████╗░██╗░█████╗░██████╗░░██████╗██████╗░░█████╗░███╗░░░███╗
██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░████║
██████╔╝██║███████║██████╔╝╚█████╗░██████╔╝███████║██╔████╔██║
██╔═══╝░██║██╔══██║██╔══██╗░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██║░░░░░██║██║░░██║██║░░██║██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝'''
# Remember to use your own values from my.telegram.org!
api_id = 1433417
api_hash = 'b7c9d037fdad2d56f6059d4bb10d0266'

client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Инфа обо мне
	me = await client.get_me()


    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
	username = me.username

    # You can print all the dialogs/conversations that you are part of:
	#async for dialog in client.iter_dialogs():
		#print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
	#await client.send_message('me', 'Рассылка началась!')
	async def Feedback():
		meeagess = input('Введите сообщение, которое будет отправлено разработчику: ')
		try:
			await client.send_message('proger_tilda', meeagess)
		except:
			print('Произошла ошибка! ')
	async def spam_piar():
		try:
			with open('base.txt', "r") as file:
				y = 0
				n = 0
				subprocess.call('cls', shell = True)
				print(piar_logo)
				print('Внимание, если вы не выполнили вход в пиар чаты из дефолтной базы, то сообщение не отправится по всем 1000 чатам! ')
				message = input('Введите сообщение для отправки: ')
				for line in file:
					try:
						await client.send_message(line, message)
						y = y + 1
						print(f'Отправлено в {line}')
					except:
						n = n + 1
		except:
			print('Произошла ошибка! ')
	async def enter():
		subprocess.call('cls', shell = True)
		print(logo_ent)
		try:
			with open('base.txt', "r") as file:
				y = 0
				n = 0
				for line in file:
					try:
						await client(JoinChannelRequest(line))
						y = y + 1
						print(f'Успешно вошел в {line}')
						time.sleep(10)
					except:
						n = n + 1
				print(f'''Успешно - {y}
Неудачно - {n}''')
		except:
			print('Произошла ошибка!')
	async def leave():
		subprocess.call('cls', shell = True)
		print(logo_leave)
		try:
			with open('base.txt', "r") as file:
				y = 0
				n = 0
				for line in file:

					try:
						from telethon.tl.functions.channels import LeaveChannelRequest
						await client(LeaveChannelRequest(line))
						print(f'Успешно вышел из {line}')
						y = y + 1
					except:
						print(f'Не удалось выйти из {line}')
						n = n + 1
				print(f'''Успешно - {y}
Неудачно - {n}''')
		except:
			print('Произошла ошибка!')


	async def spam():
		subprocess.call('cls', shell = True)
		print(logo_spam)
		base1 = input('Путь к базе: ')
		message = input('Сообщение которое хотите отправить: ')
		try:
			with open(base1, "r") as file:
				y = 0
				n = 0
				for line in file:
					try:
						await client.send_message(line, message)
						y = y + 1
					except:
						n = n + 1
				print(f'''Отправлено - {y}
Не отправлено - {n}''')
		except:
			print('Произошла ошибка!')
	#Меню
	subprocess.call('cls', shell = True)
	print(logo)
	print('[1]Вход в пиар чаты')
	print('[2]Выход из пиар чатов')
	print('[3]Рассылка в лчиные сообщения')
	print('[4]Рассылка по пиар чатам')
	what = input('>>> ')
	if what == '1':
		await enter()
	elif what == '2':
		await leave()
	elif what == '3':
		await spam()
	elif what == '4':
		await spam_piar()
with client:
    client.loop.run_until_complete(main())