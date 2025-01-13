import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen(' ')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('tudo certo')
    #print(site.read())