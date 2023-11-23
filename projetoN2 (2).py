import random

#cores
vermelho = '\033[31m'
negrito = '\033[1m'
branco = '\033[0m'
verde = '\033[32m'

def cadastro():
    global tel, nome_cli, saldo, email_cli, senha_cli, num_conta, limite_cred, deposito

    print(negrito,'\nMACK BANK - CADASTRO', branco)
    num_conta = random.randint(1000, 10000)
    print(f'NÚMERO DA CONTA: {num_conta}')
    while True:
        nome_cli = input('NOME: ').upper()
        if nome_cli == '':
            print(negrito,'Este campo deve ser preenchido!',branco)
        else:
            break

    while True:
        tel = input('TELEFONE: ')
        if tel == '':
            print(negrito,'Digite um número válido!',branco)
        else:
            break

    while True:
        email_cli = input('INSIRA SEU E-MAIL: ')
        if email_cli == "":
            print(negrito,'Este campo deve ser preenchido!',branco)
        elif "@" not in email_cli:
            print(negrito,'O e-mail deve conter um "@"!',branco)
        elif "." not in email_cli:
            print(negrito,'O e-mail dever conter um "."!',branco)
        else:
            break

    while True:
        saldo = float(input('SALDO INICIAL: R$'))
        if saldo < 1000:
            print(negrito,'Digite um valor acima de R$1.000.',branco)
        else:
            break

    while True:
        limite_cred = float(input('LIMITE DE CRÉDITO: R$'))
        if limite_cred < 0:
            print(negrito,'Digite um valor maior ou igual a 0.',branco)
        else:
            break

    while True:
        senha_cli = input('SENHA: ')
        if senha_cli == '' or senha_cli == ' ':
            print(negrito,'Este campo deve ser preenchido!',branco)

        elif len(senha_cli) < 6:
            print(negrito,'Sua senha deve ter 6 ou mais digitos!',branco)

        if len(senha_cli) >= 6 and senha_cli != '':
            repita_senha = input('REPITA SUA SENHA: ')
            if repita_senha != senha_cli:
                print(negrito,'As senhas devem ser idênticas!',branco)
            else:
                break
    print(verde,"CADASTRO REALIZADO!",branco)
                
            
def depositar():
    global saldo
    print(negrito,'\nMACK BANK - DEPÓSITO NA CONTA',branco)

    while True:
        num_confirma = int(input('NÚMERO DA CONTA: '))
        if num_confirma != num_conta:
            print('O número da conta é inválido.')
        else:
            print(f'NOME DO CLIENTE: {nome_cli}')
            break
            
    while True:
        deposito = float(input(f'{nome_cli.split()[0]}, INSIRA O VALOR DO DEPÓSITO: R$'))
        if deposito <= 0:
            print('Por favor, insira um valor.')
        else:
            break
        
    saldo += deposito
    historico.append(deposito)
    print(verde,'DEPÓSITO REALIZADO COM SUCESSO!',branco)


def sacar():
    global saldo, limite_cred, cont1

    print(negrito,'\nMACK BANK - SAQUE DA CONTA',branco)
    while True:
        num_confirma = int(input('NÚMERO DA CONTA: '))
        if num_confirma != num_conta:
            print(vermelho,'Número da conta inválido.',branco)
        else:
            break

    
    while cont1 > 0 and cont1 <= 3:
        senha_confirma = input(f'INFORME A SENHA (lembre-se: suas tentativas são limitadas a 3 chances): ')
        if senha_confirma != senha_cli:
            print(vermelho,f'Senha incorreta.',branco)
            cont1 -= 1

        else:
            print(f'NOME DO CLIENTE: {nome_cli}')
            while True:
                saque = float(input(f'{nome_cli.split()[0]}, INFORME O VALOR DO SAQUE: R$'))
                if saque <= 0:
                    print(negrito,'Por favor, informe um valor para sacar.',branco)
                else:
                    break

            if saque <= saldo:
                saldo -= saque
                s = saque * -1
                historico.append(s)
                print(verde,'SAQUE REALIZADO COM SUCESSO!\n',branco)
                break

            if (saque > (limite_cred + saldo)):
                print(vermelho,"Desculpe, você não tem crédito suficiente para realizar o saque.",branco)
                break

            if (saque <= (saldo + limite_cred)):
                while True:
                    usar_cred = input('ATENÇÃO! Você não possui saldo suficiente, deseja usar seus créditos? ').upper()
                    if usar_cred != "SIM" and usar_cred != "S" and usar_cred != "NAO" and usar_cred != "N":
                        print("Dgite uma resposta válida.")
                    elif usar_cred == "NÃO" or usar_cred  == "N" or usar_cred == "NAO":
                            print(negrito,"OK. O saque não será realizado!",branco)
                            break
                    elif usar_cred == "SIM" or usar_cred == "S":
                        aux = saque - saldo
                        saldo -= saldo
                        limite_cred -= aux
                        s = saque * -1 
                        historico.append(s)
                        print(verde,"SAQUE REALIZADO COM SUCESSO!",branco)
                        break
                break
    else:
        print(vermelho,'Suas tentativas acabaram. Sua conta será bloqueada.',branco)
        

