from time import sleep

#Funções para módulo interface:

def leiaInt(inputInt):
    while True:
        try:
            n_int = int(input(inputInt))
        except:
            print('\033[0;91m ERRO! Digite um número inteiro válido.\033[0m')
        else: 
            break
    return n_int


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\33[33m{c}\33[m - \33[34m{item}\33[m')
        c += 1
    print(linha())
    opc = leiaInt('\33[32mSua Opção: \33[m')
    return opc

#Funções para módulo arquivo.
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a: #a é a variável que está guardando o arquivo txt.
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')  
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro {nome} adicionado.')
            a.close()


arq = 'arquivo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do programa... Até logo!')
        break
    else:
        cabeçalho('\33[31mERRO! Digite uma opção válida!\33[m')
    sleep(2)



