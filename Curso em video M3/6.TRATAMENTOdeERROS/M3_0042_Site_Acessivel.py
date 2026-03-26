import urllib
import urllib.request

valor = str(input('Digite o nomedo site: '))
while True:
    try:
        site = urllib.request.urlopen(f'https://www.{valor}.com')
    except urllib.error.URLError:
        print(f'O site {valor} nao esta acessivel')
        break
    else:
        print(f'Consegui acessar o site {site.url} com sucesso!'.replace('https://www.',''))
        break
        break
    finally:
        print('\nObrigado por usar o site')