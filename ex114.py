import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('DO site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!')