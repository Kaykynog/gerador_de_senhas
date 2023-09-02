import random
import string

def gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais):
    caracteres = ""

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print("Por favor, selecione pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")

    comprimento = int(input("Informe o comprimento da senha desejada: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (S/N): ").strip().lower() == 's'
    incluir_numeros = input("Incluir números? (S/N): ").strip().lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (S/N): ").strip().lower() == 's'

    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)

    if senha:
        print(f"Sua senha segura gerada é: {senha}")
    else:
        print("Nenhuma senha foi gerada. Tente novamente.")

if __name__ == "__main__":
    main()
