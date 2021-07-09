import requests
try:
    requests.get('http://pudim.com.br/')
except:
    print('\033[031mO site Pudim não está disponível no momento!')
else:
    print('\033[032mO site Pudim foi acessado com sucesso')