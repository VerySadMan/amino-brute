from app.choice import choice
import asyncio
import pyfiglet
import os

async def start():
	os.system('clear')
	config = configparser.ConfigParser()

	print(pyfiglet.figlet_format("S.W.M", font="slant"))
	print("----------------t.me/post11x----------------")
	auth_type = int(input('1-Брут по почте\n2-Брут по номеру телефона.\n\n[S.W.M] -- > '))
	if auth_type == 1 or auth_type == 2:
		await choice(auth_type)
	else:
		print('[S.W.M] -- > Данного параметра не существует.')

if __name__ == "__main__":
	asyncio.run(start())
