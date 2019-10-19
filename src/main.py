# coding=utf-8
import sys

import config
from utils import (
    create_session, send_third_request, send_last_request,
    make_cookie_value, add_new_header, get_balance,
)


def start():
    print('Consulta Saldo Transurc\n')

    session = create_session()

    # first_response = send_first_request(session)
    # second_url = find_second_url(first_response)
    # second_response = send_second_request(session, second_url)

    # Create value of the header 'Cookie' necessary to the
    # third request and last request
    cookie_value = make_cookie_value(session)
    add_new_header(config.HEADERS_3, 'Cookie', cookie_value)
    add_new_header(config.HEADERS_4, 'Cookie', cookie_value)

    third_response = send_third_request(session, config.THIRD_URL)

    # save_file(third_response, 'consulta_saldo_form_file.html')

    # user_data = {
    #     'num_aplicacao': input('Digite o número antes do cartão (XX): '),
    #     'num_cartao': input('Digite o número do seu cartão (XX): '),
    #     'digito_verificador': input('Digite o número verificador (X): '),
    #     'data_nascimento': input(
    #         'Digite a sua data de nascimento (DD/MM/AAAA):'
    #     )
    # }

    user_data = {
        'num_aplicacao': sys.argv[1],
        'num_cartao': sys.argv[2],
        'digito_verificador': sys.argv[3],
        'data_nascimento': sys.argv[4],
    }

    # Last response contains the balance
    last_response = send_last_request(session, third_response, user_data)

    balance = get_balance(last_response)

    print('\nSeu saldo no bilhete único é ' + balance)

    # save_file(last_response, 'saldo_result.html')


if __name__ == '__main__':
    start()
