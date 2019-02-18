import utils.values as val
import utils.functions as f

print('Consulta Saldo Transurc\n')


session = f.create_session()

first_response = f.send_first_request(session)

val.second_url = f.find_second_url(first_response)

second_response = f.send_second_request(session, val.second_url)

# Create value of the header 'Cookie' necessary to the third request
cookie_value = f.make_cookie_value(session)
f.add_new_header(val.headers__3, 'Cookie', cookie_value)

third_response = f.send_third_request(session, val.THIRD_URL)

f.save_consulta_saldo_form_file_html(third_response)

print('The session is apparently correct. Fill the form and make a POST request (?) GOOD LUCK')

