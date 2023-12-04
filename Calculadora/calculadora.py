import math

class calculadora:
    def __init__(self, soma ,subtração, divisao, multiplicação, raizquadrada, potencia):
       self.soma =  soma
       self.divisao = divisao
       self.multiplicação = multiplicação
       self.raizquadrada = raizquadrada
       self.potencia = potencia
       self.subtração = subtração


    def Soma(self,x,y):
        return x+y

    def Subtração(self,x,y):
        return x-y

    def Divisao(self, numero ,x,y):
        try:
            return x/y
        except ZeroDivisionError:
          print("erro divisao por zero")
        else:
          print("O resultado da divisao é:", numero)
        finally:
          print("erro corrigido")


    def Multiplicação(self,resultado,x,y): 
        self.multiplicação = x*y
        math.round(resultado, 2)

    def Raizquadrada(self, num):
        if num < 0:
            print("impossivel raiz quadrada de valores negativos")
            return None
        return math.sqrt(num)

    def Potencia(self ,y,x):
       self.potencia_resultado = math.pow(x, y)
       self.potencia_resultado = round(self.potencia_resultado, 2)
       print(f'O resultado da potência é {self.potencia_resultado}')



        
       

        
