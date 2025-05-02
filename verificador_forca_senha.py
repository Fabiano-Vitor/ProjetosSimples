import re

def verificar_forca_senha(senha):
    if len(senha) < 8:
        return "Fraca (menos de 8 caracteres)"
    if not re.search(r"[A-Z]", senha):
        return "Fraca (sem letra maiúscula)"
    if not re.search(r"[a-z]", senha):
        return "Fraca (sem letra minúscula)"
    if not re.search(r"[0-9]", senha):
        return "Fraca (sem número)"
    if not re.search(r"[!@#$%^&*()_+=-]", senha):
        return "Fraca (sem símbolo especial)"
    return "Forte"

senha_usuario = input("Digite uma senha para verificar: ")
print("Força da senha:", verificar_forca_senha(senha_usuario))
