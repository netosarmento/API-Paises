import json
import sys
import requests

URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name/"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requisição em,", url)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)  # Parsing Json
    except:
        print("Erro ao fazer Parsing")

def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_populacao(nome_pais):
    resposta = requisicao(f"{URL_NAME}{nome_pais}")
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("{}: {} Habitantes".format(pais['name'], pais['population']))
        else:
            print("País não encontrado!")

def mostrar_moedas(nome_do_pais):
    resposta = requisicao(f"{URL_NAME}{nome_do_pais}")
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("Moedas do", pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print("{} - {}".format(moeda['name'], moeda['code']))
        else:
            print("País não encontrado.")

def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("É preciso passar o nome do país")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("## Bem vindo ao API de Paises. ##")
        print("Uso: python paises.py <acao> <nome do país>")
        print("Ações Disponíveis:\n contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
            numero_de_paises = contagem_de_paises()
            print("Existem {} países no mundo todo".format(numero_de_paises))
        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("Ação inválida. Ações disponíveis: contagem, moeda, populacao")
