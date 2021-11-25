def calculadora(a):
    resultado = str(eval(a))
    print(resultado)

a = input("Digite  a expressão: ")
calculadora(a)

def raiz(n):
  if n < 0:
    return    
  else:
    return n ** 0.5
    

n=int(input('Digite um numero para calcular a raiz quadrada: '))
print(raiz(n))

