import json

import requests

URL_ALL = "https://restcountries.com/v2/all"

URL_NAME = "https://restcountries.com/v2/name/brazil"


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return reposta.text
    except:
                print("Erro ao fazer requisicao em, ", url)
                
def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta) #Parsing Json
    except:
        print("Erro ao fazer Parsing")
        
def contagem_de_paises(lista_de_paises):
        return len(lista_de_paises)
        
def listar_paises(lista_de_paises):
        for pais in lista_de_paises:
            print(pais['name'])
def mostrar_populacao(nome_pais):
        requisicao("{}/{}".format(URL_NAME, nome_pais))
        if resposta:
            lista_de_paises = parsing(resposta)
            if lista_de_paises:
                for pais in lista_de_paises:
                    print("{}: {}".format(pais['name'], pais['population']))
                    else:
                        print("Pais nao encontrado!")

def mostrar_moedas(nome_do_pais):
    requisicao("{}/{}".format(URL_NAME, nome_do_pais))
        if resposta:
            lista_de_paises = parsing(resposta)
            if lista_de_paises:
                for pais in lista_de_paises:
                    print("Moedas do", pais['name'])
                    moedas = pais ['currencies']
                    for moeda in moedas:
                        print("{} - {}".format(moeda['name'], moeda['code']))
                 else:
                     print("Pais nao encontrado.")

                
if __name__  == "__main__":
    print("Bem vindo ao API de Paises.")
    