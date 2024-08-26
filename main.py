import os

# exibir menu
def exibir_menu():
    print('1 - Ler arquivo.')
    print('2 - Gravar novos dados no arquivo.')
    print('3 - Sair do programa.')

# função para gravar novos dados
def gravar_arquivo(dados, nome, email, profissão):
    novo_conteudo = f'{dados}\n\n{"-"*30}\n\nNome: {nome}\nE-mail: {email}\nProfissão: {profissão}'
    with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(novo_conteudo)

# função de leitura de arquivo
def ler_arquivo():
    if os.path.exists('arquivo.txt'):
        with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
            dados = arquivo.read()
    else:
        dados = ''
    return dados

# programa principal
if __name__ == '__main__':
    while True:
        dados = ler_arquivo()
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela de acordo com o sistema operacional
        match opcao:
            case '1':
                print(f'\n{dados}\n')
            case '2':
                print('NOVO CADASTRO:\n')
                novo_nome = input('Informe o nome do novo usuário: ')
                novo_email = input('Informe o e-mail do novo usuário: ')
                nova_profissão = input('Informe a profissão do novo usuário: ')
                gravar_arquivo(dados, novo_nome, novo_email, nova_profissão)
            case '3':
                print('Programa finalizado.')
                break
            case _:
                print('Opção inválida.')