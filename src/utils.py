# coding=utf-8
from bs4 import BeautifulSoup
import config
import requests


def create_session():
    # print('Criado uma sessão para tornar todas as chamadas relacionadas\n')
    return requests.Session()


def send_first_request(session):
    # print('(1) Enviando chamada para ' + config.FIRST_URL)

    response = session.get(config.FIRST_URL, headers=config.HEADERS_1)

    # print('Primeira chamada para ' + config.FIRST_URL + ' concluída')
    # print('Cookies adicionados de ' + config.FIRST_URL + ': ' +
    # str(session.cookies.get_dict()) + '\n')

    return response


def send_second_request(session, second_url):
    # print('(2) Enviando chamada para ' + second_url)

    response = session.get(second_url, headers=config.HEADERS_2)

    # print('Segunda chamada para ' + second_url + ' concluída')
    # print('Cookies adicionados de ' + second_url + ': ' +
    # str(session.cookies.get_dict()) + '\n')

    return response


def send_third_request(session, third_url):
    # print('\n(3) Enviando chamada para ' + third_url)

    response = session.get(third_url, headers=config.HEADERS_3)

    # print('Terceira chamada para ' + third_url + ' concluída\n')

    return response


def send_last_request(session, third_response, user_data):
    third_response_soup = BeautifulSoup(third_response.text, 'html.parser')

    input_hidden = third_response_soup.find_all('input')

    img_link = third_response_soup.find(id='CphBody_ASPxCaptcha1_IMG')

    print('Captcha --> https://www.transurc.com.br' + img_link.get('src'))

    image_captcha = input('Acesse o link do captcha e digite o valor: ')

    # sorry for the giant function, I'll refactor someday

    payload = {
        'ctl00$CphBody$txtIssId': '21',
        'ctl00$CphBody$ddlNumAplicacao': user_data['num_aplicacao'],
        'ctl00$CphBody$txtNumCartao': user_data['num_cartao'],
        'ctl00$CphBody$txtDigitoVerificador': user_data['digito_verificador'],
        'ctl00$CphBody$txtDtNasc': user_data['data_nascimento'],
        'ctl00$CphBody$txtDtNasc': user_data['data_nascimento'],
        'ctl00$CphBody$ASPxCaptcha1$TB$State': '{&quot;validationState&quot'
                                               ';:&quot;&quot;}',
        'ctl00$CphBody$ASPxCaptcha1$TB': image_captcha,
        'ctl00$CphBody$btnPesquisar': 'Pesquisar',
        '__RequestVerificationToken': input_hidden[-1].get('value'),
        'DXScript': '1_14,1_15,1_26,1_64,1_16,1_17,1_18,1_244,1_224,1_225 ',
        'DXCss': """1_248,1_67,1_68,1_69,1_247,1_251,1_250,/SiteApp2018/bundles/boo
                tstrapcss?v=MpoKP13sMSQ_jNus11O77RoQXY-F62QMSym2weZ7ieU1,/SiteA
                pp2018/bundles/font-awesome?v=3iEv8vqPidB6TVfgNOGrLoJr-SPH_mV3Y
                wpggEk2_ao1""",
    }

    for i, key in [
        '__EVENTTARGET',
        '__EVENTARGUMENT',
        '__VIEWSTATE',
        '__VIEWSTATEGENERATOR',
        '__VIEWSTATEENCRYPTED',
        '__EVENTVALIDATION',
    ]:
        payload[key] = input_hidden[i].get('value')

    # print('\n(4) Enviando última chamada para ' + config.LAST_URL)

    response = session.post(
        config.LAST_URL,
        headers=config.HEADERS_4,
        data=payload
    )

    # print('Última chamada para ' + config.LAST_URL + ' concluída\n')

    return response


def find_second_url(first_response):
    doc = BeautifulSoup(first_response.text, 'html.parser')
    frame_list = doc.find_all('iframe')

    return frame_list[0].get('src')


def make_cookie_value(session):
    cookie_session_value = ''.join(
        '{}={}; '.format(key, value) for key, value in session.cookies.items())

    # Remove last two characters because of '; ' at the end of the string
    cookie_session_value = cookie_session_value[:-2]

    return cookie_session_value


def add_new_header(header, key, value):
    # print('Adicionando novo header \'' + key + '\'' + ' com valor: ' + value)
    header[key] = value


def save_file(response, file_name):
    with open(file_name, 'w') as file:
        file.write(response.text)


def get_balance(last_response):
    last_response_soup = BeautifulSoup(last_response.text, 'html.parser')

    balance_tag = last_response_soup.find(id='CphBody_lblSaldoAtual_ES')

    unformatted_balance = balance_tag.contents

    return unformatted_balance[0]
