import re
import pandas as pd

def tratar_categoria(valor:str, sub_string:str, nova_categoria):
    valor_limpo = str(valor).replace(' ', '').lower()

    if sub_string in valor_limpo:
        return nova_categoria
    else:
        return valor
    
def tratar_email(texto, caractere_antigo, caractere_novo):

    if caractere_antigo in texto:
        texto = texto.replace(caractere_antigo, caractere_novo)
        return texto
    else:
        return texto
    
def padronizar_location(texto):
    # 1. Extrai a UF — duas letras maiúsculas
    uf = re.search(r'\b[A-Z]{2}\b', texto)
    
    # 2. Extrai cidade entre parênteses se existir
    cidade_parenteses = re.search(r'\(([^)]+)\)', texto)
    
    if cidade_parenteses:
        cidade = cidade_parenteses.group(1)
    else:
        # 3. Remove a UF, separadores, espaços e hifens para sobrar a cidade
        cidade = re.sub(r'\b[A-Z]{2}\b', '', texto)
        cidade = re.sub(r'[\/,\-]', '', cidade).strip()
    
    if uf and cidade:
        return f"{cidade.strip()}, {uf.group()}"
    
    return texto
