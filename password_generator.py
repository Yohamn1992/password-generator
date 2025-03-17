import string
import random

# Definição de senha com 8 dígitos
def password_generator(len_pass=8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options
    
    password_user = ''
    
    # Loop para gerar a senha
    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit
    
    # Retornar a resposta ao usuário
    return password_user

# Loop para continuar gerando senhas ou recomeçar em caso de erro
while True:
    choice_user = input('Quantos dígitos para a senha? ')
    
    if choice_user.isdigit():
        choice_user = int(choice_user)
        response = password_generator(len_pass=choice_user)
        print(f'Senha gerada com sucesso!\n{response}')
        
        # Pergunta se o usuário quer gerar outra senha
        while True:
            new_password = input('Deseja gerar outra senha? (s/n): ').lower()
            
            # Valida se o input é 's' ou 'n'
            if new_password == 's':
                break  # Se 's', volta ao início e gera nova senha
            elif new_password == 'n':
                print('Até mais!')
                quit()  # Se 'n', finaliza o programa
            else:
                print('Entrada inválida! Por favor, digite "s" para sim ou "n" para não.')  # Reforça a resposta correta

    else:
        print('Entrada inválida! Digite novamente um número válido.')
