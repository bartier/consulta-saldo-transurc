import time
import unittest
import sys
import os

from selenium import webdriver

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from BalancePage import BalancePage


class GetBalanceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver_linux64/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_get_balance(self):
        driver = self.driver

        driver.get("https://www.transurc.com.br/index.php/servicos/saldo/")
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

        balance_page = BalancePage(driver)

        time.sleep(5)
        balance_page.fill_num_aplicacao("03")
        balance_page.fill_num_cartao("00123456")
        balance_page.fill_digito_verificador("4")
        balance_page.fill_data_nascimento("28/07/2000")
        balance_page.fill_captcha("abc1234")

        time.sleep(5)

        balance_page.submit_form()

        alert_message = balance_page.get_alert_message()

        self.assertEqual(alert_message, 'Verifique se você digitou corretamente o texto de segurança.',
                         msg="O erro de captcha esperado não foi obtido.")

        time.sleep(8)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
