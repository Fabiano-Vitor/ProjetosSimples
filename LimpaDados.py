import re

def limpar_dados(texto):
    texto = re.sub(r'\d{3}\.\d{3}\.\d{3}-\d{2}', '[CPF REMOVIDO]', texto)
    texto = re.sub(r'\b[\w.-]+?@\w+?\.\w+?\b', '[EMAIL REMOVIDO]', texto)
    texto = re.sub(r'\d{4} \d{4} \d{4} \d{4}', '[CARTÃO REMOVIDO]', texto)
    return texto

entrada = """
Olá, meu nome é João. Meu CPF é 123.456.789-10 e meu e-mail é joao@email.com.
O número do meu cartão é 1234 5678 9012 3456.
"""

print(limpar_dados(entrada))
