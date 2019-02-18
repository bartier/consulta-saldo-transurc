FIRST_URL = 'https://www.transurc.com.br/index.php/servicos/saldo/'

second_url = ''  # dynamically discovered with the FIRST_URL

THIRD_URL = 'https://www.transurc.com.br/SiteApp2018/SaldoCartao/Default.aspx'

# Header of the first request (FIRST_URL)
headers__1 = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Host': 'www.transurc.com.br'
}

# Header of the second request (second_url)
headers__2 = headers__1.copy()
headers__2['Referer'] = 'https://www.transurc.com.br/index.php/servicos/saldo/'

# Header of the third request (THIRD_URL)
headers__3 = headers__1.copy()
headers__3['Cache-Control'] = 'max-age=0'
headers__3['Cookie'] = 'dynamic_value'  # The value of 'Cookie' is find in the second request
