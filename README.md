# consulta-saldo-transurc

Consulte o saldo do seu bilhete único da Transurc via script.

## Getting Started

### Prerequisites

What things you need to start hacking:

- [Docker](https://docs.docker.com/install/)

Primeiro clone esse repositório (ou faça um fork e substitua /bartier pelo seu user do GitHub)

```
git clone https://github.com/bartier/consulta-saldo-transurc.git
```

Na raiz do projeto, construa a imagem consulta-saldo-transurc com o Dockerfile

```
docker build -t consulta-saldo-transurc .
```

## Running

Para executar o projeto, utilize o comando do docker com os dados de consulta:

Considere *X* um número qualquer, *DD* o dia do aniversário, *MM* o mês e *AA* o ano.

```
docker run -i --rm consulta-saldo-transurc <num_aplicacao> <num_cartao> <dig_verificador> <data_nasc>
docker run -i --rm consulta-saldo-transurc XX XXXXXXXX XX X DD/MM/AAAA
```


## Contributing

Please feel free for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
