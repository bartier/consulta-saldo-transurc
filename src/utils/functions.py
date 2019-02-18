from bs4 import BeautifulSoup
import utils.values as val
import requests


def create_session():
    print('Created a session to make all requests related\n')
    return requests.Session()


def send_first_request(session):
    print('Sending first request to ' + val.FIRST_URL)

    response = session.get(val.FIRST_URL, headers=val.headers__1)

    print('First request to ' + val.FIRST_URL + ' completed')
    print('Cookies added from ' + val.FIRST_URL + ': ' + str(session.cookies.get_dict()) + '\n')

    return response


def send_second_request(session, second_url):
    print('Sending second request to ' + second_url)

    response = session.get(second_url, headers=val.headers__2)

    print('Second request to ' + second_url + ' completed')
    print('Cookies added from ' + second_url + ': ' + str(session.cookies.get_dict()) + '\n')

    return response


def send_third_request(session, third_url):
    print('Sending third request to ' + third_url)

    response = session.get(third_url, headers=val.headers__3)

    print('Third request to ' + third_url + ' completed\n')

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
    print('Adding new header \'' + key + '\'' + ' with value: ' + value + '\n')
    header[key] = value


def save_consulta_saldo_form_file_html(response):
    with open('consulta_saldo_form_file.html', 'w') as file:
        file.write(response.text)