def consultar_saldo(saldo, limite_cred):
    global cont2

    print(negrito,'\nMACK BANK - CONSULTAR SALDO',branco)
    while True:
        num_confirma = int(input('INFORME O NÚMERO DA CONTA: '))
        if num_confirma != num_conta:
                print(vermelho,'Número da conta inválido.',branco)
        else:
            break

    print(f'NOME DO CLIENTE: {nome_cli}')
    while cont2 > 0 and cont2 <= 3:
        senha_confirma = input('INFORME A SENHA (lembre-se: suas tentativas são limitadas a 3 chances): ')
        if senha_cli != senha_confirma:
            print(vermelho,f'Senha incorreta.',branco)
            cont2 -=1
        else:
            print(f'\nSALDO EM CONTA: R${saldo:.2f}')
            print(f'CRÉDITO DISPONÍVEL: R${limite_cred:.2f}\n')
            break
    else:
        print(vermelho,"Suas tentativas acabaram. Sua conta será bloqueada.",branco)
   

def consultar_extrato():
    global cont3

    print(negrito,'\nMACK BANK - EXTRATO DA CONTA',branco)
    while True:
        num_confirma = int(input('INFORME O NÚMERO DA CONTA: '))
        if num_conta != num_confirma:
            print(vermelho,'Número de conta inválido.',branco)
        else:
            break
   
    while cont3 > 0 and cont3 <= 3:
        senha_confirma = input(f'INFORME A SENHA (lembre-se: você só tem 3 tentativas): ')
        if senha_cli != senha_confirma:
            print(vermelho,'Senha inválida.',branco)
            cont3 -= 1
        else:
            for i in historico:
                if i > 0:
                    print(verde,f'DEPÓSITO: R${i:.2f}',branco)
                else:
                    print(vermelho,f'SAQUE: R${i:.2f}',branco)
            break
    else:
        print(vermelho,'Suas tentativas acabaram. Sua conta será bloqueada.',branco)


def dados_pessoais():
    print(negrito,'\nMACK BANK - DADOS PESSOAIS',branco)
    print(f"CONTA: {num_conta}")
    print(f"NOME: {nome_cli}")
    print(f"TELEFONE: {tel}")
    print(f"E-MAIL: {email_cli}")


def finalizar():
    print(negrito,'\nMACK BANK - SOBRE',branco)
    print('Este projeto foi desenvolvido por:'
        '\nBeatriz Pimenta - TIA: 42339561'
        '\nIsabella Sofia Martins - TIA: 32388748'
        '\nLetícia Santiago - TIA: 32396414')


def menu(cadastro_realizado):
    global cont1, cont2, cont3
    while True:
        print(negrito,'\nMACK BANK - ESCOLHA UMA OPÇÃO',branco)
        print(
            '(1) CADASTRAR CONTA CORRENTE'
            '\n(2) DEPOSITAR'
            '\n(3) SACAR'
            '\n(4) CONSULTAR SALDO'
            '\n(5) CONSULTAR EXTRATO'
            '\n(6) CONSULTAR DADOS PESSOAIS'
            '\n(7) FINALIZAR'
            )
        opcao = int(input('Digite uma opção entre 1 a 7: '))
        if opcao < 1 or opcao > 7:
            print(negrito,'Por favor, digite uma opção válida!',branco)

        if cont1 == 0 or cont2 == 0 or cont3 == 0:  #validação da contagem de tentativas de senha
            print(vermelho,'Desculpe. A sua conta foi bloqueada.',branco)   
            break
        if opcao > 1 and opcao <= 7 and cadastro_realizado == False:
                print(negrito,'O cadastro deve ser realizado para ter acesso a essa opção.')

        if opcao == 1:
            if not cadastro_realizado:
                cadastro()
                cadastro_realizado = True
            else:
                print('O cadastro já foi realizado! Você não pode acessar essa opção novamente.')  #só pode acessar o cadastro uma vez com cada conta   
        if cadastro_realizado == True:
            if opcao == 2:
                    depositar()
            if opcao == 3:
                    sacar()
            if opcao == 4:
                    consultar_saldo(saldo,limite_cred)
            if opcao == 5:
                    consultar_extrato()
            if opcao == 6:
                    dados_pessoais()
            if opcao == 7:
                    finalizar()


cont1 = 3
cont2 = 3
cont3 = 3
historico = []
cadastro_realizado = False
menu(cadastro_realizado)