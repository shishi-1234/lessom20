import requests
import pprint
url = 'https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc'
#token = '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'
#result = requests.get(url, auth=('shishi-1234', token))
#headers = {
    #'Autorization': f'tokenP{token}'
#}
#result = requests.get(url, headers= headers)

session = requests.session()
#session.auth = ('shishi-1234', token)
#pprint.pprint(result.json())


url = 'https://api.github.com/search/code?g=addClass+in:file+language:js+repo:jqury/jquery'
result = session.get(url)
pprint.pprint(result.json())

url= 'https://api.github.com/search/code?g=eval+in:file+language:python+user:Yusiloid'
result = session.get(url)
pprint.pprint(result.json())