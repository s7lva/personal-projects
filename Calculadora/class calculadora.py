from calculadora import calculadora 
import math

def main():
    calc = calculadora(0,0,0,0,0,0) 

    while True:
        try:
            escolha = input("Digite o número da operação desejada: ")
        except ValueError:
            print("Valor inválido. Digite um valor entre 1 a 7")

        print("Escolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz quadrada")
        print("6. Potência")
        print("7. Sair")

        if escolha == '7':
            print("Encerrando a calculadora.")
            break
        elif escolha in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = calc.Soma(num1, num2)
                operacao = num1 + num2
            elif escolha == '2':
                resultado = calc.Subtração(num1, num2)
                operacao = num1-num2
            elif escolha == '3':
                resultado = calc.Multiplicação(num1,num2)
                operacao = num1 * num2
            elif escolha == '4':
                resultado = calc.Divisao(num1, num2)
                operacao = num1/num2
            elif escolha == '5':
                resultado = calc.Raizquadrada(num1)
                operacao = math.sqrt(num1, num2)
            elif escolha == '6':
                resultado = calc.Potencia(num1, num2)
                operacao = num1*num1

            print(f"O resultado da {operacao} é: {resultado}")

if __name__ == "__main__":
    main()