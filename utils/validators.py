import re

def validar_nome(nome: str) -> bool:
    
    partes = nome.strip().split()
    return len(partes) >= 2 and all(p.isalpha() for p in "".join(partes))

def validar_email(email: str) -> bool:
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = ((soma * 10) % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = ((soma * 10) % 11) % 10

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])
