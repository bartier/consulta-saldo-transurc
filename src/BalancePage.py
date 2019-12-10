from Locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class BalancePage:

    def __init__(self, driver):
        self.driver = driver

        self.num_aplicacao_select_id = Locators.num_aplicacao_select_id
        self.num_cartao__input_id = Locators.num_cartao__input_id
        self.num_verificador_input_id = Locators.num_verificador_input_id
        self.data_nascimento_input_id = Locators.data_nascimento_input_id
        self.pesquisar_input_id = Locators.pesquisar_input_id

        self.captcha_img_id = Locators.captcha_img_id
        self.captcha_answer_input_id = Locators.captcha_answer_input_id

        self.alert_message_id = Locators.alert_message_id

        self.estudante_balance_span_id = Locators.estudante_balance_span_id
        self.vale_transporte_balance_div_id = Locators.vale_transporte_balance_div_id
        self.normal_balance_div_id = Locators.normal_balance_div_id

    def fill_num_aplicacao(self, num_aplicacao):
        select_num_aplicacao = Select(self.driver.find_element_by_id(self.num_aplicacao_select_id))

        select_num_aplicacao.select_by_value(num_aplicacao)

    def fill_num_cartao(self, num_cartao):
        for i in range(0, 8):
            self.driver.find_element_by_id(self.num_cartao__input_id).send_keys(Keys.BACK_SPACE)
            time.sleep(0.2)

        for c in num_cartao:
            self.driver.find_element_by_id(self.num_cartao__input_id).send_keys(c)
            time.sleep(0.4)

    def fill_digito_verificador(self, digito_verificador):
        self.driver.find_element_by_id(self.num_verificador_input_id).clear()

        self.driver.find_element_by_id(self.num_verificador_input_id).send_keys(digito_verificador)

    def fill_data_nascimento(self, data_nascimento):
        # hack to fill input correctly
        time.sleep(4)

        # self.driver.find_element_by_id(self.data_nascimento_input_id).clear()
        for i in range(0, 8):
            self.driver.find_element_by_id(self.data_nascimento_input_id).send_keys(Keys.BACK_SPACE)
            time.sleep(0.2)

        for c in data_nascimento:
            self.driver.find_element_by_id(self.data_nascimento_input_id).send_keys(c)

    def fill_captcha(self, captcha):
        self.driver.find_element_by_id(self.captcha_answer_input_id).clear()

        self.driver.find_element_by_id(self.captcha_answer_input_id).send_keys(captcha)

    def get_captcha_as_base64(self):
        return self.driver.find_element_by_id(self.captcha_img_id).screenshot_as_base64

    def submit_form(self):
        self.driver.find_element_by_id(self.pesquisar_input_id).click()

    def get_alert_message(self):
        try:
            alert_content = self.driver.find_element_by_id(self.alert_message_id).text
        except Exception:
            alert_content = None

        return alert_content

    def get_balance(self, timeout):
        print(f'Aguardando {timeout}s para obter o saldo do cartão...')
        time.sleep(timeout)

        balance_text = None

        # CphBody_panVT
        # CphBody_panComum
        try:
            # Estudante
            if self.check_exists_by_id(self.estudante_balance_span_id):
                balance_text = self.driver.find_element_by_id(self.estudante_balance_span_id).text
            else:
                # Cartao Comum possui VT e seção normal
                if self.check_exists_by_id(self.normal_balance_div_id):
                    balance_text = self.driver.find_element_by_id(self.normal_balance_div_id).text

                if self.check_exists_by_id(self.vale_transporte_balance_div_id):
                    balance_text += "\n\n" + self.driver.find_element_by_id(self.vale_transporte_balance_div_id).text

        except Exception:
            alert_content = self.get_alert_message()

            if alert_content is not None:
                print("\n" + self.get_alert_message())
            else:
                print('\nOcorre um erro muito inesperado, desculpe.')

            with open('output.html', "w+") as file:
                file.write(self.driver.page_source)

            return None

        return balance_text

    def check_exists_by_id(self, id):
        try:
            self.driver.find_element_by_id(id)
        except Exception:
            return False
        return True
