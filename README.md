# consulta-saldo-transurc


[![GitHub stars](https://img.shields.io/github/stars/bartier/consulta-saldo-transurc)](https://github.com/bartier/consulta-saldo-transurc/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bartier/consulta-saldo-transurc)](https://github.com/bartier/consulta-saldo-transurc/network)
[![GitHub license](https://img.shields.io/github/license/bartier/consulta-saldo-transurc)](https://github.com/bartier/consulta-saldo-transurc/blob/master/LICENSE)

![logo-1](https://user-images.githubusercontent.com/18057391/68075529-8aa51e00-fd87-11e9-9d51-83b8a9d53a4a.png)


Consulte o saldo do seu bilhete único da Transurc via script.

## Instruções para começar

### Pré-requisitos

O que você precisa pra começar:

- [Docker](https://docs.docker.com/install/)

Primeiro clone esse repositório (ou faça um fork e substitua /bartier pelo seu user do GitHub)

```
git clone https://github.com/bartier/consulta-saldo-transurc.git
```

Na raiz do projeto, construa a imagem consulta-saldo-transurc com o Dockerfile

```
docker build -t consulta-saldo-transurc .
```

## Execução

```
Usage: main.py [OPTIONS]

  Obtém seu saldo do cartão de bilhete único da Transurc

Options:
  -n, --num-aplicacao TEXT       Número da aplicação só pode assumir os
                                 valores 03, 04, 07 e 11  [required]
  -c, --cartao TEXT              Número do cartão a ser consultado no formato
                                 XXXXXXXX, em que X é um algarismo  [required]
  -d, --digito-verificador TEXT  Digito verificador do cartão  [required]
  -t, --data-nascimento TEXT     Data de nascimento no formato DD/MM/AAAAA
                                 [required]
  -m, --imgur-client-id TEXT     A aplicação utiliza o Imgur para realizar o
                                 upload do captcha com o objetivo de gerar o
                                 link.  [required]
  --headless                     Se a flag é utilizada, o browser é iniciado
                                 no modo headless, isto é, sem interface
                                 gráfica
  --help                         Show this message and exit.
```

Para executar o projeto, utilize o comando do docker com os dados de consulta:

Considere *X* um número qualquer, *DD* o dia do aniversário, *MM* o mês e *AA* o ano.

```
docker run -it --rm consulta-saldo-transurc -n XX -c XXXXXXXX -d X -t DD/MM/AAAA -m <imgur_client_id> --headless
docker run -it --rm consulta-saldo-transurc -n 03 -c 00123456 -d 4 -t 01/02/1980 -m <imgur_client_id> --headless
```

## Contribuição

Este projeto é open-source. Sinta-se à vontade para contribuir!

## Licença

Esse projeto é licenciado através de uma licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
