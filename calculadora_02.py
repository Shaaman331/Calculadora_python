# adição
def adicao(valor_1, valor_2): # a + b
    return valor_1 + valor_2

# subtração
def subtracao(valor_1, valor_2): # a - b
    return valor_1 - valor_2

# multiplicação
def multiplicacao(valor_1, valor_2): # a * b
    return valor_1 * valor_2

# divisão
def divisao(valor_1, valor_2): # a / b
    return valor_1 / valor_2

print("\nDigite: \n\na para adição \ns para subtração \nm para multiplicação \nd para divisão")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo numero: "))

escolha = input("Escolha a operação:")

# adição
if escolha == 'a':
    print(adicao(a, b)) # valor_1 + valor_2

# subtração

if escolha == 's':
    print(subtracao(a, b)) # valor_1 - valor_2

# multiplicação

if escolha == 'm':
    print(multiplicacao(a, b)) # valor_1 * valor_2

# divisão
if escolha == 'd':
    print(divisao(a, b))    # valor_1 / valor_2

