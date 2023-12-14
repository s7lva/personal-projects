from Conta import *

teste = True
while True:
    print("escolha uma opção")
    print("1 .create acount")
    print("2.login")
    print("3.sair")
    while teste:
            try:
                op=int(input())   
            except ValueError:
                print("Valor inválido. Digite um valor entre 1 e 3")
            else:
                teste = False


    
    match op:
        case 1:
            nome=(input("digite um nome"))

            try:
                pin=int(input("escolha um pin minimo 8 caracteres"))
            except ValueError:
                print("O pin apenas pode conter numeros")

            numerotelemovel=(input("introduza o seu numero telemovel"))
            email =(input("introduza o seu email"))
            dados= (f'os seus dados da conta serão: {nome}/{pin}/{numerotelemovel}/{email}')

        case 2:
            email=(input("introduza o seu email"))
            pin=(input("introduza o seu pin"))
            dados=(f'O os dados de acesso a conta são:{pin} e {email}')
        case 3:
            break
    teste= True

   