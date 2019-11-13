#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pkg_resources
import time
import sys

import click
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from BalancePage import BalancePage
from Imgur import Imgur

chrome_driver_path = pkg_resources.resource_filename("chromedriver_linux64", "chromedriver")


@click.command()
@click.option("-n", "--num-aplicacao", required=True,
              help="Número da aplicação só pode assumir os valores 03, 04, 07 e 11")
@click.option("-c", "--cartao", required=True,
              help="Número do cartão a ser consultado no formato XXXXXXXX, em que X é um algarismo")
@click.option("-d", "--digito-verificador", required=True, help="Digito verificador do cartão")
@click.option("-t", "--data-nascimento", required=True, help="Data de nascimento no formato DD/MM/AAAAA")
@click.option("-m", "--imgur-client-id", required=True,
              help="A aplicação utiliza o Imgur para realizar o upload do captcha com o objetivo de gerar o link.")
@click.option("--headless", default=False, is_flag=True,
              help="Se a flag é utilizada, o browser é iniciado no modo headless, isto é, sem interface "
                   "gráfica")
@click.option("-i", "--timeout", default=8, required=False,
              help="Timeout para esperar a página ser carrega após enviar o formulário e obter o saldo")
def main(num_aplicacao, cartao, digito_verificador, data_nascimento, imgur_client_id, headless, timeout):
    """ Obtém seu saldo do cartão de bilhete único da Transurc """

    print('Iniciando script...aguarde!')
    chrome_options = ChromeOptions()

    if headless:
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    driver.implicitly_wait(3)

    driver.get("https://www.transurc.com.br/index.php/servicos/saldo/")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    balance_page = BalancePage(driver)

    balance_page.fill_num_aplicacao(num_aplicacao)
    time.sleep(1.3)
    balance_page.fill_num_cartao(cartao)
    balance_page.fill_digito_verificador(digito_verificador)
    balance_page.fill_data_nascimento(data_nascimento)

    imgur = Imgur(imgur_client_id)

    captcha_image_as_base64 = balance_page.get_captcha_as_base64()

    captcha_link_imgur = imgur.upload_image(captcha_image_as_base64)

    print(f'Captcha --> {captcha_link_imgur}')
    captcha_from_input = input(f'Acesse o link do captcha e insira aqui: ')

    balance_page.fill_captcha(captcha_from_input)

    time.sleep(1)

    balance_page.submit_form()

    balance = balance_page.get_balance(timeout)

    if balance is None:
        print("\nNão foi possível obter o saldo do cartão, tente novamente.")
        sys.exit(1)

    print("\n===== Resultado da Consulta =====\n")
    print(balance)


if __name__ == "__main__":
    main()
