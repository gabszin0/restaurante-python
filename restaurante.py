# |Utilização de funções|
# Print: Imprime algo no console 
# Input: Receber dados, e imprime uma mensagem
# Match: Simplificar a lógica do código, deixando mais legível
# def: Criação de uma função
# try: Tentar um trecho do código
# except: caso o "try" não funcione

import os


# Criação de lista de estrutura de dados!
# Lista que se transforma em um Dicionário!
restaurantis = [{'nome':'BoraBiuPizza', 'categoria':'Pizza','ativo':True},
                {'nome':'Sushi', 'categoria':'japonesa','ativo':False}]


def exibir_nome():
    print(""" 
████████╗░█████╗░  ░█████╗░░█████╗░███╗░░░███╗  ███████╗░█████╗░███╗░░░███╗███████╗
╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗████╗░████║  ██╔════╝██╔══██╗████╗░████║██╔════╝
░░░██║░░░██║░░██║  ██║░░╚═╝██║░░██║██╔████╔██║  █████╗░░██║░░██║██╔████╔██║█████╗░░
░░░██║░░░██║░░██║  ██║░░██╗██║░░██║██║╚██╔╝██║  ██╔══╝░░██║░░██║██║╚██╔╝██║██╔══╝░░
░░░██║░░░╚█████╔╝  ╚█████╔╝╚█████╔╝██║░╚═╝░██║  ██║░░░░░╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░░╚════╝░  ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░░░░╚═╝╚══════╝\n""")


def opcoes():
    print('1. Cadastrar Restaurante')

    print('2. Listar Restaurante')

    print('3. Ativar Restaurante')

    print('4. Sair\n')


# Funções que se repetem!
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def finalizar_app():
    # Puxando nova biblioteca, e dando clear no console!
    exibir_subtitulo('Finalizando o app')

def opcao_inva():
    print('Opção Inválida!!')
    voltar_menu()

def voltar_menu():
    input('Digite um tecla para voltar ao menu!')
    main()




def cadastro_resta():
    exibir_subtitulo('Cadastro de novo restaurante\n')

    rest_nome = input('Digite o nome do restaurente: ')

    cate = input(f'Digite a categoria do {rest_nome}: ')

    rest_data = {'nome':rest_nome, 'categoria':cate, 'ativo':False}
    restaurantis.append(rest_data)

    print(f'O Restaurante "{rest_nome}" foi cadastrado! :)\n')
    voltar_menu()


def listar_resta():
    exibir_subtitulo('Listando os resutaurantes...\n')

    for restaurante in restaurantis:
        nome_resta = restaurante['nome']
        cat = restaurante['categoria']
        ativ = restaurante['ativo']
        print(f'- {nome_resta} | {cat} | {ativ}\n')

    voltar_menu()

def alternar_estado():
    exibir_subtitulo('Ativação e Desativação do Restaurante')

    nome_restaurant = input('Digite o nome do restaurante: ')
    
    for restaurante in restaurantis:
        if nome_restaurant == restaurante['nome']:
            restaurante['ativo'] = not restaurante['ativo']
            msg = f'O restaurante {nome_restaurant} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurant} foi desativado com sucesso\n'
            print(msg)
            break
    else:
        print('Restaurante não foi encontrado :(\n')

            




def escolher_opcao():
    try:
        # Criação de variáveis:
        opcao_escolhida = int(input('Escolha uma opção: '))

        print(f'Você escolheu a opção: {opcao_escolhida}')
        
        # Perceba que recebemos a variável opção_escolhida como parâmetro da instrução match e será feito um comparativo com todos os valores determinados pelos blocos de case, e no final temos uma instrução case _, que é um padrão curinga
        match opcao_escolhida:
            case 1:
                cadastro_resta()
            case 2:
                listar_resta()
            case 3:
                alternar_estado()
            case 4:
                print('Finalizar app\n')
            case _:
                opcao_inva()

    except:
        opcao_inva()    


# Dentro dessa função vamos definir todos os passos que precisamos para que o nosso programa funcione
def main():
    os.system('cls')
    exibir_nome()
    opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()