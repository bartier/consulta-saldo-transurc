from bs4 import BeautifulSoup
import utils.values as val
import requests


def create_session():
    print('Criado uma sessão para tornar todas as chamadas relacionadas\n')
    return requests.Session()


def send_first_request(session):
    print('(1) Enviando chamada para ' + val.FIRST_URL)

    response = session.get(val.FIRST_URL, headers=val.headers__1)

    print('Primeira chamada para ' + val.FIRST_URL + ' concluída')
    print('Cookies adicionados de ' + val.FIRST_URL + ': ' + str(session.cookies.get_dict()) + '\n')

    return response


def send_second_request(session, second_url):
    print('(2) Enviando chamada para ' + second_url)

    response = session.get(second_url, headers=val.headers__2)

    print('Segunda chamada para ' + second_url + ' concluída')
    print('Cookies adicionados de ' + second_url + ': ' + str(session.cookies.get_dict()) + '\n')

    return response


def send_third_request(session, third_url):
    print('\n(3) Enviando chamada para ' + third_url)

    response = session.get(third_url, headers=val.headers__3)

    print('Terceira chamada para ' + third_url + ' concluída\n')

    return response


def send_last_request(session, third_response, user_data):
    third_response_soup = BeautifulSoup(third_response.text, 'html.parser')

    input_hidden = third_response_soup.find_all('input')

    img_link = third_response_soup.find(id='CphBody_ASPxCaptcha1_IMG')

    print('Captcha --> https://www.transurc.com.br' + img_link.get('src'))

    image_captcha = input('Acesse o link do captcha e digite o valor: ')

    # sorry for the giant function, I'll refactor someday

    # OK
    val.payload__4['__EVENTTARGET'] = input_hidden[0].get('value')

    # OK
    val.payload__4['__EVENTARGUMENT'] = input_hidden[1].get('value')

    # OK
    val.payload__4['__VIEWSTATE'] = input_hidden[2].get('value')

    # OK
    val.payload__4['__VIEWSTATEGENERATOR'] = input_hidden[3].get('value')

    # OK
    val.payload__4['__VIEWSTATEENCRYPTED'] = input_hidden[4].get('value')

    # OK
    val.payload__4['__EVENTVALIDATION'] = input_hidden[5].get('value')

    # OK
    val.payload__4['ctl00$CphBody$txtIssId'] = '21'

    # OK
    val.payload__4['ctl00$CphBody$ddlNumAplicacao'] = user_data['num_aplicacao']

    # OK
    val.payload__4['ctl00$CphBody$txtNumCartao'] = user_data['num_cartao']

    # OK
    val.payload__4['ctl00$CphBody$txtDigitoVerificador'] = user_data['digito_verificador']

    # OK
    val.payload__4['ctl00$CphBody$txtDtNasc'] = user_data['data_nascimento']

    # OK
    val.payload__4['ctl00$CphBody$ASPxCaptcha1$TB$State'] = '{&quot;validationState&quot;:&quot;&quot;}'

    val.payload__4['ctl00$CphBody$ASPxCaptcha1$TB'] = image_captcha

    # OK
    val.payload__4['ctl00$CphBody$btnPesquisar'] = 'Pesquisar'

    # OK
    val.payload__4['__RequestVerificationToken'] = input_hidden[-1].get('value')

    # OK
    val.payload__4['DXScript'] = '1_14,1_15,1_26,1_64,1_16,1_17,1_18,1_244,1_224,1_225'

    # OK
    val.payload__4['DXCss'] = """1_248,1_67,1_68,1_69,1_247,1_251,1_250,/SiteApp2018/bundles/boo
                tstrapcss?v=MpoKP13sMSQ_jNus11O77RoQXY-F62QMSym2weZ7ieU1,/SiteA
                pp2018/bundles/font-awesome?v=3iEv8vqPidB6TVfgNOGrLoJr-SPH_mV3Y
                wpggEk2_ao1"""

    print('\n(4) Enviando última chamada para ' + val.LAST_URL)

    response = session.post(val.LAST_URL, headers=val.headers__4, data=val.payload__4)

    print('Última chamada para ' + val.LAST_URL + ' concluída\n')

    return response


def find_second_url(first_response):
    first_response_soup = BeautifulSoup(first_response.text, 'html.parser')

    iframes = first_response_soup.find_all('iframe')

    second_url = iframes[0].get('src')

    return second_url


def make_cookie_value(session):
    cookie_session_value = ''.join('{}={}; '.format(key, value) for key, value in session.cookies.items())

    # Remove last two characters because of '; ' at the end of the string
    cookie_session_value = cookie_session_value[:-2]

    return cookie_session_value


def add_new_header(header, key, value):
    #print('Adicionando novo header \'' + key + '\'' + ' com valor: ' + value)
    header[key] = value


def save_file(response, file_name):
    with open(file_name, 'w') as file:
        file.write(response.text)


def get_balance(last_response):
    last_response_soup = BeautifulSoup(last_response.text, 'html.parser')

    balance_tag = last_response_soup.find(id='CphBody_lblSaldoAtual_ES')

    unformatted_balance = balance_tag.contents

    return unformatted_balance[0]
