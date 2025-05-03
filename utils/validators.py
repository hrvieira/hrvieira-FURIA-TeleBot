import re

def validar_nome(nome: str) -> bool:
    
    partes = nome.strip().split()
    return len(partes) >= 2 and all(p.isalpha() for p in "".join(partes))

def validar_email(email: str) -> bool:
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def validar_cpf(cpf: str) -> bool:
    
    cpf_numeros = re.sub(r'\D', '', cpf)
    return len(cpf_numeros) == 11 and cpf_numeros.isdigit()
