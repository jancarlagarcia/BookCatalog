#DADOS DO SISTEMA
import json
import os

ARQUIVO = 'acervo.json'


def carregar_acervo():
    if not os.path.exists(ARQUIVO):
        return []
    
    with open(ARQUIVO, 'r', encoding = 'utf-8') as arquivo:
        return json.load(arquivo)
    

def salvar_acervo(acervo):
    with open (ARQUIVO, 'w', encoding = 'utf-8') as arquivo:
        json.dump(acervo, arquivo, ensure_ascii=False, indent = 4)

acervo = carregar_acervo()

