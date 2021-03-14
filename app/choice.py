import app.brute_email as email
import app.brute_phone as phone
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

async def choice(auth_type):
    word_list = open(config["system"]["patch_to_wordlist"],'r')
    words_collection = word_list.readlines()

    if auth_type == 1:
        email_to_brute = input('[S.W.M] -- > Введите почту: ')
        await email.brute(words_collection, email_to_brute)

    elif auth_type == 2:
        phone_to_brute = int(input('[S.W.M] -- > Введите номер телефона(в формате 77001112647): '))
        await phone.brute(words_collection, phone_to_brute)