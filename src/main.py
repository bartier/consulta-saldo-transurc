import utils.values as val
import utils.functions as f
import sys


print('Consulta Saldo Transurc\n')

session = f.create_session()

first_response = f.send_first_request(session)

val.second_url = f.find_second_url(first_response)

second_response = f.send_second_request(session, val.second_url)

# Create value of the header 'Cookie' necessary to the third request and last request
cookie_value = f.make_cookie_value(session)
f.add_new_header(val.headers__3, 'Cookie', cookie_value)
f.add_new_header(val.headers__4, 'Cookie', cookie_value)

third_response = f.send_third_request(session, val.THIRD_URL)

# f.save_file(third_response, 'consulta_saldo_form_file.html')

#user_data = {'num_aplicacao':      input('Digite o número antes do cartão (XX): '),
#             'num_cartao':         input('Digite o número do seu cartão (XX): '),
#             'digito_verificador': input('Digite o número verificador (X): '),
#             'data_nascimento':    input('Digite a sua data de nascimento (DD/MM/AAAA): ')}

user_data = {'num_aplicacao':      sys.argv[1],
             'num_cartao':         sys.argv[2],
             'digito_verificador': sys.argv[3],
             'data_nascimento':    sys.argv[4]}



# Last response contains the balance
last_response = f.send_last_request(session, third_response, user_data)

balance = f.get_balance(last_response)

print('\nSeu saldo no bilhete único é ' + balance)

# f.save_file(last_response, 'saldo_result.html')
