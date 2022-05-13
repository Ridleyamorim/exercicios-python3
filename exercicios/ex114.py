import urllib.request 

try:
    urllib.request.urlopen('http://www.pudim.com.br').getcode()
except:
    print('O site se encontra inacessível no momento.')
else:
    print('O site está funcionando normalmente.')

